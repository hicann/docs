# BlendFaceBgPartOne

```c
REG_OP(BlendFaceBgPartOne)
    .INPUT(face_img, TensorType({DT_UINT8, DT_FLOAT}))
    .INPUT(face_rect, TensorType({DT_INT32}))
    .INPUT(face_mask, TensorType({DT_FLOAT}))
    .INPUT(acc_face, TensorType({DT_FLOAT}))
    .INPUT(acc_mask, TensorType({DT_FLOAT}))
    .INPUT(max_mask, TensorType({DT_FLOAT}))
    .OUTPUT(acc_face, TensorType({DT_FLOAT}))
    .OUTPUT(acc_mask, TensorType({DT_FLOAT}))
    .OUTPUT(max_mask, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(BlendFaceBgPartOne)
```

## Brief

Blend face iamge to the backgroud.

## Inputs

- face_img: A 3D Tensor, format is ND, dtype is uint8 or float32, shape is (H, W, 3). The input face image.
- face_rect: A 1D Tensor, format is ND, dtype is int32, shape is (4,). The coordinates of the face image in the backgroud.
- face_mask: A 3D Tensor, format is ND, dtype is float32, shape is (H, W, 1).
- acc_face: A 3D Tensor, format is ND, dtype is float32, shape is (H, W, 3).
- acc_mask: A 3D Tensor, format is ND, dtype is float32, shape is (H, W, 3).
- max_mask: A 3D Tensor, format is ND, dtype is float32, shape is (H, W, 3).

## Outputs

- acc_face: A 3D Tensor, format is ND. It has the same type and shape as input "acc_face".
- acc_mask: A 3D Tensor, format is ND. It has the same type and shape as input "acc_mask".
- max_mask: A 3D Tensor, format is ND. It has the same type and shape as input "max_mask".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 face_img: float32,uint8
- input1 face_rect: int32
- input2 face_mask: float32
- input3 acc_face: float32
- input4 acc_mask: float32
- input5 max_mask: float32
- output0 acc_face: float32
- output1 acc_mask: float32
- output2 max_mask: float32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
