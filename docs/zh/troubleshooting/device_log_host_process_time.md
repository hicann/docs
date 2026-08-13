# 通过Device日志确认Host进程的拉起与结束时间

问题定位时往往需要先初步定界到问题发生的大致时间点，再根据出错时间的详细日志继续定位。这时，可以通过查找Device日志的ringbuffer关键字，来判断业务进程的拉起与结束时间，定界到问题发生的时间点。

Ringbuffer是上报error信息的一片共享内存，任务拉起时会进行create ringbuffer操作，任务结束时会进行delete ringbuffer操作，所以可以通过ringbuffer日志确认任务的拉起和结束时间，详细操作如下：

## Ascend EP形态

1. 登录Host侧服务器。
2. 通过msnpureport工具导出Device侧系统类日志和其他维测信息。

    在某个有读、写、执行权限的目录（如“/var/log/npu/report”，下文以此路径为例）下执行msnpureport工具。

    msnpureport工具命令示例如下：

    ```bash
    msnpureport -f
    ```

3. 在导出的Device侧非Control CPU上的系统类日志根目录下，查询进程创建与销毁相关的日志。

    例如，在/var/log/npu/report/\*/slog/device-os-0/\[run|debug\]/device-0目录下查询device-0上进程拉起与结束的日志信息，\*表示该日志文件创建时的时间戳，命令示例如下：

    ```bash
    grep -rn ringbuffer
    ```

    日志片段举例如下，日志片段中的YYYY‑MM‑DD‑HH:MM:SS.fff.uuu（年‑月‑日‑时:分:秒.毫秒.微秒）表示日志输出时间。

    ```bash
    device-0_******.log:23102:[EVENT] TSCH(-1,null):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu 17641 (dieid:0,cpuid:0) ringbuffer.c:177 delete_ringbuffer: pid=3299758, vf_id=0
    device-0_******.log:23103:[EVENT] TSCH(-1,null):2YYYY‑MM‑DD‑HH:MM:SS.fff.uuu 17642 (dieid:0,cpuid:0) ringbuffer.c:134 create_ringbuffer: pid=3299758, vf_id=0, buffer_len=10, runtime ver=2, offset=276096, ringbuffer_addr=0x1f7dc00000.
    device-0_******.log:23104:[EVENT] TSCH(-1,null):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu 17643 (dieid:0,cpuid:0) ringbuffer.c:163 create_ringbuffer: last_Id=21, vf_id=0, pid=3299758
    device-0_******.log:23503:[EVENT] TSCH(-1,null):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu 47266 (dieid:0,cpuid:0) ringbuffer.c:177 delete_ringbuffer: pid=3299758, vf_id=0
    ```

    如上图所示：

    - 日志中“create\_ringbuffer”关键字表示进程拉起，因此上图中device-0上ID为“3299758”的进程创建时间为“2023-12-02-14:29:25”。

        为了避免重复创建，每一次创建ringbuffer前都会进行ringbuffer删除操作，所以创建的日志包括“delete\_ringbuffer”和“create\_ringbuffer”。

        日志中，若对于同一个进程，有多个“create\_ringbuffer”，则其中包含ringbuffer\_addr关键字的日志时间表示该进程的拉起时间。

    - 日志中“delete\_ringbuffer”关键字表示进程结束，因此上图中device-0上ID为“3299758”的进程销毁时间为“2023-12-04-11:44:15”。

        日志中，若对于同一个进程，有多个“delete\_ringbuffer”，则最后一次“delete\_ringbuffer”的日志时间表示该进程的结束时间。

## Ascend RC形态

1. 登录板端环境。
2. 查看Device日志。

    例如，在“/var/log/npu/slog/\[run|debug\]/device-0”目录下查询device-0上进程拉起与结束的日志信息，命令示例如下：

    ```bash
    grep -rn ringbuffer
    ```

    日志举例如下，日志片段中的YYYY‑MM‑DD‑HH:MM:SS.fff.uuu（年‑月‑日‑时:分:秒.毫秒.微秒）表示日志输出时间。

    ```bash
    device-0_******.log:23102:[EVENT] TSCH(-1,null):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu 17641 (dieid:0,cpuid:0) ringbuffer.c:177 delete_ringbuffer: pid=3299758, vf_id=0
    device-0_******.log:23103:[EVENT] TSCH(-1,null):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu 17642 (dieid:0,cpuid:0) ringbuffer.c:134 create_ringbuffer: pid=3299758, vf_id=0, buffer_len=10, runtime ver=2, offset=276096, ringbuffer_addr=0x1f7dc00000.
    device-0_******.log:23104:[EVENT] TSCH(-1,null):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu 17643 (dieid:0,cpuid:0) ringbuffer.c:163 create_ringbuffer: last_Id=21, vf_id=0, pid=3299758
    device-0_******.log:23503:[EVENT] TSCH(-1,null):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu 47266 (dieid:0,cpuid:0) ringbuffer.c:177 delete_ringbuffer: pid=3299758, vf_id=0
    ```

    如上图所示：

    - 日志中“create\_ringbuffer”关键字表示进程拉起，因此上图中device-0上ID为“3299758”的进程创建时间为“2023-12-02-14:29:25”。

        为了避免重复创建，每一次创建ringbuffer前都会进行ringbuffer删除操作，所以创建的日志包括“delete\_ringbuffer”和“create\_ringbuffer”。

        日志中，若对于同一个进程，有多个“create\_ringbuffer”，则其中包含ringbuffer\_addr关键字的日志时间表示该进程的拉起时间。

    - 日志中“delete\_ringbuffer”关键字表示进程结束，因此上图中device-0上ID为“3299758”的进程销毁时间为“2023-12-04-11:44:15”。

        日志中，若对于同一个进程，有多个“delete\_ringbuffer”，则最后一次“delete\_ringbuffer”的日志时间表示该进程的结束时间。
