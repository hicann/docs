# 动态Shape输入（设置Shape范围）

本节介绍动态Shape输入场景下，如何设置Shape范围，介绍其关键接口、接口调用流程及示例代码。

## 接口调用流程

如果模型输入Shape是动态的，在模型执行之前调用aclmdlSetDatasetTensorDesc设置该输入的tensor描述信息（主要是设置Shape信息），在模型执行之后，调用aclmdlGetDatasetTensorDesc接口获取模型动态输出的Tensor描述信息，再进一步调用aclTensorDesc下的操作接口获取输出Tensor数据占用的内存大小、Tensor的Format信息、Tensor的维度信息等。

关键原理说明如下：

1. 构建模型。

    模型推理场景下，对于动态Shape的输入数据，使用ATC工具转换模型时，通过input\_shape参数设置输入Shape范围，详细参数说明请参见[《ATC离线模型编译工具》](https://hiascend.com/document/redirect/cannCommunityATC)中的“参数说明 \> 基础功能参数 \> 输入选项 \> --input\_shape”。

2. 加载模型。

    模型加载的详细流程，请参见[模型加载](model_load.md)，模型加载成功后，返回标识模型的ID。

3. 创建aclmdlDataset类型的数据，用于描述模型执行的输入、输出。

    详细调用流程请参见[准备模型执行的输入/输出数据结构](model_execute.md#section1620016465510)。

    注意点如下：

    - 当调用aclmdlGetInputSizeByIndex获取到的size大小为0时，表示该输入的Shape是动态的，用户可根据实际情况预估一块较大的输入内存。
    - 当调用aclmdlGetOutputSizeByIndex获取到的size大小为0时，表示该输出的Shape是动态的，用户可根据实际情况预估一块较大的输出内存，或者选择由系统内部自行申请对应index的输出内存。详细说明参见aclmdlGetOutputSizeByIndex接口。

4. 在成功加载模型之后，执行模型之前，调用aclmdlSetDatasetTensorDesc接口设置动态Shape输入的Tensor描述信息（主要是设置Shape信息）。

    在调用aclCreateTensorDesc接口，创建Tensor描述信息时，设置Shape信息，包括维度个数、维度大小，此处设置的维度个数、维度大小必须在模型构建时设置的输入Shape范围内，模型构建的详细说明请参见[模型编译](model_build.md)。
<a id="li187839613215"></a>
5. （可选）创建Allocator描述符、注册Allocator。

    **注意**：当前仅支持在动态Shape模型推理场景使用外置Allocator管理内存，注册Allocator的接口需配合aclmdlExecuteAsync接口一起使用，且需在aclmdlExecuteAsync接口之前调用本接口。

    1. 先调用aclrtAllocatorCreateDesc创建Allocator描述符；
    2. 再分别调用aclrtAllocatorSetObjToDesc、aclrtAllocatorSetAllocFuncToDesc、aclrtAllocatorSetGetAddrFromBlockFuncToDesc、aclrtAllocatorSetFreeFuncToDesc设置Allocator对象及回调函数；
    3. 然后调用aclrtAllocatorRegister注册Allocator，并将Allocator与Stream绑定，模型执行时需使用相同的Stream；
    4. 注册Allocator后，可调用aclrtAllocatorDestroyDesc接口销毁Allocator描述符。

6. 执行模型。
    - 支持同步推理场景，例如调用aclmdlExecute接口。
    - 也支持异步推理场景，例如调用aclmdlExecuteAsync接口，但异步场景下需调用流同步接口（例如aclrtSynchronizeStream）确认异步任务执行完成。

        异步推理场景下，当前仅aclmdlExecuteAsync接口支持使用用户注册的Allocator，即第[5](#li187839613215)步注册的Allocator。

7. 获取模型执行的结果数据。

    调用aclmdlGetDatasetTensorDesc接口获取动态Shape输出的Tensor描述信息，再利用aclTensorDesc数据类型的操作接口获取Tensor描述信息的属性，此处以获取size（表示Tensor数据占用的空间大小）为例，然后从内存中读取对应size的数据。

8. （可选）若在[5](#li187839613215)中注册Allocator，则此处需要取消注册、销毁已注册的Allocator。

    用户注册的Allocator和Stream绑定，如需主动释放、销毁Allocator，在释放Stream之前，应先调用aclrtAllocatorUnregister取消注册，然后释放流资源、销毁用户的Allocator。

## 同步推理场景示例代码

以下是模型推理关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

```cpp
......

// 此例中假设模型的第一个输入为动态输入，其index为0；模型的第一个输出为动态输出，其index为0。

// 1. 模型加载，加载成功后，再设置动态输入的Tensor描述信息，主要设置动态输入的Shape信息
......

// 2. 准备模型描述信息modelDesc_，准备模型的输入数据input_和模型的输出数据output_
// 此处需注意：
// 当利用aclmdlGetInputSizeByIndex获取到的size大小为0时，表示该输入的Shape是动态的，用户可根据实际情况预估一块较大的输入内存
// 当利用aclmdlGetOutputSizeByIndex获取到的size大小为0时，表示该输出的Shape是动态的，用户可根据实际情况预估一块较大的输出内存
// ......

// 3. 自定义函数，设置动态输入的Tensor描述信息
void SetTensorDesc()
{
        // ......
        // 创建Tensor描述信息
        // shape需要和给定的输入数据的shape一致
    int64_t shapes[4] = {1, 3, 224, 224};
    aclTensorDesc *inputDesc = aclCreateTensorDesc(ACL_FLOAT, 4, shapes, ACL_FORMAT_NCHW);
    // 设置index为0的动态输入的Tensor描述信息
    aclError ret = aclmdlSetDatasetTensorDesc(input_, inputDesc, 0);
        // ......
}
// 4. 自定义函数，执行模型，并获取动态输出的Tensor描述信息
void ModelExecute()
{
    aclError ret;
    // 调用自定义接口，设置动态输入的Tensor描述信息
    SetTensorDesc();
        // 执行模型
    ret = aclmdlExecute(modelId, input_, output_);
    // 获取index为0的动态输出的Tensor描述信息
        aclTensorDesc *outputDesc = aclmdlGetDatasetTensorDesc(output_, 0);
    // 利用aclTensorDesc数据类型的操作接口获取outputDesc的属性，此处需要获取size（表示Tensor数据占用的空间大小），然后从内存中读取对应size的数据
    string outputFileName = ss.str();
        FILE *outputFile = fopen(outputFileName.c_str(), "wb");
    size_t outputDesc_size = aclGetTensorDescSize(outputDesc);
        aclDataBuffer *dataBuffer = aclmdlGetDatasetBuffer(output_, 0);
        void *data = aclGetDataBufferAddr(dataBuffer);
    void *outHostData = nullptr;
        // 调用aclrtGetRunMode接口获取软件栈的运行模式，并根据运行模式判断是否进行数据传输
        aclrtRunMode runMode;
        ret = aclrtGetRunMode(&runMode);
        if (runMode == ACL_HOST) {
            ret = aclrtMallocHost(&outHostData, outputDesc_size);
       // 由于动态shape申请的内存比较大，而真实数据的大小是outputDesc_size，所以此处用真实数据大小去拷贝内存
        ret = aclrtMemcpy(outHostData, outputDesc_size, data, outputDesc_size, ACL_MEMCPY_DEVICE_TO_HOST);
        fwrite(outHostData, outputDesc_size, sizeof(char), outputFile);
            ret = aclrtFreeHost(outHostData);
    } else {
        // if app is running in host, write model output data into result file
                fwrite(data, outputDesc_size, sizeof(char), outputFile);
    }
    fclose(outputFile);
        // ......
}

// 5. 处理模型推理结果
......
```

## 异步推理场景示例代码

本节中的示例重点介绍模型推理的代码逻辑，示例场景为用户注册Allocator，并调用异步接口aclmdlExecuteAsync执行推理。

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。以下是关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。

```cpp
......

// 示例代码仅作为流程参考，实际应用场景请注意校验返回值
// 此例中假设模型的第一个输入为动态输入，其index为0；模型的第一个输出为动态输出，其index为0

// 1. 模型加载，加载成功后，再设置动态输入的Tensor描述信息，主要设置动态输入的Shape信息
......

// 2. 准备模型描述信息modelDesc_，准备模型的输入数据input_和模型的输出数据output_
// 此处需注意：
// 当利用aclmdlGetInputSizeByIndex获取到的size大小为0时，表示该输入的Shape是动态的，用户可根据实际情况预估一块较大的输入内存
// 当利用aclmdlGetOutputSizeByIndex获取到的size大小为0时，表示该输出的Shape是动态的，用户可根据实际情况预估一块较大的输出内存
// ......

// 3. 自定义函数，设置动态输入的Tensor描述信息
void SetTensorDesc()
{
        // ......
        // 创建Tensor描述信息
        // shape需要和给定的输入数据的shape一致
    int64_t shapes = {1, 3, 224, 224};
    aclTensorDesc *inputDesc = aclCreateTensorDesc(ACL_FLOAT, 4, shapes, ACL_FORMAT_NCHW);
    // 设置index为0的动态输入的Tensor描述信息
    aclError ret = aclmdlSetDatasetTensorDesc(input_, inputDesc, 0);
        // ......
}

// 4. 创建Allocator描述符、注册Allocator
// 假设allocator是用户想要注册的Allocator对象，
void RegisterCustomAllocator(aclrtAllocator allocator, aclrtStream stream) {
    // 6.1 创建 AllocatorDesc
    aclrtAllocatorDesc allocatorDesc = aclrtAllocatorCreateDesc();
    // 6.2 初始化AllocatorDesc，设置Allocator内存申请、释放相关的回调函数。CustomMallocFunc、CustomFreeFunc、CustomMallocAdviseFunc、CustomGetBlockAddrFunc是以“C”风格的方式定义的回调函数，会以函数指针的方式传入AllocatorDesc。
    aclrtAllocatorSetObjToDesc(allocatorDesc, allocator);
    aclrtAllocatorSetAllocFuncToDesc(allocatorDesc, CustomMallocFunc);
    aclrtAllocatorSetFreeFuncToDesc(allocatorDesc, CustomFreeFunc);
    aclrtAllocatorSetAllocAdviseFuncToDesc(allocatorDesc, CustomMallocAdviseFunc);
    aclrtAllocatorSetGetAddrFromBlockFuncToDesc(allocatorDesc, CustomGetBlockAddrFunc);
    // 注册Allocator并和Stream绑定，接口会根据AllocatorDesc创建Allocator
    aclrtAllocatorRegister(stream, allocatorDesc);
    // Allocator描述符使用完成后，可直接销毁
    aclrtAllocatorDestroyDesc(allocatorDesc);
}


// 5. 自定义函数，执行模型，并获取动态输出的Tensor描述信息
void ModelExecute(aclrtStream stream)
{
    aclError ret;
    // 调用自定义接口，设置动态输入的Tensor描述信息
    SetTensorDesc();
       // 执行模型，仅异步接口支持使用用户注册的Allocator，并且要求执行stream和注册Allocator所绑定的stream保持一致
    ret = aclmdlExecuteAsync(modelId, input_, output_, stream);
       // 调用异步接口成功仅表示任务下发成功，获取结果前需调用同步等待接口确保任务已执行完成
        aclrtSynchronizeStream(stream);
       // 获取index为0的动态输出的Tensor描述信息
        aclTensorDesc *outputDesc = aclmdlGetDatasetTensorDesc(output_, 0);
       // 利用aclTensorDesc数据类型的操作接口获取outputDesc的属性，此处需要获取size（表示Tensor数据占用的空间大小），然后从内存中读取对应size的数据
    string outputFileName = ss.str();
        FILE *outputFile = fopen(outputFileName.c_str(), "wb");
    size_t outputDesc_size = aclGetTensorDescSize(outputDesc);
        aclDataBuffer *dataBuffer = aclmdlGetDatasetBuffer(output_, 0);
        void *data = aclGetDataBufferAddr(dataBuffer);
    void *outHostData = nullptr;
       // 调用aclrtGetRunMode接口获取软件栈的运行模式，并根据运行模式判断是否进行数据传输
        aclrtRunMode runMode;
        ret = aclrtGetRunMode(&runMode);
        if (runMode == ACL_HOST) {
            ret = aclrtMallocHost(&outHostData, outputDesc_size);
           // 由于动态shape申请的内存比较大，而真实数据的大小是outputDesc_size，所以此处用真实数据大小去拷贝内存
        ret = aclrtMemcpy(outHostData, outputDesc_size, data, outputDesc_size, ACL_MEMCPY_DEVICE_TO_HOST);
        fwrite(outHostData, outputDesc_size, sizeof(char), outputFile);
            ret = aclrtFreeHost(outHostData);
        } else {
        // if app is running in host, write model output data into result file
                fwrite(data, outputDesc_size, sizeof(char), outputFile);
        }
    fclose(outputFile);
        // ......
}

// 6. 处理模型推理结果
......

// 7. 取消注册、销毁已注册的 Allocator
void UnregisterCustomAllocator(aclrtStream stream) {
     aclrtAllocatorUnregister(stream);
     // 由用户自行销毁自定义的Allocator
}

......
```
