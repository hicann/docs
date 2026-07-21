# AI CPU算子维度超过8维报错

## 问题现象

GE执行报错，在应用程序运行日志中GE打印了ReportErrMessage的错误信息，且提示“shape dim num should be less than****8”。

Ascend EP形态，应用程序运行日志默认在$HOME/ascend/log/\[run|debug\]/plog路径下，日志文件为plog-_pid\_\*_.log。

Ascend RC形态，应用程序运行日志默认在$HOME/ascend/log/\[run|debug\]/device-app-_pid_路径下，日志文件为device-app-_pid_\_\*.log。

```bash
[ERROR] OP(1491846,main):2024-09-27-10:49:20.272.060 [aicpu_ext_info_handle.cpp:290][NNOP][UpdateShape][1491965] errno[561000] OpName:[aclnnGatherV2_0_GatherV2AiCPU] shape dim num should be less than 8, but got [9].
[INFO] GE(1491846,main):2024-09-27-10:49:20.272.133 [error_manager.cc:411]1491965 ReportErrMessage:report error_message, error_code:EZ9999, work_stream_id:149186091965, error_mode:0.
[ERROR] OP(1491846,main):2024-09-27-10:49:20.272.448 [aicpu_ext_info_handle.cpp:290][NNOP][UpdateShape][1491965] errno[561000] OpName:[aclnnGatherV2_0_GatherV2AiCPU] shape dim num should be less than 8, but got [9].
[INFO] GE(1491846,main):2024-09-27-10:49:20.272.473 [error_manager.cc:411]1491965 ReportErrMessage:report error_message, error_code:EZ9999, work_stream_id:149186091965, error_mode:0.
[ERROR] OP(1491846,main):2024-09-27-10:49:20.272.491 [aicpu_ext_info_handle.cpp:101][NNOP][AppendExtInfoShape][1491965] errno[561000] OpName:[aclnnGatherV2_0_GatherV2AiCPU] Assert ((UpdateShape(shape, &inputs[index])) == OK) failed
```

## 可能原因

AI CPU算子输入/输出参数的维度超过最大维度限制（8维）。

## 解决方法

根据报错信息修改算子参数输入/输出维度，确保不超过8维。

若仍无法解决，  您可以获取日志后单击[Link](https://www.hiascend.com/support)联系技术支持。
