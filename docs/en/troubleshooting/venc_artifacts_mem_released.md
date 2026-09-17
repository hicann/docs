# Encoding Artifacts Due to Buffer Release In Advance

## Symptom

No other exception log information is recorded except the encoding artifacts.

## Possible Cause

The VENC input buffer is YUV image data, and is illegally accessed or released in advance.

## Solution

Add log printing of the buffer size and address to the DVPP buffer release API, as well as  **hi\_mpi\_venc\_get\_stream**,  **aclvencCallback**, and  **acldvppJpegEncodeAsync**. Check the timing of buffer release and check whether the input buffer is released before encoding is complete.
