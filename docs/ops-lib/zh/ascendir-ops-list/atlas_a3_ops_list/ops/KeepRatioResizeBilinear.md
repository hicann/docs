# KeepRatioResizeBilinear

```c
REG_OP(KeepRatioResizeBilinear)
    .INPUT(images, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(min_dimension, Int)
    .REQUIRED_ATTR(max_dimension, Int)
    .ATTR(align_corners, Bool, false)
    .ATTR(half_pixel_centers, Bool, false)
    .OP_END_FACTORY_REG(KeepRatioResizeBilinear)
```

## Brief

Resizes "images" to "size" using bilinear interpolation and keep ratio at the time. 

## Inputs

One input:
images: A Tensor.
Must be one of the following types: float16, float32. Shape must be 4D.
The format only support NHWC or NCHW. 

## Outputs

y: A Tensor with type float32 and the same format as input "images".
The format only support NHWC or NCHW. Shape must be 4D.
Shape has the same value as x in n,c. 

## Attributes

- min_dimension: A required int32 attribute for the min dimension for the images.
No default value.
- max_dimension: A required int32 attribute for the max dimension for the images.
No default value.
- align_corners: An optional bool. If "true", the centers of the corner
pixels of the input and output tensors are aligned. Defaults to "false".
- half_pixel_centers: indicates if the offset coordinates are normalized
Defaults to "false". 

## Attention Constraints

The input "images" must be a tensor of 5 elements: images[2] <= 2048,
images[3] <= 2048.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
