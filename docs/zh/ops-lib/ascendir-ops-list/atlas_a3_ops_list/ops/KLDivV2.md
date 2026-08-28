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

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 target: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the PyTorch operator kl_div_v2.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
