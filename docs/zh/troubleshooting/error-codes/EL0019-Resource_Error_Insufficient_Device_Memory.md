# EL0019 Resource\_Error\_Insufficient\_Device\_Memory

## 错误信息

报错格式如下，占位符%s的含义依次为内存大小、模块名称：

```text
Failed to allocate %s device memory requested by the %s module.
```

报错示例如下：

```text
Failed to allocate 1024 bytes host memory requested by hdc module.
```

## 可能原因

由于Device内存不足导致内存分配失败。

## 解决方法

停止不必要的进程，并确保所需内存可用。
