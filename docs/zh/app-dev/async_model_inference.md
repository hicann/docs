# 异步模型推理

本节介绍异步推理接口如何与回调函数配合使用，每隔一段时间下发一次回调任务，获取前一段时间内的异步推理结果。

## 接口调用流程

开发应用时，如果涉及异步场景下的同步等待，则应用程序中必须包含相关的代码逻辑，关于该场景的接口调用流程，请参见下图。

**图 1**  同步等待流程Callback场景  
![](figures/同步等待流程Callback场景.png "同步等待流程Callback场景")

关键接口说明如下：

1. 回调函数需由用户提前创建，用于获取并处理模型推理或算子执行的结果。
2. 线程需由用户提前创建，并自定义线程函数，在线程函数内调用aclrtProcessReport接口，设置超时时间，等待aclrtLaunchCallback接口下发的回调任务执行。
3. 调用aclrtSubscribeReport接口：指定处理Stream上回调函数的线程，线程与第2步中创建的线程保持一致。
4. 异步推理时调用aclmdlExecuteAsync接口。

    对于异步接口，还需调用aclrtSynchronizeStream接口阻塞应用程序运行，直到指定Stream中的所有任务都完成。

    用户可以在aclrtSynchronizeStream接口之后一次性获取所有图片的异步推理结果，但如果图片数据量较大的情况下，需要等待的时间比较长，这时可以使用Callback功能，每隔一段时间下发一次Callback任务，获取前一段时间内的异步推理结果。

5. 调用aclrtLaunchCallback接口：在Stream的任务队列中下发一个回调任务，系统内部在执行到该回调任务时，会在Stream上注册的线程（通过aclrtSubscribeReport接口注册的线程）中执行回调函数，回调函数与第1步中的回调函数保持一致。

    每调用一次aclrtLaunchCallback接口，就会触发一次回调函数的执行。

6. 调用aclrtUnSubscribeReport接口：取消线程注册（Stream上的回调函数不再由指定线程处理）。

## 示例代码

以下是异步模型推理功能关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

您可以单击[resnet50\_async\_imagenet\_classification](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/1_classification/resnet50_async_imagenet_classification)获取样例。

