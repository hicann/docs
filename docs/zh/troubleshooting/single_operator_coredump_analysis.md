# 执行单算子产生coredump的定位处理

## 问题现象

单算子执行结束，出现重复释放内存，导致coredump，屏幕显示关键日志信息：

```bash
double free or corruption(!prev)
```

## 可能原因

分析屏显日志信息，可能存在以下故障原因：代码中出现重复释放内存的操作。

## 解决方法

1. gdb挂载可执行文件。
2. 执行gdb调试。
3. 查看调用栈。
4. 如果该问题非用户代码问题，您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。
