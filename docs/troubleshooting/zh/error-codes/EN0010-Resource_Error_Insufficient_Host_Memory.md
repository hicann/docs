# EN0010 Resource\_Error\_Insufficient\_Host\_Memory

## 错误信息

报错格式如下，占位符%s表示内存大小：

```text
Failed to allocate %s host memory for DVPP.
```

报错示例如下：

```text
Failed to allocate 128 bytes host memory for DVPP.
```

## 可能原因

Host内存不足。

## 解决方法

确保所需内存可用，采取措施（如停止不必要的进程）以释放内存。
