# Uniform

```c
REG_OP(Uniform)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .ATTR(from, Float, 0.0)
    .ATTR(to, Float, 1.0)
    .OP_END_FACTORY_REG(Uniform)
```

## Brief

: Fill the input tensor with values drawn from the uniform distribution U(from, to). 

## Inputs

x: A Tensor. Must be one of the following types: float16, float, double. 

## Outputs

y: A Tensor has the same type as x. 

## Attributes

- from: The lower bound of the uniform. Defaults: 0.0
- to: The upper bound of the uniform. Defaults: 1.0


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
