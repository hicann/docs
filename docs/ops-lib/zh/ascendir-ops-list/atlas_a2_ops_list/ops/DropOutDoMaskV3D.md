# DropOutDoMaskV3D

```c
REG_OP(DropOutDoMaskV3D)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(mask, TensorType({DT_UINT8, DT_BOOL}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(keep_prob, Float)
    .OP_END_FACTORY_REG(DropOutDoMaskV3D)
```

## Brief

Return "output" according to the algorithm of dropout_do_mask_v3_d:  
 scale_x = x *(1 / keep_prob)  
 output = select(mask == 1, scale_x, 0)  

## Inputs

Two inputs, including:
- x: A mutable Tensor. A ND tensor. Support 1D ~ 8D. Must be one of the following types:
    float16, float32, bfloat16.
- mask: A mutable Tensor. A ND tensor. Must met all of the following rules:
    shape of mask should be 1D.
    dtype of mask should be uint8 or bool.
    value of shape should met the following algorithm:
    value = value = ((size(x) + 127) / 128) * 128 / 8.

## Outputs

y: A mutable Tensor. Has the same type, shape and format as "x".

## Attributes

- keep_prob: A required Float attribute. Must satisfy 0 <= keep_prob <= 1.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
