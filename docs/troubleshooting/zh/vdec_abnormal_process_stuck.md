# VDEC视频解码异常导致进程卡死，无法退出

## 问题现象描述

用户进程卡死，无法退出。

查看应用类日志，一直重复提示信息“**fault kernel\_name=DvppSendVdecFrame**”、“**Kernel task happen error, retCode=0x28, \[aicpu timeout\]**”，表示AI CPU异常，无法处理VDEC解码任务，导致任务超时。

日志片段举例如下：

```bash
[ERROR] RUNTIME(pid,pName):DateTimeMS [task.cc:878]1827 PreCheckTaskErr:[DVPP][DEFAULT]Kernel task happen error, retCode=0x28, [aicpu timeout].
[ERROR] RUNTIME(pid,pName):DateTimeMS [task.cc:676]1827 PrintAicpuErrorInfo:[DVPP][DEFAULT]Aicpu kernel execute failed, device_id=0, stream_id=177, task_id=4, fault so_name=libdvpp_kernels.so, fault kernel_name=DvppSendVdecFrame, fault op_name=, extend_info=.
[ERROR] RUNTIME(pid,pName):DateTimeMS [task.cc:878]1831 PreCheckTaskErr:[DVPP][DEFAULT]Kernel task happen error, retCode=0x28, [aicpu timeout].
[ERROR] RUNTIME(pid,pName):DateTimeMS [task.cc:676]1831 PrintAicpuErrorInfo:[DVPP][DEFAULT]Aicpu kernel execute failed, device_id=0, stream_id=170, task_id=8, fault so_name=libdvpp_kernels.so, fault kernel_name=DvppSendVdecFrame, fault op_name=, extend_info=.
[ERROR] RUNTIME(pid,pName):DateTimeMS [engine.cc:960]1766 ReportExceptProc:[DVPP][DEFAULT]Task exception! device_id=0, stream_id=107, task_id=8, type=1, retCode=0x28.
[ERROR] RUNTIME(pid,pName):DateTimeMS [engine.cc:960]1773 ReportExceptProc:[DVPP][DEFAULT]Task exception! device_id=0, stream_id=130, task_id=4, type=1, retCode=0x28.
```

## 可能原因

Device内存不足，AI CPU无法处理VDEC解码任务，导致任务超时。

## 处理步骤

1. 在使用媒体数据处理V1版本的VDEC视频解码功能前，可查看[《DVPP媒体加速库》](https://hiascend.com/document/redirect/CannCommunityDvppApi)手册中的VDEC功能约束，参考“每路VDEC解码的内存消耗计算公式”，预估需使用的Device内存，并合理规划Device上的内存。
2. 优化应用程序的代码逻辑，增加异常处理机制，获取VDEC解码异常信息，强制退出进程。

    在调用aclinit接口之后，定义异常回调函数，并调用aclrtSetExceptionInfoCallback接口设置异常回调函数，用于获取任务异常信息，以便在异常分支中根据任务异常信息来判断是否退出应用进程。

    基本接口调用逻辑如下：

    1. 定义并实现异常回调函数fn\(aclrtExceptionInfoCallback类型\)，回调函数原型为：typedef void \(\*aclrtExceptionInfoCallback\)\(aclrtExceptionInfo \*exceptionInfo\)

        在异常回调函数fn内调用aclrtGetDeviceIdFromExceptionInfo、aclrtGetStreamIdFromExceptionInfo、aclrtGetTaskIdFromExceptionInfo接口分别获取Device ID、Stream ID、Task ID。

        根据Stream ID、Task ID判断Device是否异常，若异常，则强制退出进程。

        异常回调函数实现示例如下：

        ```c
        void dvpp_callback(aclrtExceptionInfo * exception_info)
        {
            uint32_t taskId = aclrtGetTaskIdFromExceptionInfo(exception_info);
            uint32_t streamId = aclrtGetStreamIdFromExceptionInfo(exception_info);
            uint32_t deviceId = aclrtGetDeviceIdFromExceptionInfo(exception_info);
        
            if(taskId == 0xffffffff) || (streamId == 0xffffffff) {
                //Device异常，强制退出进程
            } else {
                //任务异常，如果频繁出现（例如，统计1秒内触发异常回调函数的次数），进程退出
            }
            return;
        }
        ```

    2. 调用aclrtSetExceptionInfoCallback接口设置异常回调函数。
    3. 执行VDEC解码。
