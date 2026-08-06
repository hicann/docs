# AddLayerNormGrad

```c
REG_OP(AddLayerNormGrad)
    .INPUT(dy, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(x1, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(x2, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(rstd, ge::TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .INPUT(mean, ge::TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .INPUT(gamma, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(dsum, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(dx, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(dgamma, ge::TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .OUTPUT(dbeta, ge::TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .OP_END_FACTORY_REG(AddLayerNormGrad)
```

## Brief

AddLayerNormGrad operator interface implementation.

## Inputs

- dy: Main grad input.
    A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- x1: Input x1 of the forward fused operator.
    A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- x2: Input x2 of the forward fused operator.
    A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- rstd: Rstd of the sum of forward inputs x1 and x2.
    A Tensor. Support dtype: [float32], support format: [ND].
- mean: Mean of the sum of forward inputs x1 and x2.
    A Tensor. Support dtype: [float32], support format: [ND].
- gamma: Describing the weight.
    A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- dsum: Other grad input.
     A optional input Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].

## Outputs

- dx: The gradient of input "x", Has the same type and shape as "x".
    A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- dgamma: The gradient of input "gamma", Has the same type and shape as "gamma".
    A Tensor. Support dtype: [float32], support format: [ND].
- dbeta: The gradient of input "beta", Has the same type and shape as "beta".
    A Tensor. Support dtype: [float32], support format: [ND].

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: float16,float32
- input1 x1: float16,float32
- input2 x2: float16,float32
- input3 rstd: float32
- input4 mean: float32
- input5 gamma: float16,float32
- input6 dsum: float16,float32
- output0 dx: float16,float32
- output1 dgamma: float32
- output2 dbeta: float32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
