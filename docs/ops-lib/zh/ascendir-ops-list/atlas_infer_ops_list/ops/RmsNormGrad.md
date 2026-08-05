# RmsNormGrad

```c
REG_OP(RmsNormGrad)
    .INPUT(dy, TensorType({DT_FLOAT,DT_FLOAT16,DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT,DT_FLOAT16,DT_BF16}))
    .INPUT(rstd, TensorType({DT_FLOAT,DT_FLOAT,DT_FLOAT}))
    .INPUT(gamma, TensorType({DT_FLOAT,DT_FLOAT16,DT_BF16}))
    .OUTPUT(dx, TensorType({DT_FLOAT,DT_FLOAT16,DT_BF16}))
    .OUTPUT(dgamma, TensorType({DT_FLOAT,DT_FLOAT,DT_FLOAT}))
    .OP_END_FACTORY_REG(RmsNormGrad)
```

## Brief

RmsNormGrad operator interface implementation.

## Inputs

Four inputs, including:
- dy: The gradient returned backward.
    A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- x: The input of the forward operator.
    A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- rstd: The intermediate computation result of the forward operator.
    A Tensor. Support dtype: [float32], support format: [ND].
- gamma: The input of the forward operator.
    A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].

## Outputs

- dx: The gradient of input "x", Has the same type and shape as "x".
    A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- dgamma: The gradient of input "gamma". Has the same type and shape as "gamma".
    A Tensor. Support dtype: [float32], support format: [ND].

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: float16,float32
- input1 x: float16,float32
- input2 rstd: float32
- input3 gamma: float16,float32
- output0 dx: float16,float32
- output1 dgamma: float32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
