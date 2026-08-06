# IMGWarpOffsets

```c
REG_OP(IMGWarpOffsets)
    .INPUT(images, TensorType({DT_UINT8, DT_FLOAT16, DT_FLOAT}))
    .INPUT(offsets, TensorType({DT_FLOAT, DT_INT32}))
    .OUTPUT(warp_images, TensorType({DT_UINT8, DT_FLOAT16, DT_FLOAT}))
    .OP_END_FACTORY_REG(IMGWarpOffsets)
```

## Brief

This operation select images to warp_images according to offsets.

## Inputs

- images: 4-D Tensor with shape [batch, height, width, 3].
- offsets: 4-D Tensor with shape [batch, 4, new_height, new_width].

## Outputs

warp_images: Returns 5-D Tensor with shape
[batch, 4, new_height, new_width, 3] and the same dtype as images.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 images: float16,float32,uint8
- input1 offsets: float32,int32
- output0 warp_images: float16,float32,uint8

## Attention Constraints

When input dtype of offsets is int32, images should be float16.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
