# CANN内置算子调用

## 基本介绍

CANN算子库提供了一系列丰富且经过深度优化、硬件亲和的高性能内置算子，可直接应用于AI业务。算子包括Device侧Kernel实现和Host侧调用两部分，为方便调用，每个算子都提供了相应的C语言API，方便用户在Host侧调用，下文简称单算子API（或者算子Host API）。

本章主要阐述单算子API的调用，其采用“两段式接口”形式，以aclnn作为接口前缀，命名风格为驼峰格式，具体样式如下：

```text
aclnnStatus aclnnXxxGetWorkspaceSize(const aclTensor *src, ..., aclTensor *out, ..., uint64_t *workspaceSize, aclOpExecutor **executor)
aclnnStatus aclnnXxx(void *workspace, uint64_t workspaceSize, aclOpExecutor *executor, aclrtStream stream)
```

其中_“Xxx”_表示对应的算子类型，如Add算子。两段式接口具体作用如下：

- 第一段接口aclnn_Xxx_GetWorkspaceSize：完成入参校验、动态Shape场景下推导输出Shape、数据切块（Tiling）以及计算执行过程中算子所需的workspace内存大小等任务。
- 第二段接口aclnn_Xxx_：executor执行器执行计算，框架自动调用DFX（例如Dump、溢出检测等）、Runtime提供的LaunchKernel接口等_。_

## 算子分类

CANN算子主要包含如下几类：

- **Math类算子**：数值计算类算子，提供不同维度的数值处理与计算算子，例如Add、Abs等，覆盖张量形态变换、基础数学运算、随机数生成等场景。
- **NN类算子**：神经网络类算子（Neural Network），提供深度学习模型中常见的计算算子，例如卷积、矩阵乘、激活函数、归一化等。
- **CV类算子**：计算机视觉类算子（Computer Vision），提供图像处理和目标检测算子，例如GridSample等。
- **Transformer类算子**：大模型计算类算子，提供Transformer核心算子，例如Attention类、LayerNorm类、通算融合类（简称MC2）等。

    对于集合通信和MatMul计算融合、并行的算子，统称为通算融合算子（简称MC2算子），如AllGatherMatmul、AlltoAllAllGatherBatchMatMul、BatchMatMulReduceScatterAlltoAll、MatMulAllReduce、MatMulAllReduceAddRmsNorm、MatMulReduceScatter等。

