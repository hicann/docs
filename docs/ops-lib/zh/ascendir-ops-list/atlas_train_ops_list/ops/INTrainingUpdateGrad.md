# INTrainingUpdateGrad

```c
REG_OP(INTrainingUpdateGrad)
    .INPUT(dy, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(variance, TensorType({DT_FLOAT}))
    .INPUT(mean, TensorType({DT_FLOAT}))
    .OUTPUT(res_gamma, TensorType({DT_FLOAT}))
    .OUTPUT(res_beta, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(INTrainingUpdateGrad)
```

## Brief

The first (reduce-over-spatial) stage of InstanceNorm training backward.
For each (N, C) instance it normalizes x with the given mean/variance and reduces
dy*x_norm and dy over the spatial dimensions (keepdims). It does NOT reduce over N
(that is the job of the downstream op INTrainingUpdateGradGammaBeta).

## Inputs

Four inputs, including:
- dy: A tensor with the full spatial dims. Must be one of the following types: float16, float32.
6D with format NDC1HWC0.
- x: A tensor with the same dtype/format/shape as dy.
- variance: An NDC1HWC0 tensor of type float32, per-instance variance, spatial dims are 1.
- mean: An NDC1HWC0 tensor of type float32, per-instance mean, spatial dims are 1.

## Outputs

Two outputs, including:
- res_gamma: An NDC1HWC0 tensor of type float32, equals sum_over_spatial(dy * x_norm), spatial dims are 1.
- res_beta: An NDC1HWC0 tensor of type float32, equals sum_over_spatial(dy), spatial dims are 1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: float16,float32
- input1 x: float16,float32
- input2 variance: float32
- input3 mean: float32
- output0 res_gamma: float32
- output1 res_beta: float32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
