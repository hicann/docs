# 模型卸载

模型执行结束后，需及时卸载模型，释放模型资源。

在模型推理结束后，还需要通过aclmdlUnload接口卸载模型，并销毁aclmdlDesc类型的模型描述信息、释放模型运行的工作内存和权值内存。

以下是关键步骤的代码示例，不能直接拷贝编译运行，仅供参考。调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

```cpp
// 1. 卸载模型
aclError ret = aclmdlUnload(modelId_);

// 2. 释放模型描述信息
if (modelDesc_ != nullptr) {
    (void)aclmdlDestroyDesc(modelDesc_);
    modelDesc_ = nullptr;
}

// 3. 释放模型运行的工作内存
if (modelWorkPtr_ != nullptr) {
    (void)aclrtFree(modelWorkPtr_);
    modelWorkPtr_ = nullptr;
    modelWorkSize_ = 0;
}

// 4. 释放模型运行的权值内存
if (modelWeightPtr_ != nullptr) {
    (void)aclrtFree(modelWeightPtr_);
    modelWeightPtr_ = nullptr;
    modelWeightSize_ = 0;
}
```