关于算子IR（Intermediate Representation）规格介绍，请参见[《算子库》](https://hiascend.com/document/redirect/CannCommunityOplist)中“Ascend IR算子规格说明”；关于算子对应的API文档介绍，请参见[《算子库》](https://hiascend.com/document/redirect/CannCommunityOplist)中“算子接口（aclnn）”。

调用算子API时，请include依赖必要的头文件和库文件，其中$\{INSTALL\_DIR\}请替换为CANN软件安装后文件存储路径。以root用户安装为例，安装后文件默认存储路径为：/usr/local/Ascend/cann。

- 头文件路径：一般默认在“$\{INSTALL\_DIR\}/include/”目录，可引用每类算子总头文件aclnnop/aclnn\_ops\_math.h、aclnnop/aclnn\_ops\_nn.h、aclnnop/aclnn\_ops\_cv.h、aclnnop/aclnn\_ops\_transformer.h；也可以引用单个算子头文件

    aclnnop/aclnn\_\*.h（\*表示具体算子名）。

- 库文件路径：一般默认在“$\{INSTALL\_DIR\}/lib64/”目录，可引用每类算子总库文件libopapi\_math.so、libopapi\_nn.so、libopapi\_cv.so、libopapi\_transformer.so。注意，从CANN 8.5.0版本开始全量算子总库文件libopapi.so要废弃，请勿使用。

如需进一步了解CANN算子库的实现，请访问[CANN开源项目](https://gitcode.com/cann)，学习算子源码的实现过程。

## 单算子API调用流程

**图 1**  单算子API调用流程  
![](figures/aclnn_API_call_process.png "单算子API调用流程")

关键接口说明如下，过程中使用的acl前缀接口详细介绍可参考《Runtime运行时API》。

1. **初始化：**调用aclInit接口实现初始化。

2. **运行时资源申请：**调用aclrtSetDevice、aclrtCreateStream等接口，依次申请运行时资源即Device、Context、Stream。

3. **数据内存申请和传输。**

    1. 调用aclrtMalloc接口申请Device上的内存，存放待执行算子的输入、输出数据。
    2. 调用aclCreateTensor、aclCreateIntArray等构造算子输入、输出参数，相关接口详见[《算子库》](https://hiascend.com/document/redirect/CannCommunityOplist)中“公共接口”。

    如果需要将Host上数据传输到Device，则需要调用aclrtMemcpy接口（同步接口）或aclrtMemcpyAsync接口（异步接口）通过内存复制的方式实现数据传输。

4. **计算workspace并执行算子**。
    1. 调用acl_xx__Xxx_GetWorkspaceSize接口获取算子入参，并计算该算子执行时需要的workspace大小。
    2. 调用aclrtMalloc接口，根据workspace大小申请Device侧内存。
    3. 调用acl_xx__Xxx_接口执行计算并得到结果。

5. 调用aclrtSynchronizeStream接口**阻塞应用运行**，直到指定Stream中的所有任务都完成。
6. 调用aclrtFree接口**释放内存**。

    如果需要将Device上的算子执行结果数据传输到Host，则需要调用aclrtMemcpy接口（同步接口）或aclrtMemcpyAsync接口（异步接口）通过内存复制的方式实现数据传输，然后再释放内存。

7. **运行时资源释放**。
    1. 调用aclDestroyTensor、aclDestroyIntArray等接口释放算子输入、输出参数，相关接口详见[《算子库》](https://hiascend.com/document/redirect/CannCommunityOplist)中“公共接口”。
    2. 所有数据释放后，调用aclrtDestroyStream、aclrtResetDevice等接口，依次释放运行时资源即Stream、Context、Device。

8. **去初始化：**调用aclFinalize接口实现去初始化。

<a id="section9465185611515"></a>

## 示例代码

以**Add算子API调用**为例，介绍算子两段式接口调用的基本逻辑，其他算子调用过程类似，请根据实际情况自行修改。

已知Add算子实现了张量加法运算，计算公式为：y=x<sub>1</sub>+αxx<sub>2</sub>。您可以获取如下示例代码，并将文件命名为“**test\_add.cpp**”，代码如下：

```cpp
#include <iostream>
#include <vector>
#include "acl/acl.h"
#include "aclnnop/aclnn_add.h"

#define CHECK_RET(cond, return_expr) \
  do {                               \
    if (!(cond)) {                   \
      return_expr;                   \
    }                                \
  } while (0)

#define LOG_PRINT(message, ...)     \
  do {                              \
    printf(message, ##__VA_ARGS__); \
  } while (0)

int64_t GetShapeSize(const std::vector<int64_t>& shape) {
  int64_t shape_size = 1;
  for (auto i : shape) {
    shape_size *= i;
  }
  return shape_size;
}

int Init(int32_t deviceId, aclrtStream* stream) {
  // 固定写法，初始化
  auto ret = aclInit(nullptr);
  CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclInit failed. ERROR: %d\n", ret); return ret);
  ret = aclrtSetDevice(deviceId);
  CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclrtSetDevice failed. ERROR: %d\n", ret); return ret);
  ret = aclrtCreateStream(stream);
  CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclrtCreateStream failed. ERROR: %d\n", ret); return ret);
  return 0;
}

template <typename T>
int CreateAclTensor(const std::vector<T>& hostData, const std::vector<int64_t>& shape, void** deviceAddr,
                    aclDataType dataType, aclTensor** tensor) {
  auto size = GetShapeSize(shape) * sizeof(T);
  // 调用aclrtMalloc申请device侧内存
  auto ret = aclrtMalloc(deviceAddr, size, ACL_MEM_MALLOC_HUGE_FIRST);
  CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclrtMalloc failed. ERROR: %d\n", ret); return ret);
  // 调用aclrtMemcpy将host侧数据拷贝到device侧内存上
  ret = aclrtMemcpy(*deviceAddr, size, hostData.data(), size, ACL_MEMCPY_HOST_TO_DEVICE);
  CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclrtMemcpy failed. ERROR: %d\n", ret); return ret);
  // 计算连续tensor的strides
  std::vector<int64_t> strides(shape.size(), 1);
  for (int64_t i = shape.size() - 2; i >= 0; i--) {
    strides[i] = shape[i + 1] * strides[i + 1];
  }
  // 调用aclCreateTensor接口创建aclTensor
  *tensor = aclCreateTensor(shape.data(), shape.size(), dataType, strides.data(), 0, aclFormat::ACL_FORMAT_ND,
                            shape.data(), shape.size(), *deviceAddr);
  return 0;
}

int main() {
  // 1. （固定写法）device/stream初始化
  // 根据自己的实际device填写deviceId
  int32_t deviceId = 0;
  aclrtStream stream;
  auto ret = Init(deviceId, &stream);
  // check根据自己的需要处理
  CHECK_RET(ret == 0, LOG_PRINT("Init acl failed. ERROR: %d\n", ret); return ret);

  // 2. 构造输入与输出，需要根据API的接口自定义构造
  std::vector<int64_t> selfShape = {4, 2};
  std::vector<int64_t> otherShape = {4, 2};
  std::vector<int64_t> outShape = {4, 2};
  void* selfDeviceAddr = nullptr;
  void* otherDeviceAddr = nullptr;
  void* outDeviceAddr = nullptr;
  aclTensor* self = nullptr;
  aclTensor* other = nullptr;
  aclScalar* alpha = nullptr;
  aclTensor* out = nullptr;
  std::vector<float> selfHostData = {0, 1, 2, 3, 4, 5, 6, 7};
  std::vector<float> otherHostData = {1, 1, 1, 2, 2, 2, 3, 3};
  std::vector<float> outHostData = {0, 0, 0, 0, 0, 0, 0, 0};
  float alphaValue = 1.2f;
  // 创建self aclTensor
  ret = CreateAclTensor(selfHostData, selfShape, &selfDeviceAddr, aclDataType::ACL_FLOAT, &self);
  CHECK_RET(ret == ACL_SUCCESS, return ret);
  // 创建other aclTensor
  ret = CreateAclTensor(otherHostData, otherShape, &otherDeviceAddr, aclDataType::ACL_FLOAT, &other);
  CHECK_RET(ret == ACL_SUCCESS, return ret);
  // 创建alpha aclScalar
  alpha = aclCreateScalar(&alphaValue, aclDataType::ACL_FLOAT);
  CHECK_RET(alpha != nullptr, return ret);
  // 创建out aclTensor
  ret = CreateAclTensor(outHostData, outShape, &outDeviceAddr, aclDataType::ACL_FLOAT, &out);
  CHECK_RET(ret == ACL_SUCCESS, return ret);

  // 3. 调用CANN算子库API，需要修改为具体的算子接口
  uint64_t workspaceSize = 0;
  aclOpExecutor* executor;
  // 调用aclnnAdd第一段接口
  ret = aclnnAddGetWorkspaceSize(self, other, alpha, out, &workspaceSize, &executor);
  CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclnnAddGetWorkspaceSize failed. ERROR: %d\n", ret); return ret);
  // 根据第一段接口计算出的workspaceSize申请device内存
  void* workspaceAddr = nullptr;
  if (workspaceSize > 0) {
    ret = aclrtMalloc(&workspaceAddr, workspaceSize, ACL_MEM_MALLOC_HUGE_FIRST);
    CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("allocate workspace failed. ERROR: %d\n", ret); return ret);
  }
  // 调用aclnnAdd第二段接口
  ret = aclnnAdd(workspaceAddr, workspaceSize, executor, stream);
  CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclnnAdd failed. ERROR: %d\n", ret); return ret);

  // 4.（ 固定写法）同步等待任务执行结束
  ret = aclrtSynchronizeStream(stream);
  CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("aclrtSynchronizeStream failed. ERROR: %d\n", ret); return ret);

  // 5. 获取输出的值，将device侧内存上的结果拷贝至host侧，需要根据具体API的接口定义修改
  auto size = GetShapeSize(outShape);
  std::vector<float> resultData(size, 0);
  ret = aclrtMemcpy(resultData.data(), resultData.size() * sizeof(resultData[0]), outDeviceAddr, size * sizeof(float),
                    ACL_MEMCPY_DEVICE_TO_HOST);
  CHECK_RET(ret == ACL_SUCCESS, LOG_PRINT("copy result from device to host failed. ERROR: %d\n", ret); return ret);
  for (int64_t i = 0; i < size; i++) {
    LOG_PRINT("result[%ld] is: %f\n", i, resultData[i]);
  }

  // 6. 释放aclTensor和aclScalar，需要根据具体API的接口定义修改
  aclDestroyTensor(self);
  aclDestroyTensor(other);
  aclDestroyScalar(alpha);
  aclDestroyTensor(out);
 
  // 7. 释放device资源，需要根据具体API的接口定义修改
  aclrtFree(selfDeviceAddr);
  aclrtFree(otherDeviceAddr);
  aclrtFree(outDeviceAddr);
  if (workspaceSize > 0) {
    aclrtFree(workspaceAddr);
  }
  aclrtDestroyStream(stream);
  aclrtResetDevice(deviceId);
  aclFinalize();
  return 0;
}
```

<a id="section1930615371323"></a>

## CMakeLists文件

以**Add算子**编译为例，CMake文件定义如下，请根据实际情况自行修改。

```cmake
# CMake lowest version requirement
cmake_minimum_required(VERSION 3.14)

# 设置工程名
project(ACLNN_EXAMPLE)

# Compile options
add_compile_options(-std=c++11)

# 设置编译选项
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY  "./bin")    
set(CMAKE_CXX_FLAGS_DEBUG "-fPIC -O0 -g -Wall")
set(CMAKE_CXX_FLAGS_RELEASE "-fPIC -O2 -Wall")

# 设置可执行文件名（如opapi_test），并指定待运行算子文件*.cpp所在目录
add_executable(opapi_test
               test_add.cpp) 

# 设置ASCEND_PATH（CANN软件包目录，请根据实际路径修改）和INCLUDE_BASE_DIR（头文件目录）
if(NOT "$ENV{ASCEND_CUSTOM_PATH}" STREQUAL "")      
    set(ASCEND_PATH $ENV{ASCEND_CUSTOM_PATH})
else()
    set(ASCEND_PATH "/usr/local/Ascend/cann")
endif()
set(INCLUDE_BASE_DIR "${ASCEND_PATH}/include")
include_directories(
    ${INCLUDE_BASE_DIR}
    ${INCLUDE_BASE_DIR}/aclnn
)

# 设置链接的库文件路径
target_link_libraries(opapi_test PRIVATE
                      ${ASCEND_PATH}/lib64/libascendcl.so
                      ${ASCEND_PATH}/lib64/libnnopbase.so
                      ${ASCEND_PATH}/lib64/libopapi_${ops_project}.so)

# 可执行文件在CMakeLists文件所在目录的bin目录下
install(TARGETS opapi_test DESTINATION ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})
```

其中$\{ops\_project\}表示不同类型算子库，请按需引用：

- Math类算子：引用对应libopapi\_math.so。
- NN类算子：引用libopapi\_math.so和libopapi\_nn.so。
- CV类算子：引用libopapi\_math.so和libopapi\_cv.so。
- Transformer类算子：引用libopapi\_math.so和libopapi\_transformer.so。

调用MC2算子API时，一般会涉及多线程和HCCL（Huawei Collective Communication Library，集合通信库），因此CMake文件需要额外导入如下内容，否则无法成功编译。

```cmake
# 设置链接的库文件路径
find_package(Threads REQUIRED)                        
target_link_libraries(opapi_test PRIVATE
                      ${ASCEND_PATH}/lib64/libascendcl.so
                      ${ASCEND_PATH}/lib64/libnnopbase.so
                      ${ASCEND_PATH}/lib64/libopapi_${ops_project}.so
                      ${ASCEND_PATH}/lib64/libhccl.so      # 集合通信库文件
                      ${CMAKE_THREAD_LIBS_INIT})            # 多线程依赖的库文件
```

“find\_package\(Threads REQUIRED\)”是CMake用于查找线程库的命令，可自动链接线程库依赖的头文件和间接依赖的其它库文件。

## 编译与运行

本节以**开发和运行环境合设场景**为例，即带AI处理器的机器既作为开发环境又作为运行环境。该场景下，代码开发与代码运行在同一台机器上。

1. 根据前文提供的[示例代码](#section9465185611515)、[CMakeLists文件](#section1930615371323)，提前准备好算子的调用代码（\*.cpp）和编译脚本（CMakeLists.txt）。
2. 配置环境变量。

    安装CANN软件后，使用CANN运行用户登录环境，执行如下命令生效环境变量。

    ```bash
    source /usr/local/Ascend/cann/set_env.sh
    ```

3. 编译并运行。
    1. 进入CMakeLists.txt所在目录，执行如下命令，新建build目录存放生成的编译文件。

        ```bash
        mkdir -p build 
        ```

    2. 进入build所在目录，执行cmake命令编译，再执行make命令生成可执行文件。

        ```bash
        cd build
        cmake ../ -DCMAKE_CXX_COMPILER=g++ -DCMAKE_SKIP_RPATH=TRUE
        make
        ```

        编译成功后，会在build目录的bin文件夹下生成opapi\_test可执行文件。

    3. 进入bin目录，运行可执行文件opapi\_test。

        ```bash
        cd bin
        ./opapi_test
        ```

        以Add算子的运行结果为例，运行后的结果如下：

        ![](figures/add_operator_execution_result.png)
