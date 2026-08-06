# 媒体数据处理算子

## 基本概念

调用媒体数据处理算子通常采用“两段式接口”形式，具体如下，其中_“_acldvpp”表示算子接口前缀=；而_“Xxx”_表示对应的算子类型，如EncodeJpeg算子。

```text
aclnnStatus acldvppXxxGetWorkspaceSize(const aclTensor *src, ..., aclTensor *out, ..., uint64_t *workspaceSize, aclOpExecutor **executor);
aclnnStatus acldvppXxx(void *workspace, uint64_t workspaceSize, aclOpExecutor *executor, aclrtStream stream);
```

两段式接口的作用分别为：

- 第一段接口acldvpp_Xxx_GetWorkspaceSize：该接口内部执行入参校验、在动态Shape场景下推导输出Shape、数据切块（Tiling）以及计算执行算子所需的workspace内存大小等任务。
- 第二段接口acldvpp_Xxx_：执行算子计算，接口内部涉及DFX（例如Dump、溢出检测等）、调用Runtime提供的LaunchKernel接口等_。_

接口调用流程如下所示：

![](figures/CJ220919103020546.png)

## 示例代码

以**JPEGE（JPEG Encoder）算子**调用为例，介绍算子两段式接口调用的基本逻辑，其他算子的调用过程类似，请根据实际情况自行修改。

已知JPEGE算子用于将单通道（GRAY）或三通道（RGB）图像编码为JPEG图像。您可以获取如下示例代码，并将文件命名为“**jpege\_demo.cpp**”，代码如下：

