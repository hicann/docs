# Correlation

```c
REG_OP(Correlation)
    .INPUT(filter, TensorType({DT_FLOAT16, DT_INT8}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_INT8}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_INT32}))
    .ATTR(groups, Int, 1)
    .OP_END_FACTORY_REG(Correlation)
```

## Brief

Computes a 2D Correlation given 4D "x" and "filter" tensors.

## Inputs

- filter: A 4D tensor of filters.
- x: A 4D tensor of input images, batch number must equal to batch
number of "filter", and channel must equal to channel of "filter".

## Outputs

y: A Tensor. Has the same type as "x".

## Attributes

- groups: set correlation mode, must be 1 or channel.

## Third-party framework compatibility

Compatible with caffe correlation custom operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
