# VPC获取结果失败

## 问题现象描述

调用hi\_mpi\_vpc\_get\_process\_result，返回HI\_ERR\_VPC\_ILLEGAL\_PARAM，查看日志信息，不同版本的报错日志可能存在差别：

```bash
this channel doesn't have taskID 8845!, Channel id 0
```

或

```bash
taskId:8845 does not exist
```

## 可能原因

调用hi\_mpi\_vpc\_get\_process\_result传入一个非法的task id。

## 解决方法

调用hi\_mpi\_vpc\_get\_process\_result传入的task id，必须是功能接口中传出的。

将功能接口中传出的task id传入hi\_mpi\_vpc\_get\_process\_result。
