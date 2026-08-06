# ReduceVar

```c
REG_OP(ReduceVar)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(var, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(mean, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(dim, ListInt, {})
    .ATTR(correction, Int, 1)
    .ATTR(keepdim, Bool, false)
    .ATTR(is_mean_out, Bool, true)
    .OP_END_FACTORY_REG(ReduceVar)
```

## Brief

Calculates the variance and average value of tensors.

## Inputs

x: A tensor. Format supports ND. Must be one of the following types: float32, float16, bfloat16. 

## Outputs

Two Outputs, including:
- var: A tensor, the variance of x. Has the same type and format as "x".
- mean: A tensor, the mean of x. Has the same type and format as "x".

## Attributes

Four Attributes, including:
- dim: The dimensions to reduce. An optional listint, Defaults to "None".
    If None (the default), reduces all dimensions.
    Must be in the range [-rank(x), rank(x)).
- correction: An optional int. Used for Bessel's correction. Defaults to 1.
- keepdim: An optional bool. Defaults to "False".
    If "True", Keep the original tensor dimension.
    If "False", Do not keep the original tensor dimension.
- is_mean_out: An optional bool. Defaults to "True".
    If "True", Output the mean.
    If "False", Do not output the mean. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 var: bfloat16,float16,float32
- output1 mean: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator var and var_mean.


---

[Back to Operator Specifications (Ascend950)](../README.md)
