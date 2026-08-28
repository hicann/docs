# AvgPool1D

```c
REG_OP(AvgPool1D)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(ksize, Int)
    .REQUIRED_ATTR(strides, Int)
    .REQUIRED_ATTR(pads, ListInt)
    .ATTR(ceil_mode, Bool, false)
    .ATTR(count_include_pad, Bool, false)
    .OP_END_FACTORY_REG(AvgPool1D)
```

## Brief

Performs AvgPool1D on the input .

## Inputs

x: A Tensor. Must be one of the following types: float16, float32 . Supported format "NC1HWC0" . 

## Outputs

y: A Tensor. Has the same type as x . Supported format "NC1HWC0" . 

## Attributes

- ksize: An required int, specifying the size of the window.
- strides: An required int.
- pads: A required tuple or list.
- ceil_mode: An optional bool. Defaults to False.
- count_include_pad: An optional bool. Defaults to False .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

- compatible with pytorch AvgPool1D operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
