# AI Core超时故障

## 问题现象

Host应用类日志（log/\[run|debug\]/plog/plog-_pid_\_\*.log）中存在如下报错。YYYY‑MM‑DD‑HH:MM:SS.fff.uuu（年‑月‑日‑时:分:秒.毫秒.微秒）表示日志输出时间。

```bash
[ERROR] RUNTIME(2897353,main):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [device_error_core_proc.cc:1227]2897467 PrintCoreInfo:An error occurs on the device(chipId:0, dieId:0), the serial number is 7, the error is aivec error, core id is 9, error code = 0, dump info: pc start: 0x1240000000e4, current: 0x12400000013c, vec error info: 0x6211f34358, mte error info: 0x7e33ba0d8b, ifu error info: 0x2075ca373f800, ccu error info: 0x2447806309616cb7, cube error info: 0, biu error info: 0, aic error mask: 0x6500020bd00028c, para base: 0x12c100001000, aic cond: 0. The extend info: errcode:(0, 0, 0) errorStr: timeout or trap error. fixp_error0 info: 0x3ba0d8b, fixp_error1 info: 0x7e, fsmId:1, tslot:0, thread:0, ctxid:0, blk:0, sublk:0, subErrType:2. For details, see the troubleshooting document on the Ascend official website. Search for the keyword "AI Core Error".
```

Device的event日志（slog/dev-os-_id_/run/event/event\_\*.log）中存在“**event\_id=0x80C98001**”或“**event\_id=0x80CB8001**”关键字。

## 故障根因

使用ascend-dmi工具压测AI Core，压测异常，提示**a timeout error occurred**，表示AI Core超时。报错示例如下所示：

```bash
Hardware:
    aicore:
        FAIL
        *** Some processes are seizing the NPU. Test results may be affected.
        *** Device 4: a timeout error occurred.
```

ascend-dmi工具需要单独安装，压测AI Core的命令示例如下：

```bash
ascend-dmi --dg -i aicore -s -q
```

ascend-dmi工具在MindCluster ToolBox软件包中，该软件与CANN的配套关系请单击[Link](https://www.hiascend.com/developer/download/community/result?module=dl+cann)查询，ascend-dmi工具的安装及详细使用指导请参见[Link](https://hiascend.com/document/redirect/mindxdl-ascenddmiug)。

## 处理方法

建议下电重启后再使用ascend-dmi工具压测，如果对应设备依旧出现timeout报错，则判断为硬件故障，需联系技术支持更换硬件。

您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。
