# EN0011 Resource\_Error\_Insufficient\_Host\_Memory

## 错误信息

报错格式如下：

```text
Failed to allocate host memory by std::make_shared.
```

## 可能原因

Host内存不足。

## 解决方法

确保所需内存可用，采取措施（如停止不必要的进程）以释放内存。
