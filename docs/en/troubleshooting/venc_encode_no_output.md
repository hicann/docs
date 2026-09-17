# No VENC Output

## Symptom

A VENC channel is created and frames are successfully sent. However, the  **hi\_mpi\_venc\_get\_stream**  call returns  **0xa008800e**, indicating that the encoded stream data cannot be obtained.

## Possible Cause

The possible causes are as follows:

- The input image frame memory is not allocated using  **hi\_mpi\_dvpp\_malloc**.
- The input image frame memory does not match the resolution.
- The OS memory management is faulty.

## Solution

Rectify the fault as follows:

- Check whether watchdog-related information is displayed in the log, which indicates that the memory usage is abnormal.

    ```text
    [Chnl]:chnl_watch_dog_timer_isr [Line]:1141 find VEDU_0  down,now reset it
    [Chnl]:chnl_watch_dog_blackbox [Line]:1097 vpu_id is 0, venc watchdog fail enter blackbx
    ```

- Check the memory allocation for the input image frame in the user code. If the memory is not allocated by calling  **hi\_mpi\_dvpp\_malloc**, VENC cannot access the memory properly, and there is no encoding output. In this case, you need to use  **hi\_mpi\_dvpp\_malloc**  to allocate the input memory.
- Check whether the memory and resolution of the input image frame match with each other. For example, for the YUV NV12 or NV21 format, the size of an image frame is width x height x 1.5. If the size of the memory sent to VENC is less than the configured resolution \(width x height x 1.5\), unexpected behavior such as out-of-bounds access occurs. In addition, no encoding output is generated. Ensure that the requested memory size matches the configured resolution.
- If the fault persists, the OS memory management may be faulty.  After obtaining the logs, click  [here](https://www.hiascend.com/support)  to contact technical support.
