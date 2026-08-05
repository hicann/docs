# DepthwiseWeight6DTo4D

```c
REG_OP(DepthwiseWeight6DTo4D)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_UINT16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_UINT16}))
    .ATTR(channel_size, Int, 16)
    .OP_END_FACTORY_REG(DepthwiseWeight6DTo4D)
```

## Brief

Convert tensor format from C1HWNCoC0 to HWCN . 

## Inputs

x: A Tensor. Must be 6D Tensor of type float16, float32, int32, uint16, with format C1HWNCoC0 . 

## Outputs

y: A 4D Tensor. Has the same type as "x", with format HWCN. 

## Attributes

channel_size: An optional int, specifying the channel size of 4D Tensor with format HWCN . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int32,uint16
- output0 y: float16,float32,int32,uint16

## Attention Constraints

THIS OPERATOR IS DEPRECATED. It will be removed in a future version.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
