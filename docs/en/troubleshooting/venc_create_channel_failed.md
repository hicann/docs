# Failed to Create a VENC Channel

## Symptom

The return value of  **hi\_mpi\_venc\_create\_chn**  is not 0, indicating that the channel fails to be created.

## Possible Cause

The possible causes of the channel creation failure are as follows:

- The input VENC channel ID is out of the valid range \[0, 255\], which allows only a maximum of 256 channels.
- The input channel attribute parameter is not within the valid range or the parameter is not supported.
- An existing channel is being created. For example, channel 0 is created again before it is destroyed.

## Solution

Rectify the fault as follows:

- Check the error code returned when  **hi\_mpi\_venc\_create\_chn**  fails to be called.
- If the error code is  **0xa0088002**, the input channel ID exceeds the valid range. In this case, you need to change the channel ID to a value within the range of \[0, 255\].
- If the error code is  **0xa0088003**  or  **0xa0088008**, the input channel attribute parameter is not within the specified range or the parameter is set to a value that is not supported currently.

    You can further check the kernel log to determine which parameter is incorrect. As shown in the following information, the input resolution is incorrect.

    ```text
    [Venc]:venc_drv_check_resolution [Line]:342 max picture width (0) err! should in [128,4096]!
    ```

    Common causes:

    1. The input parameter structures are not initialized using memset. As a result, some parameters use random values if they are not set.
    2. The header file does not match the API. As a result, the input enumeration type does not meet the expectation.
    3. The ranges of supported parameters are unknown. For details, see the description in  [DVPP Media Acceleration Library](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/acce/dvpp/dvp.html).

- If the error code is  **0xa0088004**, an existing channel is being created. For example, channel 0 is created again before it is destroyed.

    ```text
    [Venc]:venc_create_chn [Line]:2449 device:0 chnl:0 had been created!
    ```

    In this case, check the code logics: \(1\) Check whether a channel is destroyed after being created. \(2\) Whether the same channel ID is used repeatedly to create channels.
