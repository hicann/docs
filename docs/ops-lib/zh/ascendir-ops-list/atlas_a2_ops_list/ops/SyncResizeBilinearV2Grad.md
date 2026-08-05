# SyncResizeBilinearV2Grad

```c
REG_OP(SyncResizeBilinearV2Grad)
    .INPUT(grads, TensorType({DT_FLOAT}))
    .INPUT(original_image, TensorType::FloatingDataType())
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .ATTR(size, ListInt, {})
    .ATTR(ori_image_size, ListInt, {})
    .ATTR(src_start_w, Int, 0)
    .ATTR(dst_start_w, Int, 0)
    .ATTR(align_corners, Bool, false)
    .ATTR(half_pixel_centers, Bool, false)
    .OP_END_FACTORY_REG(SyncResizeBilinearV2Grad)
```

## Brief

Computes the gradient of bilinear interpolation . 

## Inputs

Two inputs, including:
- grads: A 5D tensor of type float32. Must set the format, supported format NC1HWC0.
- original_image: A 5D tensor of type float32. Must set the format, supported format NC1HWC0.
The image tensor that was resized. 

## Outputs

y: A 5D Tensor of type float32. The format support NC1HWC0.
Has the same type as original_image. 

## Attributes

- size: An optional listint. Defaults to [].
- ori_image_size: An optional listint. Defaults to [].
- src_start_w: An optional int. Defaults to 0.
- dst_start_w: An optional int. Defaults to 0.
- align_corners: An optional bool. Defaults to False. If true, the centers of
the 4 corner pixels of the input and grad tensors are aligned. Defaults to
false .
- half_pixel_centers: Bool type, indicates if the offset coordinates are normalized. Defaults
to false . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: float32
- input1 original_image: float32
- output0 y: float32

## Attention Constraints

Input grads must be a 5D tensor. 

## Third-party framework compatibility

Compatible with mindspore ResizeBilinearV2Grad operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
