# 随机数生成（Random）

除了下发Kernel执行任务外，Runtime还支持下发随机数生成的内置系统任务。系统任务区别于Kernel任务，无需用户提供执行代码。系统任务可以下发到某条Stream异步执行，同样遵循同一流上任务保序执行的规则。

通过aclrtRandomNumAsync执行随机数生成任务，调用代码示例如下：

```
aclError NormalFloatAsync(
    float mean, float stddev, uint64_t seed, uint64_t num, void *counterDevAddr, void *devOutput, aclrtStream stream)
{
    aclrtRandomNumTaskInfo taskInfo = {};
    taskInfo.dataType = ACL_FLOAT;
    taskInfo.randomNumFuncParaInfo.funcType = ACL_RT_RANDOM_NUM_FUNC_TYPE_NORMAL_DIS;
    taskInfo.randomParaAddr = NULL;
    taskInfo.randomCounterAddr = counterDevAddr;
    taskInfo.randomResultAddr = devOutput;
    memcpy(taskInfo.randomNumFuncParaInfo.paramInfo.normalDisInfo.mean.valueOrAddr, &mean, sizeof(float));
    taskInfo.randomNumFuncParaInfo.paramInfo.normalDisInfo.mean.size = sizeof(float);
    taskInfo.randomNumFuncParaInfo.paramInfo.normalDisInfo.mean.isAddr = 0;
    memcpy(taskInfo.randomNumFuncParaInfo.paramInfo.normalDisInfo.stddev.valueOrAddr, &stddev, sizeof(float));
    taskInfo.randomNumFuncParaInfo.paramInfo.normalDisInfo.stddev.size = sizeof(float);
    taskInfo.randomNumFuncParaInfo.paramInfo.normalDisInfo.stddev.isAddr = 0;
    memcpy(taskInfo.randomSeed.valueOrAddr, &seed, sizeof(uint64_t));
    taskInfo.randomSeed.size = sizeof(uint64_t);
    taskInfo.randomSeed.isAddr = 0;
    memcpy(taskInfo.randomNum.valueOrAddr, &num, sizeof(uint64_t));
    taskInfo.randomNum.size = sizeof(uint64_t);
    taskInfo.randomNum.isAddr = 0;
    return aclrtRandomNumAsync(&taskInfo, stream, NULL);
}
int main()
{
    aclError ret;
    // 初始化 ACL
    ret = aclInit(NULL);
    ret = aclrtSetDevice(0);
    aclrtStream stream;
    ret = aclrtCreateStream(&stream);
    uint64_t num = 128;
    size_t size = num * sizeof(uint64_t);  // 申请足够大内存
    // 申请 Device 内存
    void *devOutput = NULL;
    ret = aclrtMalloc(&devOutput, size, ACL_MEM_MALLOC_NORMAL_ONLY);
    // 准备 Host 数据
    void *hostOutput = malloc(size);
    // 申请存放随机数状态 counter 的device内存，要求 16Byte
    void *counterAddr = NULL;
    ret = aclrtMalloc((void **)&counterAddr, 16, ACL_MEM_MALLOC_NORMAL_ONLY);
    
    float mean = 3.0;
    float stddev = 2.0;    
    ret =NormalFloatAsync(mean, stddev, 0, num, counterAddr, devOutput, stream);
    // 同步 stream
    aclrtSynchronizeStream(stream);
    // 拷回结果
    aclrtMemcpy(hostOutput, size, devOutput, size, ACL_MEMCPY_DEVICE_TO_HOST);
    
    // 释放资源
    free(hostOutput);
    aclrtFree(devOutput);
    aclrtFree(counterAddr);
    aclrtDestroyStream(stream);
    aclrtResetDeviceForce(0);
    aclFinalize();
    return 0;
}
```
