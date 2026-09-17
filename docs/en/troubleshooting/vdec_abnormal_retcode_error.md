# VDEC Exception Due to Incorrect Setting of retCode

## Symptom

After a frame of stream is sent by calling  **aclvdecSendFrame**, the output image description is reused for the decoding of subsequent frames. As a result, decoding fails and exceptions occur repeatedly.

A log snippet is as follows:

```text
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

## Possible Cause

According to the log information, the value of  **retCode**  obtained using the  **acldvppGetPicDescRetCode**  API is  **2**. If the value of  **retCode**  is not  **0**, decoding is abnormal.

It is found in the code logic that  **retCode**  is set to  **2**  because the previous frame fails to be decoded. When the output image description is reused,  **retCode**  inherits the status value  **2**. As a result, when the subsequent frames are decoded, the system determines that the decoding fails.

## Solution

If the output image description is reused, call  **acldvppSetPicDescRetCode**  to set  **retCode**  to  **0**  to prevent the abnormal decoding status of the previous frame from affecting subsequent decoding.
