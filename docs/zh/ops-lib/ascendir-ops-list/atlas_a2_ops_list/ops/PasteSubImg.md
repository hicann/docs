# PasteSubImg

```c
REG_OP(PasteSubImg)
    .INPUT(patch_img, TensorType({DT_UINT8, DT_FLOAT16, DT_FLOAT32}))
    .INPUT(patch_coord, TensorType({DT_INT32}))
    .INPUT(core_area_coord, TensorType({DT_INT32}))
    .INPUT(combine_img, TensorType({DT_UINT8, DT_FLOAT16, DT_FLOAT32}))
    .OUTPUT(combine_img, TensorType({DT_UINT8, DT_FLOAT16, DT_FLOAT32}))
    .REQUIRED_ATTR(scale, Float)
    .OP_END_FACTORY_REG(PasteSubImg)
```

## Brief

paste sub img.

## Inputs

- patch_img: A 3D Tensor, format is ND, dtype is uint8 or float16 or float32,
shape is (H, W, C). The input image.
- patch_coord: A 1D Tensor, format is ND, dtype is int32, shape is (4,). The coordinates
in the combined img.
- core_area_coord: A 1D Tensor, format is ND, dtype is int32, shape is (4,). The
coordinates in the patch img
- combine_img: A 3D Tensor, format is ND, dtype is uint8 or float16 or float32, shape is
(H, W, C). 

## Outputs

- combine_img: A 3D Tensor, format is ND. It has the same type and shape as input
"combine_img". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 patch_img: float16,float32,uint8
- input1 patch_coord: int32
- input2 core_area_coord: int32
- input3 combine_img: float16,float32,uint8
- output0 combine_img: float16,float32,uint8

## Attr

- scale: A required float, scale of coordinates.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
