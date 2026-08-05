# AscendDequantS16

```c
REG_OP(AscendDequantS16)
    .INPUT(x0, TensorType({DT_INT32}))
    .INPUT(deq_scale, TensorType({DT_UINT64}))
    .OPTIONAL_INPUT(x1, TensorType({DT_INT16}))
    .OUTPUT(y, TensorType({DT_INT16}))
    .ATTR(relu_flag, Bool, false)
    .OP_END_FACTORY_REG(AscendDequantS16)
```

## Brief

Dequantizes the input of int16 . 

## Inputs

- x0: A tensor of type int32, specifying the input.
The format support NC1HWC0, FRACTAL_NZ. Shape support 4D ~ 8D.
- deq_scale: A tensor of type uint64, specifying the scaling ratio.
The format support NC1HWC0. Shape support 5D, must be 1 in n, h, w.
- x1: A tensor of type int16, specifying the input.
The format support NC1HWC0, ND. Shape support 1D or 5D.
When the format of x1 is ND, the shape length of x1 must be 1. 

## Outputs

y: The dequantized output tensor of type int16.
The format support NC1HWC0, FRACTAL_NZ. Shape support 4D ~ 8D.
The shape and format are the same as input "x0". 

## Attributes

relu_flag: An optional bool, specifying whether to perform ReLU,
either "True" or "False". Defaults to "False" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x0: int32
- input1 deq_scale: uint64
- input2 x1: int16
- output0 y: int16

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
