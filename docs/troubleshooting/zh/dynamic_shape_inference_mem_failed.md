# 动态shape推理申请内存失败

## 问题现象描述

模型推理过程中，申请了大小为0的内存，日志报错信息中包含以下关键信息：

```bash
[INFO] ASCENDCL ****** start to execute aclrtMalloc, size = 0
[ERROR] ASCENDCL ****** malloc size must be greater than zero
```

## 可能原因

模型为动态shape模型，模型的输出shape中含有-1，所以直接调用aclmdlGetOutputSizeByIndex接口取到的size为0。

然后申请了大小为0的内存，导致失败。

## 处理步骤

在aclmdlGetOutputSizeByIndex取到size为0时，用户需要预估一块较大的内存。
