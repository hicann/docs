# 模型执行

本节描述的是**整网模型执行**的接口调用流程。本节结合接口调用流程、示例代码介绍模型执行前需要准备哪些数据、模型执行接口以及模型执行之后需要释放哪些资源。

## 基本原理

**在模型加载之后，模型执行之前**，需要准备输入、输出数据结构，将输入数据传输到模型输入数据结构的对应内存中。

**模型执行结束后**，若无需使用输入数据、aclmdlDesc类型、aclmdlDataset类型、aclDataBuffer类型等相关资源，需及时释放内存、销毁对应的数据类型，防止内存异常。模型可能存在多个输入、多个输出，每个输入/输出的内存地址、内存大小用aclDataBuffer类型的数据来描述，针对每个输入/输出，需调用aclrtFree接口释放内存中的数据，再调用aclDestroyDataBuffer接口销毁相应的aclDataBuffer类型。

## 模型执行流程

**图 1**  基本的模型推理流程  
![](figures/basic_model_inference_process.png "基本的模型推理流程")

关键接口的说明如下：

1. 调用aclmdlCreateDesc接口**创建描述模型基本信息**的数据类型。
2. 调用aclmdlGetDesc接口根据[模型加载](model_load.md)中返回的模型ID**获取模型基本信息**。
3. **准备模型执行的输入、输出数据结构**，具体流程，请参见[准备模型执行的输入/输出数据结构](#section1620016465510)。

    <!-- npu="950,A3,910b,910,310p,310b" id1 -->
    如果模型的输入涉及动态Batch、动态分辨率、动态AIPP、动态维度（ND格式）等特性，请参见[模型动态Shape输入推理](static_shape_model_inference.md)、[模型动态AIPP推理](dynamic_AIPP_inference.md)。
    <!-- end id1 -->

4. **执行模型推理**。

    对于固定的多Batch场景，需要满足batch size后，才能将输入数据发送给模型进行推理。不满足batch size时，用户需根据自己的实际场景处理。

    当前系统支持模型的同步推理和异步推理：

    - 同步推理

        <!-- npu="950,A3,910b,910,310p,310b" id2 -->
        调用aclmdlExecute接口执行同步推理。
        <!-- end id2 -->

        <!-- npu="IPV350" id3 -->
        调用aclmdlExecuteV2接口执行同步推理。
        <!-- end id3 -->

    - 异步推理

        <!-- npu="950,A3,910b,910,310p,310b" id4 -->
        调用aclmdlExecuteAsync接口执行异步推理。
        <!-- end id4 -->

        <!-- npu="IPV350" id5 -->
        调用aclmdlExecuteAsyncV2接口执行异步推理。
        <!-- end id5 -->

        但对于异步接口，还需调用aclrtSynchronizeStream接口阻塞应用程序运行，直到指定Stream中的所有任务都完成。

        <!-- npu="950,A3,910b,910,310p,310b" id6 -->
        异步推理的详细介绍，请参见[异步模型推理](async_model_inference.md)。
        <!-- end id6 -->

5. **获取模型推理的结果**，用于后续处理。
    - 对于同步推理，直接获取模型推理的输出数据即可。
    - 对于异步推理，在实现Callback功能时，在回调函数内获取模型推理的结果，供后续使用。

6. **释放内存**。

    调用aclrtFree接口释放Device上的内存。

7. **释放相关数据类型的数据**。

    在模型推理结束后，需依次调用aclDestroyDataBuffer接口、aclmdlDestroyDataset接口及时释放描述模型输入、输出数据类型的数据。如果存在多个输入、输出，需调用多次aclDestroyDataBuffer接口。

<a id="section1620016465510"></a>

## 准备模型执行的输入/输出数据结构

以下数据类型用来描述模型、描述其输入输出以及存放数据的内存，在模型执行前，需要构造好这些数据类型，作为模型执行的输入：

- 使用**aclmdlDesc**类型的数据描述模型基本信息（例如输入/输出的个数、名称、数据类型、Format、维度信息等）。

    模型加载成功后，用户可根据模型的ID，调用aclmdlGetDesc接口获取该模型的描述信息，进而从模型的描述信息中获取模型输入/输出的个数、内存大小、维度信息、Format、数据类型等信息，可参见aclmdlDesc类型下的操作接口。

- 使用**aclmdlDataset**类型的数据描述模型的输入/输出数据，模型可能存在多个输入、多个输出。

    调用aclmdlDataset类型下的操作接口添加aclDataBuffer类型的数据、获取aclDataBuffer的个数等。

- 每个输入/输出的内存地址、内存大小用**aclDataBuffer**类型的数据来描述。

    调用aclDataBuffer类型下的操作接口获取内存地址、内存大小等。

    **图 2**  aclmdlDataset类型与aclDataBuffer类型的关系  
    ![](figures/relationship_between_aclmdlDataset_and_aclDataBuffer.png "aclmdlDataset类型与aclDataBuffer类型的关系")

了解相关的数据类型后，可以使用这些数据类型的操作接口准备模型的输入、输出数据结构，如下图所示。

**图 3**  模型执行的输入/输出数据结构的准备流程  
![](figures/prepare_model_input_output.png "模型执行的输入-输出数据结构的准备流程")

关键说明如下：

- 模型存在多个输入、输出时，用户可调用aclmdlGetNumInputs、aclmdlGetNumOutputs接口获取输入、输出的个数。
- 模型每个输入、输出所需的内存大小，用户可调用aclmdlGetInputSizeByIndex、aclmdlGetOutputSizeByIndex接口获取。
- 模型存在多个输入、输出时，用户在向aclmdlDataset中添加aclDataBuffer时，为避免顺序出错，可以先调用aclmdlGetInputNameByIndex、aclmdlGetOutputNameByIndex接口获取输入、输出的名称，根据输入、输出名称所对应的index的顺序添加。

## 示例代码

此处的示例代码是处理图片分类模型的输出结果，屏显每张图片的top5置信度的类别编号。用户可根据实际需求，自行实现模型推理输出数据的处理逻辑。

以下是关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

<!-- npu="950,A3,910b,910,310p,310b" id7 -->
您可以单击[resnet50\_imagenet\_classification](https://gitcode.com/cann/ge/tree/master/examples/acl/1_sample_resnet50_imagenet_classification)获取样例。
<!-- end id7 -->

```cpp
// 1. 根据模型的ID，获取该模型的描述信息。
// modelDesc_为aclmdlDesc类型。
modelDesc_ = aclmdlCreateDesc();
aclError ret = aclmdlGetDesc(modelDesc_, modelId_);

// 2. 准备模型推理的输入数据结构
// (1)申请输入内存
size_t modelInputSize;
void *modelInputBuffer = nullptr;
// 当前示例代码中的模型只有一个输入，所以index为0，如果模型有多个输入，则需要先调用aclmdlGetNumInputs接口获取模型输入的数量
modelInputSize = aclmdlGetInputSizeByIndex(modelDesc_, 0);
ret = aclrtMalloc(&modelInputBuffer, modelInputSize, ACL_MEM_MALLOC_HUGE_FIRST);

// (2)准备模型的输入数据结构
// 创建aclmdlDataset类型的数据，描述模型推理的输入，input_为aclmdlDataset类型
input_ = aclmdlCreateDataset();
aclDataBuffer *inputData = aclCreateDataBuffer(modelInputBuffer, modelInputSize);
ret = aclmdlAddDatasetBuffer(input_, inputData);

// 3. 准备模型推理的输出数据结构
// (1)创建aclmdlDataset类型的数据，描述模型推理的输出，output_为aclmdlDataset类型
output_ = aclmdlCreateDataset();

// (2)获取模型的输出个数.
size_t outputSize = aclmdlGetNumOutputs(modelDesc_);

// (3)循环为每个输出申请内存，并将每个输出添加到aclmdlDataset类型的数据中.
for (size_t i = 0; i < outputSize; ++i) {
    size_t buffer_size = aclmdlGetOutputSizeByIndex(modelDesc_, i);
    void *outputBuffer = nullptr;
    ret = aclrtMalloc(&outputBuffer, buffer_size, ACL_MEM_MALLOC_HUGE_FIRST);
    aclDataBuffer* outputData = aclCreateDataBuffer(outputBuffer, buffer_size);   
    ret = aclmdlAddDatasetBuffer(output_, outputData);
    }

// 4. 模型执行
string testFile[] = {
        "../data/dog1_1024_683.bin",
        "../data/dog2_1024_683.bin"
    };

for (size_t index = 0; index < sizeof(testFile) / sizeof(testFile[0]); ++index) {
    // 4.1 自定义函数ReadBinFile，调用C++标准库std::ifstream中的函数读取图片文件，输出图片文件占用的内存大小inputBuffSize以及图片文件存放在内存中的地址inputBuff
    void *inputBuff = nullptr;
    uint32_t inputBuffSize = 0;
    auto ret1 = Utils::ReadBinFile(fileName, inputBuff, inputBuffSize);
    
    // 4.2 准备模型推理的输入数据
    // 在申请运行时资源时调用aclrtGetRunMode接口获取软件栈的运行模式
    // 如果运行模式为ACL_DEVICE，则g_isDevice参数值为true，表示软件栈运行在Device侧，无需传输图片数据或在Device内传输数据 ；否则，需要调用内存复制接口将数据传输到Device
    if (!g_isDevice) {
        // if app is running in host, need copy data from host to device
        // modelInputBuffer、modelInputSize分别表示模型推理输入数据的内存地址、内存大小，在输入/输出数据结构准备时申请该内存
        ret = aclrtMemcpy(modelInputBuffer, modelInputSize, inputBuff, inputBuffSize, ACL_MEMCPY_HOST_TO_DEVICE);
        (void)aclrtFreeHost(inputBuff);
    } else { // app is running in device
        ret = aclrtMemcpy(modelInputBuffer, modelInputSize, inputBuff, inputBuffSize, ACL_MEMCPY_DEVICE_TO_DEVICE);
        (void)aclrtFree(inputBuff);
    }

    // 4.3 执行模型推理
    // modelId_表示模型ID，在模型加载成功后，会返回标识模型的ID
    // input_、output_分别表示模型推理的输入、输出数据，在准备模型推理的输入、输出数据结构时已定义
    ret = aclmdlExecute(modelId_, input_, output_);
        

    // 处理模型推理的输出数据，输出top5置信度的类别编号 
    // output_表示模型执行的输出
    for (size_t i = 0; i < aclmdlGetDatasetNumBuffers(output_); ++i) {
    // 获取每个输出的内存地址和内存大小
        aclDataBuffer* dataBuffer = aclmdlGetDatasetBuffer(output_, i);
        void* data = aclGetDataBufferAddr(dataBuffer);

        size_t len = aclGetDataBufferSizeV2(dataBuffer);

        // 将内存中的数据转换为float类型
        float *outData = NULL;
        outData = reinterpret_cast<float*>(data);
        
        // 屏显每张图片的top5置信度的类别编号
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
    }
}

// 5. 释放模型推理的输入、输出资源
// 释放输入资源，包括数据结构和内存
for (size_t i = 0; i < aclmdlGetDatasetNumBuffers(input_); ++i) {
        aclDataBuffer *dataBuffer = aclmdlGetDatasetBuffer(input_, i);
        (void)aclDestroyDataBuffer(dataBuffer);
}
(void)aclmdlDestroyDataset(input_);
input_ = nullptr;
aclrtFree(modelInputBuffer);

// 释放输出资源，包括数据结构和内存
for (size_t i = 0; i < aclmdlGetDatasetNumBuffers(output_); ++i) {
    aclDataBuffer* dataBuffer = aclmdlGetDatasetBuffer(output_, i);
    void* data = aclGetDataBufferAddr(dataBuffer);
    (void)aclrtFree(data);
    (void)aclDestroyDataBuffer(dataBuffer);
}

(void)aclmdlDestroyDataset(output_);
output_ = nullptr;
```

在构建模型时，若batchSize≥2（通过ATC工具的input\_shape参数设置），在推理前，需要编写一段代码，实现逻辑为：等输入数据满足batchSize（例如：batchSize=8）的要求，申请Device上的内存存放batchSize=8的数据，作为模型推理的输入。如果最后循环遍历所有的输入数据后，仍不满足batchSize的要求，则直接将剩余数据作为模型推理的输入。

此处的示例代码以batchSize=8为例：

```cpp
uint32_t batchSize = 8;
uint32_t deviceNum = 1;
uint32_t deviceId = 0;

// 获取模型第一个输入的大小
uint32_t modelInputSize = aclmdlGetInputSizeByIndex(modelDesc, 0);
// 获取每个Batch输入数据的大小
uint32_t singleBuffSize = modelInputSize / batchSize;

// 定义该变量，用于累加batch size是否达到8 Batch
uint32_t cnt = 0;
// 定义该变量，用于描述每个文件读入内存时的位置偏移
uint32_t pos = 0;

void* p_batchDst = NULL;
std::vector<std::string>inferFile_vec;

for (int i = 0; i < files.size(); ++i) 
        {
            // 每8个文件，申请一次Device上的内存，存放8 Batch的输入数据 
            if (cnt % batchSize == 0)
            {
                pos = 0;
                inferFile_vec.clear();
                // 申请Device上的内存
                aclrtMalloc(&p_batchDst, modelInputSize, ACL_MEM_MALLOC_HUGE_FIRST);
            }

            // TODO: 从某个目录下读入文件，计算文件大小fileSize
            
            // 根据文件大小，申请内存，存放文件数据
            aclrtMallocHost(&p_imgBuf, fileSize);

            // 将数据传输到Device的内存
            aclrtMemcpy((uint8_t *)p_batchDst + pos, fileSize, p_imgBuf, fileSize, ACL_MEMCPY_HOST_TO_DEVICE);
            pos += fileSize;
            // 及时释放不使用的内存
            aclrtFreeHost(p_imgBuf);

            // 将第i个文件存入vector中，同时cnt+1
            inferFile_vec.push_back(files[i]);
            cnt++;

            // 每8 Batch的输入数据送给模型进行推理
            if (cnt % batchSize == 0)
            {
                // TODO: 创建aclmdlDataset、aclDataBuffer类型的数据，用于描述模型的输入、输出数据
                // TODO: 调用aclmdlExecute接口执行模型推理
                // TODO: 推理结束后，调用aclrtFree接口释放Device上的内存
            }
        }

// 如果最后循环遍历所有的输入数据后，仍不满足多Batch的要求，则直接将剩余数据作为模型推理的输入。
if (cnt % batchSize != 0)
    {
            // TODO: 创建aclmdlDataset、aclDataBuffer类型的数据，用于描述模型的输入、输出数据
            // TODO: 调用aclmdlExecute接口执行模型推理
            // TODO: 推理结束后，调用aclrtFree接口释放Device上的内存
    }
```
