# Buffer Size Error Despite Buffer Allocation with a Correct API

## Symptom

The error information in the log is as follows:

```text
device:0 chan 0, output terminal address is invalid, maybe outBufSize:3110400 is invalid.
```

## Possible Cause

The buffer size input by the API is too large and exceeds the range of the actually allocated buffer. As a result, an error occurs during the internal end address verification.

## Solution

Add log printing of the buffer address and length to the DVPP buffer allocation API. Check whether the buffer lengths input by  **hi\_mpi\_venc\_send\_frame**,  **hi\_mpi\_venc\_send\_jpege\_frame**,  **aclvencSendFrame**, and  **acldvppJpegEncodeAsync**  are the same.
