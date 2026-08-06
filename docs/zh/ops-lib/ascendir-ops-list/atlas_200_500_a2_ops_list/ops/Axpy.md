# Axpy

```c
REG_OP(Axpy)
    .INPUT(x1, TensorType({DT_FLOAT, DT_INT32, DT_FLOAT16, DT_BF16}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_INT32, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_INT32, DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(alpha, Float)
    .OP_END_FACTORY_REG(Axpy)
```

## Brief

Add tensor with scale y = x1 + x2*alpha. Support broadcasting operations.

## Inputs

- x1: A ND Tensor dtype of int32, float16, float32, bfloat16.
- x2: A ND Tensor dtype of int32, float16, float32, bfloat16.

## Outputs

y: A ND Tensor. should be broadcast shape of x1 and x2. 

## Attributes

alpha: a float required attr, apply to x2:x2*alpha

## Third-party framework compatibility

Compatible with the PyTorch operator Axpy.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
