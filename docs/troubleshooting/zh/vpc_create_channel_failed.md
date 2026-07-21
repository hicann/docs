# VPC创建通道失败

## 问题现象描述

调用hi\_mpi\_vpc\_create\_chn创建通道返回错误码HI\_ERR\_VPC\_EXIST，查看日志有如下类似错误信息，不同版本的报错日志可能存在差别：

```bash
device 0, chn 0 has already been created!
```

或

```bash
dev 0 chnl 0 is busy
```

## 可能原因

对于VPC模块，调用hi\_mpi\_vpc\_create\_chn指定通道号，创建通道，任何情况下通道号不能重复。原因是该通道已存在了。

## 定位思路

检查代码，查看通道号的使用。

## 解决方法

1、规划通道号，hi\_mpi\_vpc\_create\_chn创建时传入未被使用的通道号。

2、或者使用hi\_mpi\_vpc\_sys\_create\_chn，调用完成后系统会分配一个未被使用过的通道号。