```cpp
#include "acl/acl.h"
......

// 获取当前AI软件栈的运行模式，根据不同的运行模式，后续的内存申请、内存复制等接口调用方式不同
aclrtRunMode runMode;
extern bool g_isDevice;
aclrtGetRunMode(&runMode);
g_isDevice = (runMode == ACL_DEVICE);

// 1. 申请模型推理资源

// 此处的..表示相对路径，相对可执行文件所在的目录
// 例如，编译出来的可执行文件存放在out目录下，此处的..就表示out目录的上一级目录
const char* omModelPath = "../model/resnet50.om";

// 1.1 加载模型
// 根据模型文件获取模型执行时所需的权值内存大小、工作内存大小，并申请权值内存、工作内存
aclmdlQuerySize(omModelPath, &modelMemSize_, &modelWeightSize_);
aclrtMalloc(&modelMemPtr_, modelMemSize_, ACL_MEM_MALLOC_HUGE_FIRST);
aclrtMalloc(&modelWeightPtr_, modelWeightSize_, ACL_MEM_MALLOC_HUGE_FIRST);

// 加载离线模型文件，模型加载成功，返回标识模型的ID。
aclmdlLoadFromFileWithMem(modelPath, &modelId_, modelMemPtr_,
        modelMemSize_, modelWeightPtr_, modelWeightSize_);

// 1.2 根据模型的ID，获取该模型的描述信息
modelDesc_ = aclmdlCreateDesc();
aclmdlGetDesc(modelDesc_, modelId_);

// 1.3 自定义函数InitMemPool，初始化内存池，存放模型推理的输入数据、输出数据
// -----自定义函数InitMemPool内部的关键实现-----
string testFile[] = {
        "../data/dog1_1024_683.bin",
        "../data/dog2_1024_683.bin"
    };
size_t fileNum = sizeof(testFile) / sizeof(testFile[0]);
// g_memoryPoolSize表示内存池中的内存块的个数默认为100个
for (size_t i = 0; i < g_memoryPoolSize; ++i) {
        size_t index = i % (sizeof(testFile) / sizeof(testFile[0]));
        // model process
        uint32_t devBufferSize;
        // 自定义函数GetDeviceBufferOfFile，完成以下功能：
        // 获取存放输入图片数据的内存及内存大小、将图片数据传输到Device
        void *picDevBuffer = Utils::GetDeviceBufferOfFile(testFile[index], devBufferSize);
        aclmdlDataset *input = nullptr;
        // 自定义函数CreateInput，创建aclmdlDataset类型的数据input，用于存放模型推理的输入数据
        Result ret = CreateInput(picDevBuffer, devBufferSize, input);
        aclmdlDataset *output = nullptr;
        // 自定义函数CreateOutput，创建aclmdlDataset类型的数据output，用于存放模型推理的输出数据，modelDesc表示模型的描述信息
        CreateOutput(output, modelDesc);
        {
            std::lock_guard<std::recursive_mutex> lk(freePoolMutex_);
            freeMemoryPool_[input] = output;
        }
}
// -----自定义函数InitMemPool内部的关键实现-----

// 2 模型推理
// 2.1 创建线程tid，并将该tid线程指定为处理Stream上回调函数的线程
// 其中ProcessCallback为线程函数，在该函数内调用aclrtProcessReport接口，等待指定时间后，触发回调函数处理
pthread_t tid;
(void)pthread_create(&tid, nullptr, ProcessCallback, &s_isExit);

// 2.2 指定处理Stream上回调函数的线程
aclrtSubscribeReport(tid, stream_);

// 2.3 创建回调函数，用户处理模型推理的结果，由用户自行定义
void ModelProcess::CallBackFunc(void *arg)
{
    std::map<aclmdlDataset *, aclmdlDataset *> *dataMap =
        (std::map<aclmdlDataset *, aclmdlDataset *> *)arg;

    aclmdlDataset *input = nullptr;
    aclmdlDataset *output = nullptr;
    MemoryPool *memPool = MemoryPool::Instance();

    for (auto& data : *dataMap) {
        ModelProcess::OutputModelResult(data.second);
        memPool->FreeMemory(data.first, data.second);
    }

    delete dataMap;
}

// 2.4 自定义函数ExecuteAsync，执行模型推理
// -----自定义函数ExecuteAsync内部的关键实现开始-----
// g_callbackInterval表示callback间隔，默认为1，表示1次异步推理后，下发一次callback任务
bool isCallback = (g_callbackInterval != 0);
size_t callbackCnt = 0;
std::map<aclmdlDataset *, aclmdlDataset *> *dataMap = nullptr;
aclmdlDataset *input = nullptr;
aclmdlDataset *output = nullptr;
MemoryPool *memPool = MemoryPool::Instance();
// g_executeTimes表示执行模型异步推理的次数，默认为100次
for (uint32_t cnt = 0; cnt < g_executeTimes; ++cnt) {
    if (memPool->mallocMemory(input, output) != SUCCESS) {
        ERROR_LOG("get free memory failed");
        return FAILED;
    }
    // 执行异步推理
    aclError ret = aclmdlExecuteAsync(modelId_, input, output, stream_);

    if (isCallback) {
        if (dataMap == nullptr) {
            dataMap = new std::map<aclmdlDataset *, aclmdlDataset *>;
            if (dataMap == nullptr) {
                ERROR_LOG("malloc list failed, modelId is %u", modelId_);
                memPool->FreeMemory(input, output);
                return FAILED;
            }
        }
        (*dataMap)[input] = output;
        callbackCnt++;
        if ((callbackCnt % g_callbackInterval) == 0) {
            // 在Stream的任务队列中增加一个需要执行的回调函数
            ret = aclrtLaunchCallback(CallBackFunc, (void *)dataMap, ACL_CALLBACK_BLOCK, stream_);
            if (ret != ACL_SUCCESS) {
                ERROR_LOG("launch callback failed, index=%zu", callbackCnt);
                memPool->FreeMemory(input, output);
                delete dataMap;
                return FAILED;
            }
            dataMap = nullptr;
        }

    }
}
// -----自定义函数ExecuteAsync内部的关键实现结束-----

// 2.5 对于异步推理，需阻塞应用程序运行，直到指定Stream中的所有任务都完成
aclrtSynchronizeStream(stream_);

// 2.6 取消线程注册，Stream上的回调函数不再由指定线程处理 
aclrtUnSubscribeReport(static_cast<uint64_t>(tid), stream_);
s_isExit = true;
(void)pthread_join(tid, nullptr);

......
```
