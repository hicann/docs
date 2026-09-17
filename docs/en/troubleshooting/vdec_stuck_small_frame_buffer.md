# VDEC Stuck Due to Small Frame Buffer Size and Insufficient Number of Reference Frames of the Decoder

## Symptom

Decoding is stuck. An error message is displayed in the log, indicating that frame buffers fails to be allocated.

A log example on the device is as follows:

```text
pid 0 usr chn 0 device 0 chn 0, user set frame buffer size(1000 Byte) and ref frame num(5) is not enough for actual frame buffer size(2000 Byte) and actual ref frame num(7), pic width = 1280, height = 720, bit_width =8
```

>**NOTE:**
>In EP mode, after running the decoding process, log in to the host and run the  **msnpureport -a**  command in the directory on which you have the read, write, and execute permissions to export the log information of the device.
>In RC mode, log in to the board environment and run the  **cat /proc/umap/vdec**  command to export decoding information.

## Possible Cause

A certain number of frame buffers should be allocated in the decoder. During frame buffer adaptation, if the configured  _frame buffer size x frame buffer count_  is less than the required  _frame buffer size x frame buffer count_, the decoding fails.

## Solution

When creating a VDEC channel by calling  **hi\_mpi\_vdec\_create\_chn**, adjust the passed frame buffer size and frame buffer count \(**attr-\>frame\_buf\_size**  and  **attr-\>frame\_buf\_cnt**\) parameters or set them to  **0**, indicating auto adaptation by the decoder.
