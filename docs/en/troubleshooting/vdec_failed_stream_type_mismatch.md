# VDEC Failure Due to Inconsistency Between the Actual Stream Type and the Decoder Type Set in the API

## Symptom

VDEC fails to decode every frame.

A log example on the device is as follows:

```text
temporal_id(-1) is not supported.
sps id 2 is larger than 2.
pid 2487 usr chn 4 device 0 video format unsupport at event chn 4
```

>**NOTE:**
>In  Ascend EP  form, after running the decoding process, log in to the host and run the  **msnpureport -a**  command in a directory on which you have the read, write, and execute permissions to export the log information of the device.
>In  Ascend RC  form, log in to the board environment and run the  **cat /proc/umap/vdec**  command to export decoding information.

## Possible Cause

The decoding protocol type \(HI\_PT\_H264 or HI\_PT\_H265\) is specified during the creation of a VDEC channel. If the actual decoding stream type is different from the configured decoding protocol type, the decoding fails.

## Solution

Check whether the input parameter  **attr-\>type**  passed by the  **hi\_mpi\_vdec\_create\_chn**  API is  **HI\_PT\_H264**  or  **HI\_PT\_H265**, and compare it with the actual stream type.
