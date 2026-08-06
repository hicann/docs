# VDEC视频解码无报错，但无解码结果数据、CPU占用率高

## 问题现象描述

查看应用类日志，无ERROR报错、无解码结果数据输出，另外，在运行应用程序的Linux服务器上执行top命令，该应用进程的cpu占用率持续升高。

## 可能原因

1. 无ERROR、无解码结果数据输出，判断可能是因为解码发帧接口aclvdecSendFrame调用正常，但未触发回调函数，无法获取解码结果数据。
2. 检查触发回调函数的代码逻辑。

    按照VDEC视频解码的接口调用逻辑：由用户提前创建一个单独的线程，并自定义线程函数，在线程函数内调用aclrtProcessReport接口，通过该接口配置超时时间，等待指定的超时时间后，触发回调函数，获取解码结果数据。

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

3. 如果触发回调函数的接口调用逻辑正确，则在aclrtProcessReport接口处增加日志打印，判断应用运行过程中线程是否成功调用了aclrtProcessReport接口，只有成功调用aclrtProcessReport接口，才会触发回调函数。

    示例代码如下：

    ```c
    while (runFlag) {
            // Notice: timeout 1000ms
            aclError ret = aclrtProcessReport(1000);
            printf("aclrtProcessReport failed, ret=%d.\n", ret);
    }
    ```

4. 修改代码后，重新编译运行应用。

    在终端屏幕重复出现以下打印信息，表示调用aclrtProcessReport接口失败：

    ```bash
    aclrtProcessReport failed, ret = 107012
    ```

    查阅该接口的返回值说明，107012表示线程未订阅或重复订阅。

5. 检查代码逻辑，检查是否调用aclvdecSetChannelDescThreadId接口绑定用户新建的线程，按照VDEC视频解码的接口调用逻辑，只有调用该接口绑定用户线程，才可以触发调用aclrtProcessReport接口，进而触发回调函数。
6. 修改代码后，重新编译运行应用，VDEC视频解码正常，正常输出解码结果数据，同时cpu占用率下降。

## 解决办法

参考[Link](https://gitee.com/ascend/samples/tree/master/cplusplus/level2_simple_inference/1_classification/vdec_resnet50_classification)上的VDEC功能样例开发VDEC功能。

其中，需关注以下注意点：

- 创建新线程，并自定义线程函数，在线程函数内调用aclrtProcessReport接口，等待指定时间后，触发回调函数。
- 需调用aclvdecSetChannelDescThreadId接口绑定用户创建的新线程。

- 释放资源时，依次销毁通道、销毁通道描述信息后，才可以销毁用户创建的新线程。
