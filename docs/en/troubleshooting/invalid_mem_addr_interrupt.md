# Exception Due to Invalid Read/Write Buffer Address

## Symptom

The kernel-space log on the device reports an error indicating that the VPC has an exception. \(The error log in different version may be different.\)

- Log 1

    ```text
    vpc get err int: vpc_cvdr_axi_rd_resp_err
    ```

- Log 2

    ```text
    vpc get err int: vpc_cvdr_axi_wr_resp_err
    ```

## Possible Cause

- **cvdr\_axi\_rd\_resp\_err**  indicates out-of-bounds read. This is possibly because the allocated input buffer is too small or the buffer address is invalid. As a result, the  AI processor  accesses an invalid address when performing the read operation.
- **cvdr\_axi\_wr\_resp\_err**  indicates out-of-bounds write. This is possibly because the allocated output buffer is too small or the buffer address is invalid. As a result, the  AI processor  accesses an invalid address when performing the write operation.

## Solution

1. Add log printing to the API for allocating DVPP buffer and the API for an abnormal VPC task. Check whether the allocated input/output buffer size is the same as the actually used input/output buffer size.
2. Add log printing to the API for releasing DVPP buffer to check whether the buffer is released before the VPC task is complete.
