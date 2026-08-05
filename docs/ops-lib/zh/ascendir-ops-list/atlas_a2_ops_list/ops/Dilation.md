# Dilation

```c
REG_OP(Dilation)
    .INPUT(x, TensorType({DT_INT8, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_INT8, DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(dilations, ListInt)
    .ATTR(pads, ListInt, {})
    .ATTR(padding_value, Float, 0.0)
    .OP_END_FACTORY_REG(Dilation)
```

## Brief

Computes the deformed dilation output with the expected input

## Inputs

One inputs:
x: A Tensor of type int8, float16, float32 with format NCHW.

## Outputs

y: A Tensor. A Tensor with the same type and format as input x.

## Attributes

- dilations: Controls the spacing between the input x. A required tuple/list of integers with format NCHW.
- pads: Controls the amout of padding applied to the input. A optional tuple/list of integers. Defaults to [].
- padding_value: A optional float32 value. default value filling in blank. Defaults to 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int8
- output0 y: bfloat16,float16,float32,int8


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