```cpp
#include <vector>
#include <string>
#include <cstdint>
#include <functional>

#include "acl/acl.h"
#include "acldvpp_op_api.h"
#include <memory>

#define ALIGN_UP(x, a) ((((x) + ((a) - 1U)) / (a)) * (a))

typedef int32_t (*InitFunc)(const char *configPath);
typedef int32_t (*FinalizeFunc)();

InitFunc initFunc;
FinalizeFunc finalizeFunc;

class ScopeGuard {
    public:
    // Noncopyable
    ScopeGuard(ScopeGuard const &) = delete;
    ScopeGuard &operator=(ScopeGuard const &) = delete;

    explicit ScopeGuard(const std::function<void()> &on_exit_scope) : on_exit_scope_(on_exit_scope), dismissed_(false) {}

    ~ScopeGuard() {
        if (!dismissed_) {
            if (on_exit_scope_ != nullptr) {
            try {
                on_exit_scope_();
            } catch (std::bad_function_call &) { }
                catch (...) { }
            }
        }
    }

    void Dismiss() { dismissed_ = true; }

    private:
    std::function<void()> on_exit_scope_;
    bool dismissed_;
};

int64_t GetShapeSize(const std::vector<int64_t>& shape)
{
    int64_t shape_size = 1;
    for (auto i : shape) {
        shape_size *= i;
    }
    return shape_size;
}

// 自定义函数，用于创建Tensor
template <typename T>
int32_t CreateAclTensor(const std::vector<T>& hostData, const std::vector<int64_t>& shape, void** deviceAddr,
    aclDataType dataType, aclTensor** tensor, aclFormat tensorFormat, bool needCopy = true) {
    auto size = GetShapeSize(shape) * sizeof(T);

    // 申请Device内存
    aclrtMalloc(deviceAddr, size, ACL_MEM_MALLOC_HUGE_FIRST);
    aclrtMemset(*deviceAddr, size, 0, size);
    // 将Host侧数据拷贝到Device侧
    aclrtMemcpy(*deviceAddr, size, hostData.data(), size, ACL_MEMCPY_HOST_TO_DEVICE);

    // 计算连续Tensor的访问步长
    std::vector<int64_t> strides(shape.size(), 1);
    for (int64_t i = shape.size() - 2; i >= 0; i--) {
      strides[i] = shape[i + 1] * strides[i + 1];
    }

    // 创建aclTensor
    *tensor = aclCreateTensor(shape.data(), shape.size(), dataType, strides.data(), 0, tensorFormat,
                              shape.data(), shape.size(), *deviceAddr);
    return 0;
}

int32_t encode_jpeg(aclrtStream stream) {
    constexpr uint32_t jpegeHeaderSize = 640U;
    constexpr uint32_t startAlignBytes = 128U;
    constexpr uint32_t memoryAlignSize = 2097152U; // 2M: 2*1024*1024
    int64_t inChannel = 0;
    uint32_t inWidth = 1920;
    uint32_t inHeight = 1080;

    // 1. 初始化参数
    std::vector<int64_t> selfShape = {1, inChannel, inHeight, inWidth}; // 默认 NCHW
    uint32_t encode_size = ALIGN_UP(inWidth, 16U) * ALIGN_UP(inHeight, 16U) * 3 / 2 +
        jpegeHeaderSize + startAlignBytes;
    encode_size = ALIGN_UP(encode_size, memoryAlignSize);
    std::vector<int64_t> outShape = {encode_size};
    std::vector<float> inputPic(inWidth * inHeight * inChannel, 0.0);
    std::vector<float> outputPic(encode_size, 0.0);
    size_t inputPicSize = inWidth * inHeight * inChannel;

    std::shared_ptr<FILE> srcFp(fopen("./1920x1080_nv12.yuv", "rb"), fclose);
    fread(inputPic.data(), 1, inputPicSize, srcFp.get());

    // 2. 创建输入输出，将vector转成aclTensor
    void* selfDeviceAddr = nullptr;
    void* outDeviceAddr = nullptr;
    aclTensor* self = nullptr;
    aclTensor* out = nullptr;
    CreateAclTensor(inputPic, selfShape, &selfDeviceAddr, aclDataType::ACL_UINT8, &self, aclFormat::ACL_FORMAT_NCHW);
    ScopeGuard autoCloseInTensor([self, selfDeviceAddr] { aclrtFree(self);aclDestroyTensor((const aclTensor *)selfDeviceAddr);});

    // 每次执行完输出Tensor Shape会修改，因此性能测试将输出Tensor构造放到循环内部，不然会第二次执行会被内部拦截
    // 放到内部时，最后执行完文件无法保留，因为内存提前释放了
    CreateAclTensor(outputPic, outShape, &outDeviceAddr, aclDataType::ACL_UINT8, &out, ACL_FORMAT_ND, false);
    ScopeGuard autoCloseOutTensor([out, outDeviceAddr] { aclrtFree(out);aclDestroyTensor((const aclTensor *)outDeviceAddr);});

    // 3. 调用CANN算子库API
    uint64_t workspaceSize = 0;
    aclOpExecutor* executor;
    const uint32_t quality = 75;
    // 调用第一段接口
    acldvppEncodeJpegGetWorkspaceSize(self, quality, out, &workspaceSize, &executor);
    // 根据第一段接口计算出的workspaceSize，并申请Device内存
    void* workspaceAddr = nullptr;
    if (workspaceSize > 0) {
        aclrtMalloc(&workspaceAddr, workspaceSize, ACL_MEM_MALLOC_HUGE_FIRST);
    }
    ScopeGuard autoWorkspace([workspaceAddr] { aclrtFree(workspaceAddr); });
    // 调用第二段接口
    acldvppEncodeJpeg(workspaceAddr, workspaceSize, executor, stream);

    // 获取编码后JPEG图片长度
    int64_t* viewDims = nullptr;
    uint64_t viewDimsNum = 0;
    aclGetViewShape(out, &viewDims, &viewDimsNum);
    std::vector<int64_t> outSize(viewDims, viewDims + viewDimsNum);
    size_t outputPicSize = outSize[0];

    //  获取输出的值，将Device内存中的结果数据拷贝至Host侧
    aclrtMemcpy(outputPic.data(), outputPicSize, outDeviceAddr, outputPicSize, ACL_MEMCPY_DEVICE_TO_HOST);

    std::shared_ptr<FILE> dstFp(fopen("./1920x1080_nv12.jpg", "wb+"), fclose);
    fwrite(outputPic.data(), 1, outputPicSize, dstFp.get());

    return 0;
}

int32_t Init(int32_t deviceId, aclrtContext* context, aclrtStream* stream)
{
    // 涉及Profiling功能需要调用aclInit接口初始化，如果不需要Profiling功能则直接调用acldvppInit接口即可
    initFunc = acldvppInit;
    finalizeFunc = acldvppFinalize;

    auto initFunc(nullptr);
    ScopeGuard autoDeinit([] { finalizeFunc(); });

    aclrtSetDevice(deviceId);
    ScopeGuard autoResetDevice([deviceId] { aclrtResetDevice(deviceId); });

    aclrtCreateContext(context, deviceId);
    ScopeGuard autoDestroyContext([context] { aclrtDestroyContext(context); });

    aclrtSetCurrentContext(*context);

    aclrtCreateStream(stream);
    ScopeGuard autoDestroyStream([stream] { aclrtDestroyStream(stream); });

    autoResetDevice.Dismiss();
    autoDestroyContext.Dismiss();
    autoDestroyStream.Dismiss();
    autoDeinit.Dismiss();
    return 0;
}

// 销毁Stream、Context资源，复位Device
void UnInit(int32_t deviceId, aclrtContext context, aclrtStream stream)
{
    aclrtDestroyStream(stream);
    aclrtDestroyContext(context);
    aclrtResetDevice(deviceId);
    finalizeFunc();
}

int32_t main() 
{

    // 初始化系统，指定计算设备，依次创建Context、Stream
    int32_t deviceId = 0;
    aclrtContext context;
    aclrtStream stream;
    Init(deviceId, &context, &stream);
    // jpeg图片编码
    encode_jpeg(stream);

    // 资源释放
    UnInit(deviceId, context, stream);
    return 0;
}
```

