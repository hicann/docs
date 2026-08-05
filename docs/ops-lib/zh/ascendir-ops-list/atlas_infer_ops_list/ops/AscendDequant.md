# AscendDequant

```c
REG_OP(AscendDequant)
    .INPUT(x, TensorType({DT_INT32}))
    .INPUT(deq_scale, TensorType({DT_FLOAT16, DT_UINT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(sqrt_mode, Bool, false)
    .ATTR(relu_flag, Bool, false)
    .ATTR(dtype, Int, DT_FLOAT)
    .OP_END_FACTORY_REG(AscendDequant)
```

## Brief

Dequantizes the input.

## Inputs

- x: A tensor of type int32, specifying the input. Shape support 1D ~ 8D.
The format must be FRACTAL_NZ, NC1HWC0 or NDC1HWC0.
- deq_scale: A required Tensor. Must be one of the following types: float16,
uint64. The format must be NC1HWC0 or NDC1HWC0. If deq_scale is 1D tensor,
shape must be same as the last dimension of x. Otherwise the number of
dimensions should be equal to x, the last dimension of shape should be
the same as x, others must be 1. 

## Outputs

y: The dequantized output tensor of type float16 or float32. The format must
be FRACTAL_NZ, NC1HWC0 or NDC1HWC0. The shape is same as x. 

## Attributes

- sqrt_mode: An optional bool, specifying whether to perform square root
on "scale", either "True" or "False". Defaults to "False".
- relu_flag: An optional bool, specifying whether to perform ReLU,
either "True" or "False". Defaults to "False".
- dtype: An optional int32, specifying the output data type. Defaults to "0"
, represents dtype "DT_FLOAT". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: int32
- input1 deq_scale: uint64
- output0 y: float16

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
