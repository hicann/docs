# acl API Initialization Error Due to Insufficient Permission to Execute an App

## Symptom

The user process reports an error and exits.

Check the application log and find a message indicating that the device information fails to be obtained, resulting in the initialization failure. A log snippet is as follows:

```text
[ERROR] RUNTIME(89696,main):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [runtime.cc:1065]89696 CheckHaveDevice:[INIT][DEFAULT]Call halGetDeviceInfo failed: drvRet=4, module type=0, info type=1.
[ERROR] ASCENDCL(89696,main):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [acl.cpp:164]89696 aclInit: [INIT][DEFAULT][Init][Version]init soc version failed, ret = 507008
[ERROR] RUNTIME(89696,main):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_impl.cc:3490]89696 GetDevErrMsg:report error module_type=3, module_name=EE8888
[ERROR] RUNTIME(89696,main):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_impl.cc:3490]89696 GetDevErrMsg:ctx is NULL!
[ERROR] RUNTIME(89696,main):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_impl.cc:3546]89696 GetDevMsg:Failed to GetDeviceErrMsg, retCode=0x7070001.
[ERROR] RUNTIME(89696,main):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [logger.cc:1348]89696 GetDevMsg:GetDeviceMsg failed, getMsgType=0.
[ERROR] RUNTIME(89696,main):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [api_c.cc:3595]89696 rtGetDevMsg:ErrCode=107002, desc=[context pointer null], InnerCode=0x7070001
[ERROR] RUNTIME(89696,main):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:49]89696 FuncErrorReason:report error module_type=3, module_name=EE8888
[ERROR] RUNTIME(89696,main):YYYY‑MM‑DD‑HH:MM:SS.fff.uuu [error_message_manage.cc:49]89696 FuncErrorReason:rtGetDevMsg execute failed, reason=[context pointer null]
EL0003: The argument is invalid.
        Solution: Try again with a valid argument.
        TraceBack (most recent call last):
        [Init][Version]init soc version failed, ret = 507008[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        ctx is NULL![FUNC:GetDevErrMsg][FILE:api_impl.cc][LINE:3490]
        rtGetDevMsg execute failed, reason=[context pointer null][FUNC:FuncErrorReason][FILE:error_message_manage.cc][LINE:49]

[ERROR] acl init failed
[ERROR] Sample init resource failed
```

## Possible Cause

The possible causes are as follows:

- The device status is abnormal, that is, the device is not started properly.
- The user who runs the app does not have the permission to query the device information.

## Solution

1. Check whether the device is started properly.
    1. Log in to the environment where the driver package is installed as the  **root**  user and run the following command to query the driver installation path:

        ```bash
        cat /etc/ascend_install.info
        ```

        In this file,  **Driver\_Install\_Path\_Param**  indicates the installation path of the driver package.

    2. Access the driver installation path and use upgrade-tool to check the version of the file system running on the device. If the version can be queried, the device is started properly.

        ```bash
        ./upgrade-tool --device_index -1 --system_version
        ```

        Information similar to the following is displayed:

        ![](figures/image_0000001882036538.png)

2. Check whether the permission of the user who runs the app is correct.

    The user who runs the app must be in the same group as the driver running user. You can view the user group in the  **cat /etc/passwd**  file. The default driver running user is  **HwHiAiUser**.

    An example of the command for changing the owner group of a user is as follows:

    ```bash
    usermod -g Group name User name
    ```

3. If the problem persists, perform the following steps to obtain the log and contact technical support.  After obtaining the logs, click  [here](https://www.hiascend.com/support)  to contact technical support.
    1. Log in to the environment where the app is running and run the following command to set the log level to  **Debug**:

        ```bash
        export ASCEND_GLOBAL_LOG_LEVEL=0
        ```

    2. Run the app again.
    3. Obtain the app log from the log storage path.

        The default path for storing log files is  **$HOME/ascend/log**.

    4. Use the msnpureport tool to obtain the debug log on a specified device.

        The following is an example command, in which  **deviceID**  must be set to the ID of the specified device.

        ```bash
        msnpureport -g debug -d deviceID
        ```
