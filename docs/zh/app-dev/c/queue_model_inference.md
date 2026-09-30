# 队列方式模型推理

本节介绍如何基于队列加载模型、准备模型输入数据、获取模型推理输出数据。

队列方式模型推理通过“队列”实现推理任务与数据生产/消费的解耦、异步调度，例如数据预处理和模型推理通过异步队列的方式实现异步并行。

## 基本原理

- 调用aclmdlLoadFromFileWithQ或aclmdlLoadFromMemWithQ接口以队列方式加载模型。
- 调用acltdtEnqueueData接口将模型的输入数据传入队列，由接口内部根据队列中的输入数据进行推理，无需调用模型执行的接口。
- 调用acltdtDequeueData接口等待模型推理执行完毕，再由用户从输出内存中获取结果数据。

>**说明：** 
>如果涉及多线程，当模型有多个输入时，多个输入数据的入队任务（即调用acltdtEnqueueData接口）必须在同一个线程中；当模型有多个输出时，多个输出数据的出队任务（即调用acltdtDequeueData接口）必须在同一个线程中。

## 示例代码

以下是队列方式模型推理关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

```cpp
#include "acl/acl.h"
......

// 获取当前AI软件栈的运行模式，根据不同的运行模式，后续的内存申请、内存复制等接口调用方式不同
extern bool g_isDevice;
aclrtRunMode runMode;
aclError ret = aclrtGetRunMode(&runMode);
g_isDevice = (runMode == ACL_DEVICE);

// 1. 加载并执行模型
// 此处的..表示相对路径，相对可执行文件所在的目录
// 例如，编译出来的可执行文件存放在out目录下，此处的..就表示out目录的上一级目录
const char* omModelPath = "../model/resnet50.om";

// 1.1 创建模型的输入队列，如果模型有多个输入，则创建多个输入队列，此处以一个输入为例
acltdtQueueAttr *attr = acltdtCreateQueueAttr();
uint32_t *inputQueueList = new (nothrow) uint32_t[num];
int32_t inputNum = 1;

for (int n = 0; n < inputNum; n++) {
        uint32_t inputQid;
        ret = acltdtCreateQueue(attr, &inputQid);
        inputQueueList[n] = inputQid;
    }

// 1.2 创建模型的输出队列，如果模型有多个输出，则创建多个输出队列，此处以一个输出为例
uint32_t *outputQueueList = new (nothrow) uint32_t[num];
int32_t outputNum = 1;

for (int n = 0; n < outputNum; n++) {
        uint32_t outputQid;
        ret = acltdtCreateQueue(attr, &outputQid);
        outputQueueList[n] = outputQid;
    }

// 1.3 加载模型
uint32_t modelId;
ret= aclmdlLoadFromFileWithQ(omModelPath, &modelId, 
                             inputQueueList, inputNum, outputQueueList, outputNum);

// 1.4 根据模型的ID，获取该模型的描述信息
aclmdlDesc *modelDesc = aclmdlCreateDesc();
ret = aclmdlGetDesc(modelDesc, modelId);

// 1.5 获取模型的输入内存大小，如果模型有多个输入，则需要获取每个输入的内存大小，此处以一个输入为例
size_t inputSize = aclmdlGetInputSizeByIndex(modelDesc, 0);

// 1.6 加载测试图片数据，进行推理，并对推理结果数据进行后处理
string testFile[] = {
        "../data/dog1_1024_683.bin",
        "../data/dog2_1024_683.bin"
};

for (size_t index = 0; index < sizeof(testFile) / sizeof(testFile[0]); ++index) {
        uint32_t devBufferSize;
        void *picDevBuffer = nullptr;
        // 自定义函数ReadBinFile，根据AI软件栈的运行模式，申请对应的内存，再调用C++标准库中的函数将图片数据读入内存
        ret = Utils::ReadBinFile(testFile[index], picDevBuffer, devBufferSize);

        // 将模型输入数据传入队列中，执行模型推理，-1是表示阻塞程序直到输入数据入队完成
        ret = acltdtEnqueueData(inputQid, picDevBuffer, devBufferSize, nullptr, 0, -1, 0);
        // 获取每个输出的大小
    size_t dataSize = aclmdlGetOutputSizeByIndex(modelDesc, 0);
    void *data = nullptr;
        size_t retDataSize = 0;
        // 为模型输出数据申请内存
    if (!g_isDevice) {
            aclError aclRet = aclrtMallocHost(&data, dataSize);
     } else {
        aclError aclRet = aclrtMalloc(&data, dataSize, ACL_MEM_MALLOC_HUGE_FIRST);
     }
         // 等待模型推理执行完毕，从输出内存中获取结果数据，-1是表示阻塞程序直到推理输出数据入队完成
         ret = acltdtDequeueData(outputQid, data, dataSize, &retDataSize, nullptr, 0, -1);
         //将输出内存中的数据转换为float类型
         float *outData = NULL;
         outData = reinterpret_cast<float*>(data);
        
         // 显示每张图片的top5置信度的类别编号
         map<float, int, greater<float> > resultMap;
         for (int j = 0; j < len / sizeof(float); ++j) {
            resultMap[*outData] = j;
            outData++;
         }
         int cnt = 0;
         for (auto it = resultMap.begin(); it != resultMap.end(); ++it) {
            // print top 5
            if (++cnt > 5) {
               break;
            }
            INFO_LOG("top %d: index[%d] value[%lf]", cnt, it->second, it->first);
         }
         if (!g_isDevice) {
            aclError aclRet = aclrtFreeHost(picDevBuffer);
            aclrtFreeHost(data);
     } else {
        aclError aclRet = aclrtFree(picDevBuffer);
            aclrtFree(data); 
     }
}

// 2. 卸载模型，并释放模型推理相关资源
aclmdlUnload(modelId);
aclmdlDestroyDesc(modelDesc);
acltdtDestroyQueue(inputQid);
acltdtDestroyQueue(outputQid);
acltdtDestroyQueueAttr(attr);

......
```