## 编译与运行

1. 准备编译脚本CMakeLists文件。

    ```cmake
    cmake_minimum_required(VERSION 3.14)
    
    set(ASCEND_PATH $ENV{ASCEND_HOME_PATH})
    
    # 设置可执行文件名（如opapi_test），并指定待运行cpp文件所在目录
    add_executable(opapi_test jpege_demo.cpp)
    
    # 设置库文件路径
    find_library(NNOPBASE_LIBRARY_DIR libnnopbase.so "${ASCEND_PATH}/lib64") # aclTensor 相关接口
    find_library(ACLDVPPOP_LIBRARY_DIR libacl_dvpp_op.so "${ASCEND_PATH}/lib64")
    find_library(DVPPOPBASE_LIBRARY_DIR libdvpp_op_base.so "${ASCEND_PATH}/lib64")
    find_library(ASCENDCL_LIBRARY_DIR libascendcl.so "${ASCEND_PATH}/lib64")
    find_library(ASCENDCL_C_SEC_DIR libc_sec.so "${ASCEND_PATH}/lib64")
    
    target_link_libraries(opapi_test PRIVATE
        -Wl,--no-as-needed
        ${NNOPBASE_LIBRARY_DIR}
        ${ACLDVPPOP_LIBRARY_DIR}
        ${ASCENDCL_LIBRARY_DIR}
        ${ASCENDCL_C_SEC_DIR}
        ${DVPPOPBASE_LIBRARY_DIR}
        -Wl,--as-needed
    )
    
    # 设置头文件路径
    target_include_directories(opapi_test PRIVATE
        ${ASCEND_PATH}/include/acldvppop/
        ${ASCEND_PATH}/include/
    )
    ```

2. 编译并运行。
    1. 进入CMakeLists.txt所在目录，执行如下命令，新建build目录存放生成的编译文件。

        ```bash
        mkdir -p build 
        ```

    2. 进入build所在目录，执行cmake命令编译，再执行make命令生成可执行文件。

        ```bash
        cd build
        cmake ..
        make
        ```

        编译成功后，会在build目录下生成opapi\_test可执行文件。

    3. 运行可执行文件opapi\_test。

        ```bash
        ./opapi_test
        ```
