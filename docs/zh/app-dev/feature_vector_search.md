# 特征向量检索（FV）

## 基本原理

该部分主要实现了对特征检索的功能验证，生成随机底库，随机生成特征数据进行特征检索（当前支持1:N、M:N两种检索模式，下文的示例代码以1：N为例）。大致可分为初始化、添加特征到底库、底库搜索、精准修改或删除底库特征、去初始化几个主要步骤，具体接口调用方式如下：

- **初始化**：调用aclInit接口进行初始化，调用aclfvCreateInitPara接口创建aclfvInitPara类型的数据来指定特征向量检索的初始化参数。
- **添加特征到底库**：主要调用aclfvCreateFeatureInfo接口创建aclfvFeatureInfo类型数据来表示创建特征的描述信息，然后调用aclfvRepoAdd添加底库。
- **底库搜索**：调用aclfvSearch接口来实现检索。
- **精准修改或删除底库特征**：调用aclfvDel和aclfvModify接口来实现删除或修改底库中某个特征。下文的代码以删除底库特征为例。
- **去初始化**：主要包括释放运行时资源、调用aclfvDestroyInitPara接口销毁aclfvInitPara类型的数据、调用aclfvRelease接口特征检索模块去初始化，释放内存空间。

## 示例代码

本节中的示例重点介绍特征向量检索的代码逻辑，不能直接拷贝编译运行，仅供参考。完整样例代码可单击[Link](https://gitee.com/ascend/samples/tree/master/cplusplus/level1_single_api/9_feature_retrieval/feature_retrieval)查看。

调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

```cpp
// 设置默认的运行模式为HOST
aclrtRunMode runMode = ACL_HOST;

// 1.初始化
// 1.1 初始化特征检索模块，此处以底库特征数100000为例
size_t fsNum = 100000;
fvInitPara = aclfvCreateInitPara(fsNum);

// 1.2 指定特征向量检索的初始化参数
ret = aclfvInit(fvInitPara);

// 2.添加底库和特征向量
// 2.1 增加第一个特征，创建特征描述信息时，偏移量offset参数值为0
uint32_t offset = 0;
uint32_t featureCount = 1000;
uint32_t featureLen = 36;

// 此处的自定义函数BaseShortFeaAlloc用于生成特征随机数据，由用户自行实现
void *featureData = BaseShortFeaAlloc(1000, static_cast<size_t>(featureCount), 0);
std::shared_ptr<void> feaBufPtr(featureData, [](void *p){(void)aclrtFreeHost(p);});
void *inputData = featureData;
std::shared_ptr<void> inputDataPtr = nullptr;

// 如果运行模式为ACL_HOST，则需要申请内存，再通过aclrtMemcpy接口将Host的随机特征数据传输到Device；否则直接将随机特征数据读入Device内存
if (aclrtGetRunMode(&runMode) == ACL_HOST) {
      // 为inputData申请内存
      ret = aclrtMalloc(&inputData, featureLen * featureCount, 
                        ACL_MEM_MALLOC_HUGE_FIRST);
      // 将随机特征数据读入到Device内存中
      inputDataPtr.reset(inputData, [](void *p) {(void)aclrtFree(p);});
      // 将featureData从Host侧拷贝到Device侧      
      ret = aclrtMemcpy(inputData,
                        featureLen * featureCount,
                        featureData,
                        featureLen * featureCount,
                        ACL_MEMCPY_HOST_TO_DEVICE);
}

// 创建特征描述信息，inputData表示前一步的特征随机数据
auto featureInfo = aclfvCreateFeatureInfo(id0, id1, offset, featureLen, featureCount, 
                        reinterpret_cast<uint8_t *>(inputData), featureLen * featureCount);

// 添加底库并向底库中添加特征，featureInfo表示前一步的特征描述信息
aclError ret = aclfvRepoAdd(SEARCH_1_N, featureInfo);

// 销毁aclfvFeatureInfo特征描述信息
aclfvDestroyFeatureInfo(featureInfo);

// 2.2增加第二个特征，创建特征描述信息时，偏移值offset需要与库中已添加特征个数一致，并精确删除或修改底库中的某个特征
offset += featureCount;

// 增加特征到底库的步骤，参考4.1中的代码
// ....

uint8_t featureData[36];
for (size_t i = 0; i < 36; i++) {
        featureData[i] = static_cast<uint8_t>(i);
}

// 创建内存并传输特征数据
void *inputData = nullptr;
aclrtMalloc(&inputData, 36, ACL_MEM_MALLOC_HUGE_FIRST);
std::shared_ptr<void> inputDataPtr(inputData, [](void *p){(void)aclrtFree(p);});
aclrtMemcpyKind kind = ACL_MEMCPY_DEVICE_TO_DEVICE;

// 如果运行模式是ACL_HOST,将特征数据拷贝到Device侧，否则无需拷贝，其中dataLen为featureData指针申请的内存长度
if (aclrtGetRunMode(&runMode) == ACL_HOST) {
        kind = ACL_MEMCPY_HOST_TO_DEVICE;
}
aclrtMemcpy(inputData, 36, featureData, dataLen, kind);

// 创建特征描述信息
uint32_t id0 = 0;
uint32_t id1 = 0;
auto featureInfo1 = aclfvCreateFeatureInfo(id0, id1, offset, 36, 1,
                                          reinterpret_cast<uint8_t *>(inputData), 36);
std::shared_ptr<aclfvFeatureInfo> featureInfoPtr(featureInfo1,
                                          [](aclfvFeatureInfo *p){(void)aclfvDestroyFeatureInfo(p);});

// 删除1个特征
aclfvDel(featureInfo1);

// 2.3 增加特征到其它底库,其中一级底库为1，二级底库为1
id0 = 1;
id1 = 1;
offset = 0; 

// 增加特征到底库步骤，参考2.1中的代码
// ....

// 3 底库检索（以1：N检索为例），主要包括特征检索预处理，特征1:N检索，特征检索结果处理三个部分
// 3.1 特征检索预处理，对于1:N来说, queryCnt必须为1
uint32_t queryCnt = 1;
uint32_t topK = 5;
uint32_t dataLen = queryCnt * topK * sizeof(uint32_t);
uint32_t resultNumDataLen = queryCnt * sizeof(uint32_t);
const uint32_t tableLen = 32 * 1024; 
uint32_t tableDataLen = queryCnt * tableLen;

// 生成数据表，用户通过数据表进行检索比对，此处的自定义函数AdcTabInit用于初始化特征检索输入Adc表，由用户自行实现
uint8_t *tableDataTmp = (uint8_t *)AdcTabInit(1000, queryCnt * 1024);
std::shared_ptr<void> tableDataTmpPtr(tableDataTmp,[](void *p){(void)aclrtFreeHost(p);});

// 为数据表分配内存，tableDataDev用于创建检索输入表信息
void *devPtr = nullptr;
aclrtMalloc(&devPtr, tableDataLen, ACL_MEM_MALLOC_HUGE_FIRST);
tableDataDev.reset(devPtr, [](void *p) {(void)aclrtFree(p);});

// 拷贝表数据到Device侧
uint8_t *devPtrTmp = reinterpret_cast<uint8_t *>(devPtr);
for (uint32_t i = 0; i < queryCnt; ++i) {
     for (uint32_t j = 0; j < 32; ++j) {
          uint8_t *dst = devPtrTmp + i * 32 * 1024 + j * 1024;
          uint8_t *src = tableDataTmp + i * 1024;
          aclrtMemcpy(dst, 1024, src, 1024, ACL_MEMCPY_HOST_TO_DEVICE);
     }
}

// 为检索结果resultNumDev,id0Dev,id1Dev,resultOffsetDev,resultDistanceDev分配内存
aclrtMalloc(&devPtr, resultNumDataLen, ACL_MEM_MALLOC_HUGE_FIRST);
resultNumDev.reset(devPtr, [](void *p) {(void)aclrtFree(p);});
aclrtMalloc(&devPtr, dataLen, ACL_MEM_MALLOC_HUGE_FIRST);
id0Dev.reset(devPtr, [](void *p) {(void)aclrtFree(p);});
aclrtMalloc(&devPtr, dataLen, ACL_MEM_MALLOC_HUGE_FIRST);
id1Dev.reset(devPtr, [](void *p) {(void)aclrtFree(p);});
aclrtMalloc(&devPtr, dataLen, ACL_MEM_MALLOC_HUGE_FIRST);              
resultOffsetDev.reset(devPtr, [](void *p) {(void)aclrtFree(p);});
aclrtMalloc(&devPtr, dataLen, ACL_MEM_MALLOC_HUGE_FIRST);
resultDistanceDev.reset(devPtr, [](void *p) {(void)aclrtFree(p);}); 
 
// 创建检索输入表信息，结果用于创建检索任务输入信息
aclfvQueryTable *searchQueryTable = aclfvCreateQueryTable(queryCnt, tableLen, reinterpret_cast<uint8_t *>
                                   (tableDataDev.get()), tableDataLen);
searchQueryTable.reset(searchQueryTable, [](aclfvQueryTable *p){(void)aclfvDestroyQueryTable(p);});

// 创建特征库范围参数，结果用于创建检索任务输入信息
aclfvRepoRange *searchRange = aclfvCreateRepoRange(0, 1023, 0, 1023); 
searchRange.reset(searchRange, [](aclfvRepoRange *p){(void)aclfvDestroyRepoRange(p);});

// 创建检索任务输入信息，结果用于特征1:N检索
aclfvSearchInput *searchInput = aclfvCreateSearchInput(searchQueryTable, searchRange, topK);
searchInput.reset(searchInput, [](aclfvSearchInput *p){(void)aclfvDestroySearchInput(p);});

// 创建检索结果信息，结果用于特征1:N检索
aclfvSearchResult *searchResult = aclfvCreateSearchResult(queryCnt,
                                   reinterpret_cast<uint32_t *>(resultNumDev.get()),
                                   resultNumDataLen,
                                   reinterpret_cast<uint32_t *>(id0Dev.get()),
                                   reinterpret_cast<uint32_t *>(id1Dev.get()),
                                   reinterpret_cast<uint32_t *>(resultOffsetDev.get()),
                                   reinterpret_cast<float *>(resultDistanceDev.get()),
                                   dataLen);
searchResult.reset(searchResult, [](aclfvSearchResult *p){(void)aclfvDestroySearchResult(p);});

// 3.2 特征1:N检索
aclfvSearch(SEARCH_1_N, searchInput.get(), searchResult.get());

// 3.3 特征检索结果处理
// 获取检索结果
uint32_t dataLen = queryCnt * topK * sizeof(uint32_t);
uint32_t *id0 = (uint32_t *)id0Dev.get();
uint32_t *id1 = (uint32_t *)id1Dev.get();
uint32_t *resultOffset= (uint32_t *)resultOffsetDev.get();
float *resultDistance = (float *)resultDistanceDev.get();

// 如果运行模式为ACL_HOST，则需要通过aclrtMemcpy接口将Device的检索结果回传到Host侧；否则无需回传
if (aclrtGetRunMode(&runMode) == ACL_HOST) {
        // 从Device侧拷贝数据到Host侧
        id0 = (uint32_t *)malloc(dataLen);
        id0Ptr.reset(id0);
        id1 = (uint32_t *)malloc(dataLen);
        id1Ptr.reset(id1);
        resultOffset = (uint32_t *)malloc(dataLen);
        resultOffsetPtr.reset(resultOffset);
        resultDistance = (float *)malloc(dataLen);
        resultDistancePtr.reset(resultDistance);
        aclrtMemcpy(id0, dataLen, id0Dev.get(), dataLen, ACL_MEMCPY_DEVICE_TO_HOST);
        aclrtMemcpy(id1, dataLen, id0Dev.get(), dataLen, ACL_MEMCPY_DEVICE_TO_HOST);
        aclrtMemcpy(resultOffset, dataLen, resultOffsetDev.get(), dataLen, ACL_MEMCPY_DEVICE_TO_HOST);
        aclrtMemcpy(resultDistance, dataLen, resultDistanceDev.get(), dataLen, ACL_MEMCPY_DEVICE_TO_HOST);
}

// 展示底库中的数据
for (uint32_t i = 0; i < queryCnt; i++) {
     for (uint32_t j = 0; j < topK; ++j) {
          uint32_t i0 = id0[i * topK + j];
          uint32_t i1 = id1[i * topK + j];
          uint32_t offset = resultOffset[i * topK + j];
          float distance = resultDistance[i * topK + j];
    }
}

// 4. 删除底库和数据
// 创建特征库范围并删除指定范围内的底库
uint32_t id0Min = 0;
uint32_t id0Max = 1023;
uint32_t id1Min = 0;
uint32_t id1Max = 1023;
aclfvRepoRange *repoRange = aclfvCreateRepoRange(id0Min, id0Max, id1Min, id1Max);
aclfvRepoDel(SEARCH_1_N, repoRange);
// 销毁aclfvInitPara类型的数据
aclfvDestroyInitPara(fvInitPara);

......
```
