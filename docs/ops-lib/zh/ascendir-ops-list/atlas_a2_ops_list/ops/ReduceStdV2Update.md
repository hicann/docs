# ReduceStdV2Update

```c
REG_OP(ReduceStdV2Update)
    .INPUT(x, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(mean, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(output_var, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(dim, ListInt)
    .ATTR(if_std, Bool, false)
    .ATTR(unbiased, Bool, true)
    .ATTR(keepdim, Bool, false)
    .ATTR(correction, Int, 1)
    .OP_END_FACTORY_REG(ReduceStdV2Update)
```

## Brief

Calculates the standard deviation or the variance of Tensors with the average value.

## Inputs

Two inputs, including:
- x: A Tensor. Must be one of the following types: float16, float32, bfloat16.
- mean: A Tensor. It's the mean of X. Has the same shape and type as "x"

## Outputs

- output_var: A Tensor. It's the standard deviation or the variance of X. Has the same type as "x".

## Attributes

Five Attributes, including:
- dim: The dimensions to reduce. A required listint.
    Must be in the range [-rank(x), rank(x)).
- if_std: An optional bool. Defaults to "False".
    If "True", Calculate the standard deviation
    If "False", Calculate the variance
- unbiased: An optional bool. Defaults to "True".
    If "True", Use Bessel Correction.
    If "False", Do not use Bessel Correction. 
- keepdim: An optional bool. Defaults to "False".
    If "True", Keep the original tensor dimension.
    If "False", Do not keep the original tensor dimension. 
- correction: An optional int. Defaults to 1.
    If unbiased is "True", use Bessel Correction. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 mean: bfloat16,float16,float32
- output0 output_var: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator Var_mean.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
