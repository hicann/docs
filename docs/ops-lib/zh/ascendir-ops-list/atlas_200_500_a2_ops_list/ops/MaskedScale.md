# MaskedScale

```c
REG_OP(MaskedScale)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT32}))
    .INPUT(mask, TensorType({DT_INT8, DT_FLOAT16, DT_FLOAT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT32}))
    .REQUIRED_ATTR(value, Float)
    .OP_END_FACTORY_REG(MaskedScale)
```

## Brief

Calculates x * maske * value.

## Inputs

- x: An tensor of type float16 or float32, specifying the input to the data layer.
- mask: An tensor of type int8 or float16 or float32, be same shape with x.

## Outputs

y: The output tensor of type float16 or float32. Same dtype and shape as x.

## Attributes

value: An optional float, default value is 1.0. 


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
