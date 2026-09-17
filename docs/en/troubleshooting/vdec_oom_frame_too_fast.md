# VDEC OOM Due to Fast Frame Sending

## Symptom

During multi-channel decoding, the interval between frames is too short. As a result, frames are sent too fast, OOM occurs, and the decoding is suspended.

A log example on the device is as follows:

```text
OOM_NOTIFIER: oom type 2
```

>**NOTE:**
>In EP mode, after running the decoding process, log in to the host and run the  **msnpureport -a**  command in the directory on which you have the read, write, and execute permissions to export the log information of the device.
>In RC mode, log in to the board environment and run the  **cat /proc/umap/vdec**  command to export decoding information.

## Possible Cause

An output buffer needs to be applied each time a frame is sent. If the frame sending rate is much faster than the frame decoding rate, a large number of output buffers are required, which occupies a large amount of memory and results in OOM.

## Solution

Adjust the frame sending interval by referring to the VDEC performance indicators in  [DVPP Media Acceleration Library](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/acce/dvpp/dvp.html).
