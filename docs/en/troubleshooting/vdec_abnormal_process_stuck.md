# Suspended User Process Due to VDEC Exceptions

## Symptom

A user process is suspended and cannot exit.

In the app logs, messages "fault kernel\_name=DvppSendVdecFrame" and "Kernel task happen error, retCode=0x28, \[aicpu timeout\]" are repeatedly displayed, indicating that the AI CPU is abnormal and cannot handle the VDEC task. As a result, the task times out.

A log snippet is as follows:

```text
[ERROR] RUNTIME(pid,pName):DateTimeMS [task.cc:878]1827 PreCheckTaskErr:[DVPP][DEFAULT]Kernel task happen error, retCode=0x28, [aicpu timeout].
[ERROR] RUNTIME(pid,pName):DateTimeMS [task.cc:676]1827 PrintAicpuErrorInfo:[DVPP][DEFAULT]Aicpu kernel execute failed, device_id=0, stream_id=177, task_id=4, fault so_name=libdvpp_kernels.so, fault kernel_name=DvppSendVdecFrame, fault op_name=, extend_info=.
[ERROR] RUNTIME(pid,pName):DateTimeMS [task.cc:878]1831 PreCheckTaskErr:[DVPP][DEFAULT]Kernel task happen error, retCode=0x28, [aicpu timeout].
[ERROR] RUNTIME(pid,pName):DateTimeMS [task.cc:676]1831 PrintAicpuErrorInfo:[DVPP][DEFAULT]Aicpu kernel execute failed, device_id=0, stream_id=170, task_id=8, fault so_name=libdvpp_kernels.so, fault kernel_name=DvppSendVdecFrame, fault op_name=, extend_info=.
[ERROR] RUNTIME(pid,pName):DateTimeMS [engine.cc:960]1766 ReportExceptProc:[DVPP][DEFAULT]Task exception! device_id=0, stream_id=107, task_id=8, type=1, retCode=0x28.
[ERROR] RUNTIME(pid,pName):DateTimeMS [engine.cc:960]1773 ReportExceptProc:[DVPP][DEFAULT]Task exception! device_id=0, stream_id=130, task_id=4, type=1, retCode=0x28.
```

## Possible Cause

The device memory is insufficient.

## Solution

1. Before using VDEC of media data processing V1, view VDEC functions and restrictions in  [DVPP Media Acceleration Library](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/acce/dvpp/dvp.html), and predict the required device memory and allocate it properly by referring to the formula for calculating the maximum memory used by each VDEC channel.
2. Optimize the app code logic by adding an exception handling mechanism to obtain the VDEC exception information, and forcibly kill the process.

    After the  **aclinit**  call, define an exception callback function and call  **aclrtSetExceptionInfoCallback**  to set the function to obtain the task exception information, based on which you can determine whether to exit the app process in an exception branch.

    The API call logic is as follows:

    1. Define and implement an exception callback function \(**aclrtExceptionInfoCallback**  type\). The prototype is  **typedef void \(\*aclrtExceptionInfoCallback\)\(aclrtExceptionInfo \*exceptionInfo\)**.

        Call  **aclrtGetDeviceIdFromExceptionInfo**,  **aclrtGetStreamIdFromExceptionInfo**, and  **aclrtGetTaskIdFromExceptionInfo**  in the exception callback function to obtain the device ID, stream ID, and task ID, respectively.

        Check whether the device is abnormal based on the stream ID and task ID. If so, forcibly kill the process.

        The following is an example of implementing the exception callback function:

        ```c
        void dvpp_callback(aclrtExceptionInfo * exception_info)
        {
            uint32_t taskId = aclrtGetTaskIdFromExceptionInfo(exception_info);
            uint32_t streamId = aclrtGetStreamIdFromExceptionInfo(exception_info);
            uint32_t deviceId = aclrtGetDeviceIdFromExceptionInfo(exception_info);

            if(taskId == 0xffffffff) || (streamId == 0xffffffff) {
                //Device exception. Forcibly kill the process.
            } else {
                //Task exception. Forcibly kill the process if the exception occurs frequently (based on the exceptions triggered within a period of time, for example, 1s).
            }
            return;
        }
        ```

    2. Call  **aclrtSetExceptionInfoCallback**  to set the exception callback function.
    3. Execute the VDEC process.
