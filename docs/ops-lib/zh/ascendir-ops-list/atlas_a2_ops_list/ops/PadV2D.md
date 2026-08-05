# PadV2D

```c
REG_OP(PadV2D)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .INPUT(constant_values, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .REQUIRED_ATTR(paddings, ListListInt)
    .OP_END_FACTORY_REG(PadV2D)
```

## Brief

Pad a tensor .

## Inputs

- x: A Tensor. Must be one of the following types: float16, float32, int32 .
- constant_values: A Tensor. Must have the same type as input.

## Outputs

y: A Tensor of the same type as "x" . 

## Attributes

paddings: A required Attribute.
    For each dimension D of input, paddings[D, 0] indicates how many
    values to add before the contents of tensor in that dimension,
    and paddings[D, 1] indicates how many values to add after the
    contents of tensor in that dimension . 

## Attention Constraints

The operator will not be enhanced in the future.

## Third-party framework compatibility

Compatible with TensorFlow operator PadV2.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
