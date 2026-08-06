# AscendRequant

```c
REG_OP(AscendRequant)
    .INPUT(x, TensorType({DT_INT32}))
    .INPUT(req_scale, TensorType({DT_UINT64}))
    .OUTPUT(y, TensorType({DT_INT8}))
    .ATTR(relu_flag, Bool, false)
    .OP_END_FACTORY_REG(AscendRequant)
```

## Brief

Requantizes the input.

## Inputs

- x: A tensor of type int32, specifying the input. The format must be
FRACTAL_NZ, NC1HWC0 or DNC1HWC0. Shape support 4D ~ 6D.
- req_scale:A required Tensor. The type only support uint64. The format
must be NC1HWC0 or NDC1HWC0. If req_scale is 1D tensor, shape must be same as
the last dimension of x. Otherwise the number of dimensions should be equal to
x, the last dimension of shape should be same as x, others must be 1.
Shape support 5D ~ 6D. Shape must be 1 in n,d,h,w. 

## Outputs

y: The dequantized output tensor of type int8. The format must be FRACTAL_NZ,
NC1HWC0 or NDC1HWC0. The shape is same as x. 

## Attributes

relu_flag: An optional bool, specifying whether to perform ReLU,
either "True" or "False". Defaults to "False" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: int32
- input1 req_scale: uint64
- output0 y: int8

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
