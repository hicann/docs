# SyncResizeBilinearV2

```c
REG_OP(SyncResizeBilinearV2)
    .INPUT(x, TensorType({DT_FLOAT}))
    .INPUT(size, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .ATTR(ori_image_size, ListInt, {})
    .ATTR(split_size, ListInt, {})
    .ATTR(src_start_w, Int, 0)
    .ATTR(dst_start_w, Int, 0)
    .ATTR(align_corners, Bool, false)
    .ATTR(half_pixel_centers, Bool, false)
    .OP_END_FACTORY_REG(SyncResizeBilinearV2)
```

## Brief

Resize images to size using bilinear interpolation . 

## Inputs

Input images must be a 4-D tensor. Inputs include:
- x: 4-D float32 tensor. Must set the format, supported format NC1HWC0.
- size: A 1-D int32 Tensor of 2 elements: new_height, new_width. The new
size for the images. 

## Outputs

y: 4-D with shape [batch, new_height, new_width, channels].
Must be one of the following types: float. The format support NC1HWC0. 

## Attributes

- align_corners: Bool type. If true, the centers of the 4 corner pixels of the input and
output tensors are aligned, preserving the values at the corner pixels.
Defaults to false.
- half_pixel_centers: An optional bool. Defaults to False .
- ori_image_size: An optional listint. Defaults to [].
- split_size: An optional listint. Defaults to [].
- src_start_w: An optional int. Defaults to 0.
- dst_start_w: An optional int. Defaults to 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- input1 size: int32
- output0 y: float32

## Attention Constraints

Input images can be of different types but output images are always float . 

## Third-party framework compatibility

Compatible with mindspore ResizeBilinearV2 operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
