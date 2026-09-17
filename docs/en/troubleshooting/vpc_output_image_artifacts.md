# Artifacts or Green Edges in VPC Output Images

## Symptom

Artifacts or green edges occur on the output image.

The following figure shows an example. A green edge exists on the right of the image.

![](figures/image_0000001927915733.png)

## Possible Cause

1. Due to hardware restrictions, the VPC has alignment requirements on the width and height of the output image. The alignment requirements of different hardware versions may vary. The green edge may be invalid alignment data. For example, if the VPC requires that the width of the output image be 16-pixel aligned, but the width of the current output image is 100, which does not meet the 16-pixel alignment requirement, you need to configure the width to an aligned size, for example, 128. In this case, the extra 28 is invalid alignment data, causing green edges in the output image.
2. If the size of the cropped and resized image is different from that of the output image \(as shown in the following figure\), the blue edges in the base image may be random values from the output memory, which will cause artifacts.

    ![](figures/image_crop_paste.png)

## Solution

1. Check the width of the output image and the width of the output image after alignment configured in the code. If the green edges are aligned data, you need to write the file line by line based on the width of the output image and delete the aligned data.

    For details, see the sample code in  [vpc\_sample](https://gitee.com/ascend/samples/tree/master/cplusplus/level1_single_api/7_dvpp/vpc_sample).

2. If the size of the cropped and resized image is different from that of the output image, check whether  **memset\_s**  has been performed in the output memory in advance. Initialize the memory to eliminate the impact of random values.
