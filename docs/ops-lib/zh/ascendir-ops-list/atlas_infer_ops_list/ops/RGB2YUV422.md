# RGB2YUV422

```c
REG_OP(RGB2YUV422)
    .INPUT(rgb, TensorType({DT_UINT8}))
    .OUTPUT(yuv, TensorType({DT_UINT8}))
    .OP_END_FACTORY_REG(RGB2YUV422)
```

## Brief

RGB2YUV422. Convert the image from rgb to yuv422.

## Inputs

rgb: A 3D Tensor of dtype uint8 with shape (H, W, 3).
The value of W is a multiple of 16. 

## Outputs

yuv: A 3D Tensor of dtype uint8 with shape (H, W, 2).
The value of H and W are same as rgb. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 rgb: uint8
- output0 yuv: uint8

## Attention Constraints

Input images is a tensor of 3 dimensions. The last dimension is
interpretted as channels, and must be three . 


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
