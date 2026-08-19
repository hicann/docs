# EL0018 Resource\_Error\_Insufficient\_Host\_Memory

## 错误信息

报错格式如下，占位符%s的含义依次为内存大小、模块名称：

```text
Failed to allocate %s host memory requested by the %s module.
```

报错示例如下：

```text
Failed to allocate 1024 bytes host memory requested by DRV(hdc) module.
```

## 可能原因

由于Host内存不足导致内存分配失败。

## 解决方法

确保所需内存可用，采取措施（如停止不必要的进程）以释放内存。
