# Image Frame Failed to Be Sent to VENC

## Symptom

The return value of  **hi\_mpi\_venc\_send\_frame**  is not 0, indicating that a frame fails to be sent.

## Possible Cause

The possible causes of the frame sending failure are as follows:

- The input image frame parameter is not within the valid range or the parameter is not supported.
- The frame sending rate is too high, which exceeds the performance specification.

## Solution

Rectify the fault as follows:

- If the error code is  **0xa0088003**  or  **0xa0088008**, the input image frame parameter is not within the specified range or the parameter is set to a value that is not supported.

    You can further check the kernel log to determine which parameter is incorrect. As shown in the following information, the input YUV format is incorrect.

    ```text
    [Venc]:hevc_check_pixel_format [Line]:1110 H.265 don't support format 5,should be NV12(1) or NV21(2)
    ```

    Common causes:

    1. The input parameter structures are not initialized using memset. As a result, some parameters use random values if they are not set.
    2. The header file does not match the API. As a result, the input enumeration type does not meet the expectation.
    3. The ranges of supported parameters are unknown. For details, see the description in  [DVPP Media Acceleration Library](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/acce/dvpp/dvp.html).

- If the error code is  **0xa008800d**, the input idle queue of VENC is full, and no more data frames can be sent to VENC. The possible cause is that the frame sending rate is higher than the processing speed of the chip. As a result, when there are more than six data frames, the frames are stacked in the VENC input queue, leading to a reported error. In this case, you are advised to control the interval of calling  **hi\_mpi\_venc\_send\_frame**. For example, if the encoding frame rate is 30 fps, call  **hi\_mpi\_venc\_send\_frame**  at an interval of 33 ms.
