# KLDivV2

```c
REG_OP(KLDivV2)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .INPUT(target, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .ATTR(reduction, String, "mean")
    .ATTR(log_target, Bool, false)
    .OP_END_FACTORY_REG(KLDivV2)
```

## Brief

Kullback-Leibler divergence.

## Inputs

Two inputs, including:
- x: Tensor of arbitrary shape. Must be the type of following types: bfloat16, float16, float32.
- target: Tensor of the same shape and dtype as x.

## Outputs

y: A ND Tensor of the same dtype as x.

## Attributes

reduction: An optional "string", Specifies the reduction to apply to the output;
Reduction supports the modes of "sum" and "mean", default value is "mean". 
log_target: An optional bool, a flag indicating whether target is passed in the log space. Default value is false. 

## Third-party framework compatibility

Compatible with the PyTorch operator kl_div_v2.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
