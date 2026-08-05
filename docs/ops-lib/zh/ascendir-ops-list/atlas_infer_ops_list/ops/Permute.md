# Permute

```c
REG_OP(Permute)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(order, ListInt, {0})
    .OP_END_FACTORY_REG(Permute)
```

## Brief

Permutes the dimensions according to order.
The returned tensor's dimension i will correspond to the input dimension order[i] . 

## Inputs

x: A ND tensor. Support 4D. Must be one of the following types: float16, float32 . 

## Outputs

y: A ND tensor. Support 4D. Has the same type as "x".

## Attributes

order: A permutation of the dimensions of "x".Type must be int32.Support any axis transformation.Defaults to "{0}"

## Attention Constraints

The Attributes order must ensure that the provided dimensions are unique,do not repeat, and cover all dimensions of
"x". 


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
