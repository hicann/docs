# VPC Parameter Verification Failure

## Symptom

The VPC API call returns  **0xA0078003**  \(**HI\_ERR\_VPC\_ILLEGAL\_PARAM**\), indicating that the parameter value is out of the valid range. Information similar to the following is displayed in the log, which may vary in different versions:

- Log message \(1\): The VPC resizing width is greater than the output width.

    ```text
    resize width (224) is greater than output width (120)
    ```

    Or

    ```text
    width should be in [10, 32768], width is 654321
    ```

- Log message \(2\): The VPC cropping width is greater than the input width.

    ```text
    crop width 120 cannot be greater than input width 100
    ```

- Log message \(3\): The input resizing algorithm is incorrect.

    ```text
    resize interpolation [8] is not supported
    ```

    Or

    ```text
    flip mode[5] not supported, support mode [0, 1, 2]
    ```

- Log message \(4\): The image buffer size is insufficient.

    ```text
    buffer size(50176) is smaller than need buffer size(95264) when format is 1
    ```

    Or

    ```text
    buffer size(50176) is smaller than need buffer size(95264) when format is 1
    ```

- Log message \(5\): Failed to verify the image address.

    ```text
    on device 0, num 0 input addr (start 0x100020003000 end 0x100020004000) is illegal
    ```

    Or

    ```text
    buffer address is null
    ```

- Log message \(6\): The VPC cropping output width or height is greater than the input width or height.

    ```text
    crop width[300] or height[300] is greater than input width[224] or height[224]
    ```

## Possible Cause

The possible causes are as follows:

- Log message \(1\): The VPC resizing width is greater than the output width.
- Log message \(2\): The VPC cropping width is greater than the input width.

- Log message \(3\): The input resizing algorithm is incorrect.
- Log message \(4\): The image buffer size is insufficient.
- Log message \(5\): Failed to verify the image address.
- Log message \(6\): The VPC cropping output width or height is greater than the input width or height.

## Fault Locating

1. Locate the VPC configuration parameter based on the error information in the log and modify the parameter as prompted.
2. Based on the error information in the log, rectify the fault by referring to  DVPP Media Acceleration Library \> Media Data Processing V1 APIs \> VPC Image Processing  or  DVPP Media Acceleration Library \> Media Data Processing V2 APIs \> VPC Image Processing.

## Solution

Modify the configuration file based on the error information.

1. For log message \(1\), change the resizing width to a value less than or equal to the output width.
2. For log messages \(2\) and \(6\), change the cropping width to a value less than the input width.
3. For log message \(3\), change the resizing algorithm to one that is supported by the current version.
4. For log message \(4\), allocate a sufficient buffer according to the format and correctly configure  **buffer\_size**.
5. For log message \(5\), allocate an image address using  **hi\_mpi\_dvpp\_malloc**  or  **acldvppMalloc**.
