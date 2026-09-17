# Buffer Address Verification Error Due to Buffer Allocation with an Incorrect API

## Symptom

The error information in the log is as follows:

```text
address check failed ret 0x3, please check: 1. use hi_mpi_dvpp_malloc or aclDvppMalloc to alloc dvpp memory; 2. current buffer size 3110400 may be larger than actually allocated.
```

## Possible Cause

According to the log information, the possible causes are as follows:

1. The specified API is not used to allocate DVPP buffer.
2. The buffer size input by the API is smaller than the actually allocated buffer size.

## Solution

Check the code:

1. Check whether  **acldvppMalloc**  in media data processing V1 or  **hi\_mpi\_dvpp\_malloc**  in media data processing V2 is used to allocate buffer for storing the input or output data of JPEGD or VDEC.
2. Add log printing of the buffer size and address to the DVPP buffer allocation API, and check whether the buffer size input by  **hi\_mpi\_vdec\_get\_frame**,  **aclvdecSendFrame**, or  **acldvppJpegDecodeAsync**  exceeds the actually allocated buffer size.
