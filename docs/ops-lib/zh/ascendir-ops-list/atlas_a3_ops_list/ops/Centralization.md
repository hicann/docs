# Centralization

```c
REG_OP(Centralization)
    .INPUT(x, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .OUTPUT(y, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .ATTR(axes, ListInt, {-1})
    .OP_END_FACTORY_REG(Centralization)
```

## Brief

Computes Centralization. result = x - mean(x, axes)

## Inputs

 x: An ND tensor of type float16, float32.

## Outputs

y: A Tensor. Has the same type as "x". 

## Attributes

axes: The dimensions to reduce. Must be one of the following types: int, list, tuple, NoneType, default: -1.
Must be in the range [-rank(x), rank(x)).

## Third-party framework compatibility

custom operator 


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
