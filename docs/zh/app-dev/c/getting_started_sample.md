# 入门样例

## 样例功能

本样例展示了如何使用CANN的Runtime API以及算子库中的Add算子实现向量加法运算out = self + alpha \* other。

```bash
Input vectors:
  self:   [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
  other:  [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
  alpha:  1.0

Vector addition result:
  out:   [1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0]
```

## 编译及运行应用

您可以单击[Link](https://gitcode.com/cann/runtime/tree/master/example/0_quickstart/0_hello_cann)获取完整样例代码，同时，该样例的README.md文件中也提供了编译和运行的指导。

## 了解关键代码逻辑

本节按照应用开发的顺序介绍样例代码的逻辑：**资源初始化 → 创建Stream → 准备输入 → 调用Add算子 → 输出结果 → 释放资源→ 资源去初始化**。通过本节的介绍，还可以帮助您了解CANN应用开发中关键API的功能，这些关键API的接口名前缀为acl，下文简称acl接口。

1. **资源初始化**。

    ```cpp
    // 初始化系统，nullptr表示采用默认配置初始化系统，调用其它acl接口前，必须先初始化，否则可能会导致后续系统内部资源初始化出错，进而导致其它业务异常
    aclInit(nullptr); 
    
    // 指定计算设备
    int32_t deviceId = 0;
    aclrtSetDevice(deviceId);
    ```

2. **创建Stream**。

    ```cpp
    // Stream相当于一个任务队列，任务按照进入队列的顺序依次执行
    aclrtStream stream = nullptr;
    aclrtCreateStream(&stream);
    ```

3. **准备输入。**

    根据Add算子的计算公式（out = self + alpha \* other），self和other为相加的两个输入向量，alpha为系数，out为相加后的结果向量。因此在准备输入时，涉及创建两个输入Tensor、创建一个表示系数的Scalar、创建一个输出Tensor。在创建输入、输出Tensor时，涉及申请Device内存存放输入或输出数据。

    1. **定义一个创建Tensor的通用接口。**

        ```cpp
        template <typename T>
        int CreateAclTensor(const std::vector<T>& hostData, const std::vector<int64_t>& shape, void** deviceAddr, aclDataType dataType, aclTensor** tensor)
        {
            auto size = GetShapeSize(shape) * sizeof(T);
            // 申请Device内存
            aclrtMalloc(deviceAddr, size, ACL_MEM_MALLOC_HUGE_FIRST);
            // 将输入数据从Host同步复制到Device
            aclrtMemcpy(*deviceAddr, size, hostData.data(), size, ACL_MEMCPY_HOST_TO_DEVICE);
            // 计算strides
            std::vector<int64_t> strides(shape.size(), 1);
            for (int64_t i = shape.size() - 2; i >= 0; i--) {
                strides[i] = shape[i + 1] * strides[i + 1];
            }
            // 创建Tensor
            *tensor = aclCreateTensor(shape.data(), shape.size(), dataType, strides.data(), 0, aclFormat::ACL_FORMAT_ND, shape.data(), shape.size(), *deviceAddr);
            return 0;
        }
        ```

    2. **创建输入、输出Tensor以及一个系数Scalar。**

        ```cpp
        std::vector<int64_t> shape{8}; // 向量长度为8
        void* selfDeviceAddr = nullptr;
        void* otherDeviceAddr = nullptr;
        void* outDeviceAddr = nullptr;
        aclDataBuffer* outDataBuffer = nullptr;
        aclTensor* self = nullptr;
        aclTensor* other = nullptr;
        aclTensor* out = nullptr;
        aclScalar* alpha = nullptr;
        std::vector<float> selfHostData = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f};    // self向量输入数据
        std::vector<float> otherHostData = {0.5f, 1.0f, 1.5f, 2.0f, 2.5f, 3.0f, 3.5f, 4.0f};   // other向量输入数据
        std::vector<float> outHostData(8, 0.0f);   
        float alphaValue = 1.0f;       // 系数值
        
        // 创建输入 Tensor
        CreateAclTensor(selfHostData, shape, &selfDeviceAddr, aclDataType::ACL_FLOAT, &self);
        CreateAclTensor(otherHostData, shape, &otherDeviceAddr, aclDataType::ACL_FLOAT, &other);
        // 创建 alpha Scalar
        alpha = aclCreateScalar(&alphaValue, aclDataType::ACL_FLOAT);
        // 创建输出 Tensor
        CreateAclTensor(outHostData, shape, &outDeviceAddr, aclDataType::ACL_FLOAT, &out);
        ```

4. **调用Add算子**。

    ```cpp
    // 调用CANN内置的算子，通常调用两段式接口
    
    // 第一段接口aclnnAddGetWorkspaceSize，该接口内部执行入参校验、在动态Shape场景下推导输出Shape、数据切块（Tiling）以及计算执行算子所需的workspace内存大小等任务
    uint64_t workspaceSize = 0;
    aclOpExecutor* executor = nullptr;
    ret = aclnnAddGetWorkspaceSize(self, other, alpha, out, &workspaceSize, &executor);
    
    // 第二段接口aclnnAdd，执行算子计算，接口内部涉及DFX（例如Dump、溢出检测等）、调用Runtime提供的LaunchKernel接口等
    // workspaceAddr表示在Device侧申请的workspace内存地址
    ret = aclnnAdd(workspaceAddr, workspaceSize, executor, stream);
    
    // 同步等待任务完成
    aclrtSynchronizeStream(stream);
    ```

5. **输出结果。**

    将Device侧的结果数据回传到Host上。

    ```cpp
    // outBufferAddr表示存放Device侧结果数据的内存地址
    // resultData.data()表示存放Host侧数据的内存地址
    aclrtMemcpy(resultData.data(), resultData.size() * sizeof(float), outBufferAddr, size * sizeof(float), ACL_MEMCPY_DEVICE_TO_HOST);
    ```

6. **释放资源。**

    ```cpp
    // 销毁Tensor和Scalar
    aclDestroyTensor(self);
    aclDestroyTensor(other);
    aclDestroyScalar(alpha);
    aclDestroyTensor(out);
     
    // 释放Device内存
    aclrtFree(selfDeviceAddr);
    aclrtFree(otherDeviceAddr);
    aclrtFree(outDeviceAddr);
    aclrtFree(workspaceAddr);
    
    // 销毁Stream
    aclrtDestroyStream(stream);
    ```

7. **资源去初始化。**

    ```cpp
    // 复位设备
    aclrtResetDeviceForce(deviceId);
    // 去初始化
    aclFinalize();
    ```
