# Decoding Artifacts Due to Buffer Release In Advance

## Symptom

All frames of the original H.264/H.265 video streams are normal, and no exception occurs during decoding \(no exception log is generated\). However, the output image is abnormal.

## Possible Cause

If no exception occurs during decoding, the input streams are normal. In this case, if the output streams are damaged, the possible causes are as follows:

1. The output buffer is reused by others, illegally accessed, or released in advance.
2. The output buffer required for decoding is larger than the actually allocated buffer.

## Solution

1. Add log printing of the buffer size and address to the DVPP buffer allocation API, check the VDEC output buffer, and check whether the allocated buffer size is the same as the actually used one. For example, in a typical error scenario, the VDEC output format is expected to be RGB, but the buffer is still allocated based on YUV420SP.
2. Add log printing of the buffer size and address to the DVPP buffer release API, as well as hi\_mpi\_vdec\_get\_frame, aclvdecCallback, or acldvppJpegDecodeAsync. Check the timing of buffer release and check whether the buffer address is released before decoding is complete.
