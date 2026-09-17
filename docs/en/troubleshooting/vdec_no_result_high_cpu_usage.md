# No Error Is Reported During VDEC, But No Decoding Result Is Output and the CPU Usage is High

## Symptom

Check the app log and find that no error is reported and no decoding result is output. Run the  **top**  command on the Linux server where the app is running, and find that the CPU usage of the app process keeps increasing.

## Possible Cause

1. If no error occurs and no decoding result is output, the possible cause is that the decoding frame sending API  **aclvdecSendFrame**  is properly called but the callback function is not triggered. As a result, the decoding result data cannot be obtained.
2. Check the logic of code that triggers the callback function.

    VDEC API call logic: The user creates an independent thread and defines the thread function in advance, and then calls  **aclrtProcessReport**  in the thread function to configure the timeout interval. After the specified timeout interval ends, the callback function is triggered to obtain the decoding result.

    ```c
    void *ThreadFunc(aclrtContext sharedContext)
    {
        if (sharedContext == nullptr) {
            ERROR_LOG("sharedContext can not be nullptr");
            return ((void*)(-1));
        }
        INFO_LOG("use shared context for this thread");
        aclError ret = aclrtSetCurrentContext(sharedContext);
        if (ret != ACL_SUCCESS) {
            ERROR_LOG("aclrtSetCurrentContext failed, errorCode = %d", static_cast<int32_t>(ret));
            return ((void*)(-1));
        }

        INFO_LOG("thread start ");
        while (runFlag) {
            // Notice: timeout 1000ms
            (void)aclrtProcessReport(1000);
        }
        return (void*)0;
    }
    ```

3. If the API call logic that triggers the callback function is correct, add log printing at  **aclrtProcessReport**  to check whether the thread successfully calls  **aclrtProcessReport**  during app running. The callback function can be triggered only when  **aclrtProcessReport**  is successfully called.

    The sample code is as follows:

    ```c
    while (runFlag) {
            // Notice: timeout 1000ms
            aclError ret = aclrtProcessReport(1000);
            printf("aclrtProcessReport failed, ret=%d.\n", ret);
    }
    ```

4. After modifying the code, recompile and run the app.

    If the following information is displayed repeatedly,  **aclrtProcessReport**  fails to be called:

    ```text
    aclrtProcessReport failed, ret = 107012
    ```

    According to the API return value  **107012**, the thread is not subscribed or subscribed repeatedly.

5. Check the code logic and determine whether  **aclvdecSetChannelDescThreadId**  is called to bind the thread created by the user. According to the API call logic of VDEC,  **aclrtProcessReport**  can be called only after  **aclvdecSetChannelDescThreadId**  is called to bind the user thread, and then the callback function can be triggered.
6. After modifying the code, and recompiling and running the app, the VDEC is normal, the decoding result is properly output, and the CPU usage decreases.

## Solution

Develop VDEC functions by referring to the VDEC function sample  [here](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/1_classification/vdec_resnet50_classification).

Pay attention to the following points:

- Create a thread and define the thread function in advance. Once  **aclrtProcessReport**  is called in the thread function, the callback function will be triggered after a specified period of time.
- Call  **aclvdecSetChannelDescThreadId**  to bind the thread created by the user.

- When releasing resources, destroy the channel and channel description in sequence before destroying the thread created by the user.
