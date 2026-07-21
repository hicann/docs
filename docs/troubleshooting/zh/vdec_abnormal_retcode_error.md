# retCode返回值设置错误，导致VDEC视频解码异常

## 问题现象描述

调用aclvdecSendFrame接口发送一帧码流后，继续复用output输出图片描述信息，进行后续帧码流的解码操作，结果反复出现解码不成功、解码异常的情况。

日志片段举例如下：

```bash
Channel[0]: success to aclvdecSendFrame, loop=1, count=7
get frame success, totalCount=7
packet.size is 26084.
Channel[0]: begin to send frame, loop=1, count=8
acldvppGetPicDescRetCode, retCode: 2.
Vdec ERROR!!!!!!!!!!!!!!!!
errCount is 3. total count is 3.
!!!!!!!!!!!!!!!!!!acldvppGetPicDescRetCode, retCode: 2.right_count:0,fail_count:3,total_count:3
Channel[0]: success to aclvdecSendFrame, loop=1, count=8
get frame success, totalCount=8
packet.size is 27927.
Channel[0]: begin to send frame, loop=1, count=9
acldvppGetPicDescRetCode, retCode: 2.
Vdec ERROR!!!!!!!!!!!!!!!!
errCount is 4. total count is 4.
!!!!!!!!!!!!!!!!!!acldvppGetPicDescRetCode, retCode: 2.right_count:0,fail_count:4,total_count:4
```

## 可能原因

根据日志中的提示，通过acldvppGetPicDescRetCode接口获取到的retCode为2，retCode为非0值时，表示解码异常。

再查看代码逻辑时，发现由于前一帧码流解码失败，retCode被置为2，在复用output输出图片描述信息时，retCode也继承了前一帧解码失败的状态值2，导致在解码后续帧时，获取到retCode值为2，就一直判断解码是失败。

## 处理步骤

如果存在复用output输出图片描述信息的场景，需先调用acldvppSetPicDescRetCode设置为0，防止前一帧解码异常的状态影响后续解码。
