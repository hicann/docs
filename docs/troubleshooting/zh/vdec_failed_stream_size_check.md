# 码流大小校验失败导致VDEC视频解码失败

## 问题现象描述

调用hi\_mpi\_vdec\_send\_stream接口返回错误码HI\_ERR\_VDEC\_ILLEGAL\_PARAM，查看应用类日志，有报错“**stream len can't be zero!**”，日志示例如下：

```bash
[Vdec]:vdec_check_send_stream [Line]:6563 pid 578 usr chn 64 device 0 chn 64 stream len can't be zero!
```

## 原因分析

查看日志中报错stream len can't be zero!，被VDEC代码参数校验拦截，建议排查传入的参数stream-\>len或stream-\>addr是否合法。

## 解决方法

检查代码中的stream-\>len参数值，发现len为0，修改参数赋值代码逻辑。
