# ReduceStdWithMean

```c
REG_OP(ReduceStdWithMean)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(mean, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(dim, ListInt, {})
    .ATTR(unbiased, Bool, true)
    .ATTR(keepdim, Bool, false)
    .ATTR(invert, Bool, false)
    .ATTR(epsilon, Float, 0.001)
    .ATTR(correction, Int, 1)
    .OP_END_FACTORY_REG(ReduceStdWithMean)
```

## Brief

Calculates the standard deviation of Tensors.

## Inputs

include:
- x: A tensor. Must be one of the following types: float16, float32, bfloat16.
The format must be NCHW, NHWC, or ND. 
- mean: A tensor. It's the mean of X. Has the same shape, format and type as "x".

## Outputs

y: A tensor. It's the variance of X or reciprocal of vaiance of X. Has the same type and format as "x".

## Attributes

Six Attributes, including:
- dim: The dimensions to reduce. An optional listint, Defaults to "None".
    If None (the default), reduces all dimensions.
    Must be in the range [-rank(x), rank(x)). 
- unbiased: An optional bool. Defaults to "True".
    If "True", Use Bessel Correction.
    If "False", Do not use Bessel Correction. 
- keepdim: An optional bool. Defaults to "False".
    If "True", Keep the original tensor dimension.
    If "False", Do not keep the original tensor dimension. 
- invert: An optional bool, Defaults to "False".
    If "True", the output is inverse of variance.
    If "False", the output is variance.
- epsilon: An optional float, Defaults to 0.001.
    Prevent division by 0.
- correction: An optional int. Defaults to 1.
    If unbiased is "True", use Bessel Correction. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 mean: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator ReduceStdWithMean.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
