# SpatialTransformerD

```c
REG_OP(SpatialTransformerD)
    .INPUT(x, TensorType({DT_FLOAT,DT_FLOAT16}))
    .OPTIONAL_INPUT(theta, TensorType({DT_FLOAT,DT_FLOAT16}))
    .OUTPUT(y, TensorType({DT_FLOAT,DT_FLOAT16}))
    .ATTR(output_size, ListInt, {-1, -1})
    .ATTR(default_theta, ListFloat, {})
    .ATTR(align_corners, Bool, false)
    .ATTR(use_default_theta, ListBool, {})
    .OP_END_FACTORY_REG(SpatialTransformerD)
```

## Brief

Function spatial transformer . 

## Inputs

- x: A Tensor dtype of float16, float32.
- theta: A Tensor dtype of float16, float32, auxiliary coefficients .

## Outputs

y: A Tensor dtype of float16, float32, should be same shape and type as x.

## Attributes

- output_size: A tuple output size.
- default_theta: A tuple default theta
- use_default_theta: List use default theta
- align_corners: Align corners

## Attention Constraints

The operator will not be enhanced in the future.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
