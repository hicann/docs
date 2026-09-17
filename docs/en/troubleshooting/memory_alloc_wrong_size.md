# Buffer Size Error Despite Buffer Allocation with a Correct API

## Symptom

The error logs may vary in different versions.

- Log example 1

    ```text
    buffer size(3110400) is smaller than need buffer size(4147200) when format is 3.
    ```

- Log example 2

    ```text
    device 0, vpc end address is illegal, check allocated buffer size: configured buffer size: 3110400, current pic: format 3 width_stride 1920 height_stride 1080.
    ```

- Log example 3

    ```text
    dvpp_check_mem_usable [Line]:85 mem:0x****f000****4020 is not usable, please check:1. mem not allocated or has been freed;2. make sure mem actual size should be:8017920
    ```

## Possible Cause

1. The allocated buffer size is smaller than the input/output buffer size required by the format.
2. The buffer size input by the VPC API is normal and matches the input format. However, the buffer size exceeds the length of the actually allocated buffer. As a result, the end address is invalid.

## Solution

1. Check the code and the buffer size requirements of the corresponding format by referring to  DVPP Media Acceleration Library \> Media Data Processing V1 APIs \> VPC Image Processing  or  DVPP Media Acceleration Library \> Media Data Processing V2 APIs \> VPC Image Processing.
2. Add the log for printing the buffer length to the code and check whether the buffer size input by the VPC API is the same as the length of the actually allocated buffer.
