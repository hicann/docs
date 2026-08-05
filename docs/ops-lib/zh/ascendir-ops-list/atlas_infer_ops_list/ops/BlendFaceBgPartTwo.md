# BlendFaceBgPartTwo

```c
REG_OP(BlendFaceBgPartTwo)
    .INPUT(acc_face, TensorType({DT_FLOAT}))
    .INPUT(acc_mask, TensorType({DT_FLOAT}))
    .INPUT(max_mask, TensorType({DT_FLOAT}))
    .INPUT(bg_img, TensorType({DT_UINT8, DT_FLOAT}))
    .OUTPUT(fused_img, TensorType({DT_FLOAT}))
    .ATTR(epsilon, Float, 1e-12f)
    .OP_END_FACTORY_REG(BlendFaceBgPartTwo)
```

## Brief

Blend face iamge to the backgroud Part Two.

## Inputs

- acc_face: A 3D Tensor, format is ND, dtype is float32, shape is (H, W, 3).
- acc_mask: A 3D Tensor, format is ND, dtype is float32, shape is (H, W, 3).
- max_mask: A 3D Tensor, format is ND, dtype is float32, shape is (H, W, 3).
- bg_img: A 3D Tensor, format is ND, dtype is float32 or uint8, shape is (H, W, 3), the input background image.

## Outputs

- fused_img: A 3D Tensor, format is ND. It has the same type and shape as input "acc_face".

## Attributes

- epsilon: A scalar of the same type as "var".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 acc_face: float32
- input1 acc_mask: float32
- input2 max_mask: float32
- input3 bg_img: float32,uint8
- output0 fused_img: float32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
