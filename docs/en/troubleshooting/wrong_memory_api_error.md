# Buffer Address Verification Error Due to Buffer Allocation with an Incorrect API

## Symptom

When a VPC API is called, the  **HI\_ERR\_VPC\_BADADDR**  \(**0xA0078011**\) error code is returned, and an error message is recorded in the log. The error logs vary according to the version.

- Log example 1

    ```text
    device 0, vpc address is illegal, please make sure it has been allocated with hi_mpi_dvpp_malloc or acldvppMalloc.
    ```

- Log example 2

    ```text
    dvpp_check_mem_usable [Line]:85 mem:0x****f000****4020 is not usable, please check:1. mem not allocated or has been freed;2. make sure mem actual size should be:8017920
    ```

## Possible Cause

According to the log information, the specified API is not used to allocate buffer.

## Solution

Check the code to see whether  **acldvppMalloc**  in media data processing V1 or  **hi\_mpi\_dvpp\_malloc**  in media data processing V2 is used to allocate buffer for storing the VPC input or output data.
