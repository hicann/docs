# VPC Call Failure

## Symptom

The VPC module fails to be called. \(The error logs in different versions may be different\). The log contains the following error information:

Log message \(1\)

```text
RoiNum(0), inputArea rightOffset is 1918, it should be odd!
```

Log message \(2\)

```text
Output bufferSize(65536) should not be smaller than widthStride(256) * heightStride(256) * 3 / 2 = 98304
```

Log message \(3\)

```text
Input widthStride(300) is not right, it should be 16 aligned!
```

```text
Input widthStride(16) is not right, it should not be smaller than 32!
```

Log message \(4\)

```text
bareDataAddr(0xaaaadeccdcd0), bareDataBufferSize(3133440) should be allocated by acldvppMalloc!
```

Log message \(5\)

```text
Both RoiNum(1) outputAddr(0xaaaadeccdcd0) and first roi outputAddr(0xffff00002000) should be allocated by acldvppMalloc!
```

Log message \(6\)

```text
RoiNum(0): inputConfigure cropArea, leftOffset(26) should be smaller than rightOffset(25)!
```

```text
RoiNum(0): inputConfigure cropArea, upOffset(80) should be smaller than downOffset(79)!
```

```text
RoiNum(0): inputConfigure cropArea, cropWidth(1931) should not be bigger than width(1920)!
```

```text
RoiNum(0): inputConfigure cropArea, cropHeight(1270) should not be bigger than height(1088)!
```

```text
RoiNum(0): inputConfigure cropArea, cropWidth(9) should be between [10, 8192]!
```

```text
RoiNum(0): inputConfigure cropArea, cropHeight(4) should be between [6, 8192]!
```

```text
RoiNum(0): inputConfigure cropArea, rightOffset(1921) should be smaller than width(1920)!
```

```text
RoiNum(0): inputConfigure cropArea, downOffset(1089) should be smaller than height(1088)!
```

Log message \(7\)

```text
RoiNum(0): scale must be in [1/32, 16], cropWidth(1920), pasteWidth(10)!
```

```text
RoiNum(0): scale must be in [1/32, 16], cropHeight(6), pasteHeight(100)!
```

## Possible Cause

The possible causes are as follows:

- Log message \(1\): The right offset coordinate of the VPC crop ROI must be an odd number. In the log message, 1918 is an even number, which does not meet the requirement.
- Log message \(2\): The size of the output buffer must be at least Width stride x Height stride x 3/2. The log message indicates that this requirement is not met.

- Log message \(3\): The width stride of the input image \(space occupied by each line of pixels in the buffer\) must be a multiple of 16 and at least 32. In the log, the width stride is 300, which is not a multiple of 16. You need to align the image and set the width stride to the aligned value.
- Log message \(4\): The input buffer of VPC needs to be allocated by using  **acldvppMalloc**.
- Log message \(5\): The output buffer of VPC needs to be allocated by using  **acldvppMalloc**.
- Log message \(6\): The VPC crop ROI does not satisfy the restrictions.
- Log message \(7\): The VPC resizing ratio range is \[1/32, 16\]. The log message indicates that the width of the crop ROI is  **1920**  while the width of the paste ROI is  **10**, which means 10/1920 < 1/32.

## Fault Locating

1. Locate the VPC configuration parameter based on the error information in the log and modify the parameter as prompted.
2. Based on the error information in the log, rectify the fault by referring to  DVPP Media Acceleration Library \> Media Data Processing V1 APIs \> VPC Image Processing  or  DVPP Media Acceleration Library \> Media Data Processing V2 APIs \> VPC Image Processing.

## Solution

Modify the configuration file based on the error information.

1. For log message \(1\), the right offset of the cropped region of the input image is incorrect. Change it to an odd number.
2. For log message \(2\), the size of the input buffer is incorrect. Check the code for allocating input buffer. The size of the allocated buffer should be 1920 x 1088 x 3/2, and the value of  **bareDataBufferSize**  should be 1920 x 1088 x 3/2.
3. For log message \(3\), the stride value of the input image does not meet the requirements. In this case, set the stride value to a multiple of 16.
4. For log message \(4\) and log message \(5\), allocate buffer by using  **acldvppMalloc**.
5. For log message \(6\), change the width of the cropped image.
6. For log message \(7\), change the resizing ratio.
