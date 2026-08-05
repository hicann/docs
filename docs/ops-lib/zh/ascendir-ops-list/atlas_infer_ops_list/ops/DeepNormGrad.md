# DeepNormGrad

```c
REG_OP(DeepNormGrad)
    .INPUT(dy, TensorType({DT_FLOAT,DT_FLOAT16,DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT,DT_FLOAT16,DT_BF16}))
    .INPUT(gx, TensorType({DT_FLOAT,DT_FLOAT16,DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT,DT_FLOAT16,DT_BF16}))
    .INPUT(mean, TensorType::({DT_FLOAT}))
    .INPUT(rstd, TensorType::({DT_FLOAT}))
    .OUTPUT(dx, TensorType({DT_FLOAT,DT_FLOAT16,DT_BF16}))
    .OUTPUT(dgx, TensorType({DT_FLOAT,DT_FLOAT16,DT_BF16}))
    .OUTPUT(dbeta, TensorType({DT_FLOAT}))
    .OUTPUT(dgamma, TensorType({DT_FLOAT}))
    .ATTR(alpha, Float, 0.3f)
    .OP_END_FACTORY_REG(DeepNormGrad)
```

## Brief

DeepNormGrad Operator.

## Inputs

- dy: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- x: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- gx: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- gamma: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- mean: A Tensor. Support dtype: [float32], support format: [ND].
- rstd: A Tensor. Support dtype: [float32], support format: [ND].

## Outputs

- dx: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- dgx: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- dbeta: A Tensor. Support dtype: [float32], support format: [ND].
- dgamma: A Tensor. Support dtype: [float32], support format: [ND].

## Attributes

alpha: An optional attribute, the type is float. Defaults to 0.3.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: float16,float32
- input1 x: float16,float32
- input2 gx: float16,float32
- input3 gamma: float16,float32
- input4 mean: float32
- input5 rstd: float32
- output0 dx: float16,float32
- output1 dgx: float16,float32
- output2 dbeta: float32
- output3 dgamma: float32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
