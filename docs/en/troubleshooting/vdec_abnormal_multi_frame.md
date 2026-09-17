# VDEC Exception Due to the Input of Multi-Frame Stream as a Single-Frame Stream

## Symptom

Frame loss occurs during decoding, and an error log is generated.

A log example on the device is as follows:

```text
User send more than one stream data, but only send one outbuf
```

>**NOTE:**
>In EP mode, after running the decoding process, log in to the host and run the  **msnpureport -a**  command in the directory on which you have the read, write, and execute permissions to export the log information of the device.
>In RC mode, log in to the board environment and run the  **cat /proc/umap/vdec**  command to export decoding information.

## Possible Cause

VDEC supports only the sending streams by frame. Therefore, when calling  **hi\_mpi\_vdec\_send\_stream**, send a single-frame stream data and the corresponding output buffer each time. If multi-frames stream data is sent at a time \(multiple frames of stream data in the input stream buffer\), VDEC discards all frames except the first frame and prints an error log.

## Solution

Check the code logic. Check whether multiple frames are read at a time in the input stream buffer \(**stream-\>addr**\) when  **hi\_mpi\_vdec\_send\_stream**  is called. If yes, modify the code logic.
