# Buffer Address Verification Error Due to Buffer Allocation with an Incorrect API

## Symptom

The error information in the log is as follows:

- Log 1

    ```text
    device:0 chan 0, venc or jpege input buffer is invalid, make sure it has been allocated with hi_mpi_dvpp_malloc or aclDvppMalloc.
    ```

- Log 2

    ```text
    device:0 chan 0, venc or jpege output buffer is invalid, make sure it has been allocated with hi_mpi_dvpp_malloc or aclDvppMalloc.
    ```

- Log 3

    ```text
    device:0 chan 0, jpege input buffer is invalid, make sure it has been allocated with hi_mpi_dvpp_malloc or aclDvppMalloc.
    ```

- Log 4

    ```text
    device:0 chan 0, jpege output buffer is invalid, make sure it has been allocated with hi_mpi_dvpp_malloc or aclDvppMalloc.
    ```

## Possible Cause

According to the log information, the specified API is not used to allocate buffer.

## Solution

Use  **acldvppMalloc**  in media data processing V1 or  **hi\_mpi\_dvpp\_malloc**  in media data processing V2 to allocate DVPP buffer for storing the input or output data of JPEGE or VENC.
