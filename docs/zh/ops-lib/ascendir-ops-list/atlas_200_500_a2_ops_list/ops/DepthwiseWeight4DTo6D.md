# DepthwiseWeight4DTo6D

```c
REG_OP(DepthwiseWeight4DTo6D)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_UINT16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_UINT16}))
    .OP_END_FACTORY_REG(DepthwiseWeight4DTo6D)
```

## Brief

Convert tensor format from HWCN to C1HWNCoC0 . 

## Inputs

x: A Tensor. Must be 4D Tensor of type float16, float32, int32, uint16, with format HWCN . 

## Outputs

y: A 6D Tensor. Has the same type as "x", with format C1HWNCoC0. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int32,uint16
- output0 y: float16,float32,int32,uint16

## Attention Constraints

THIS OPERATOR IS DEPRECATED. It will be removed in a future version.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
