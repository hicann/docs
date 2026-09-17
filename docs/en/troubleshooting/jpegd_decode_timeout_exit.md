# Exiting of the JPEGD Process Due to Timeout

## Symptom

The user process exits.

In the app logs, error logs similar to "task timeout, userData=..., timeout=30, duration=..." and warning logs similar to "frames statistic: ACL receive\(_n_\), send\(_n_-1\)" are displayed.  _n_  indicates the number of processed tasks.

A log snippet is as follows:

```text
[ERROR] AICPU(pid,pName):DateTimeMS [dvpp_timeout_manager.cc:33][OnPulse][tid:2581][DVPP_KERNELS] WaitId[10] task timeout, userData=0xe7ffe0001280, timeout=30, duration=30.930062.
[INFO] AICPU(pid,pName):DateTimeMS [dvpp_kernel_base.cc:222][SendTaskCompleteToTs][tid:2581][DVPP_KERNELS] Send task complete to ts success, taskId=2, streamId=44, errorCode=1.
[WARNING] DVPP(pid,pName):DateTimeMS [JpegdAsyncManager.cpp:405][API] [PrintFrameCount:405] [T208] DFX[JPEGD]: frames statistic: ACL receive(16), send(15)
```

## Possible Cause

When multiple channels of large-resolution \(for example, 3840 x 2160 or higher\) JPEG images with rotation information are concurrently decoded, the image decoding may take a long time. As a result, the user process exits due to timeout.

## Solution

1. Determine whether a large-size image contains rotation information.

    Use a JPEG stream analyzer \(such as JPEGsnoop\) to parse large-size images and check whether the images contain rotation information. If  **Orientation**  is  **1**, the image is not rotated. Otherwise, the rotation is performed by a certain angle. For example, the  **Orientation**  information parsed in the following figure is  **8**, indicating that the rotation is performed by 270° clockwise.

    ![](figures/image_0000001881876542.png)

2. If the images are large-size ones with rotation, you are advised to call a third-party library \(such as OpenCV\) for decoding.
