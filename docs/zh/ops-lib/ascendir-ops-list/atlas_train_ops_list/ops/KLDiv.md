# KLDiv

```c
REG_OP(KLDiv)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .INPUT(target, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .REQUIRED_ATTR(reduction, String)
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .OP_END_FACTORY_REG(KLDiv)
```

## Brief

Kullback-Leibler divergence.

## Inputs

Two inputs, including:
- x: Tensor with one of the following types: float16, float32, double, bfloat16. Support 1D ~ 8D. Support format:
["ND", "NC1HWC0", "FRACTAL_Z", "HWCN", "FRACTAL_NZ", "C1HWNCoC0"].
- target: Tensor of the same shape and format and dtype as x. Support 1D ~ 8D. Support format:
["ND", "NC1HWC0", "FRACTAL_Z", "HWCN", "FRACTAL_NZ", "C1HWNCoC0"]. 

## Outputs

y: A ND Tensor of the same dtype as x, output shape=[1,], when reduction='sum' or 'batchmean'.
when reduction='none', output y is a tensor, Support 1D ~ 8D. Must have the same type, shape and format as input "x".

## Attributes

reduction: An required "string", Specifies the reduction to apply to the output;
Reduction supports the three modes of "sum" and "batchmean" and "none". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 target: float16,float32
- output0 y: float16,float32

## Attention Constraints

Warning: This operator will not be enhanced in the future. Please use KLDivV2 instead.

## Third-party framework compatibility

Compatible with the PyTorch operator kl_div.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
