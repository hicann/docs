# ReduceStd

```c
REG_OP(ReduceStd)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(y1, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(y2, TensorType({DT_FLOAT, DT_FLOAT16}))
    .ATTR(dim, ListInt, {})
    .ATTR(unbiased, Bool, true)
    .ATTR(keepdim, Bool, false)
    .OP_END_FACTORY_REG(ReduceStd)
```

## Brief

Calculates the standard deviation and average value of Tensors.

## Inputs

x: A Tensor. Must be one of the following types:
    float16, float32. 

## Outputs

Two Outputs, including:
- y1: A Tensor. Has the same type as "x".
- y2: A Tensor. Has the same type as "x".

## Attributes

Three Attributes, including:
- dim: An optional listint, Defaults to "[]".
- unbiased: An optional bool. Defaults to "True".
    If "True", Use Bessel Correction.
    If "False", Do not use Bessel Correction. 
- keepdim: An optional bool. Defaults to "False".
    If "True", Keep the original tensor dimension.
    If "False", Do not keep the original tensor dimension. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y1: float16,float32
- output1 y2: float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator ReduceStd.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
