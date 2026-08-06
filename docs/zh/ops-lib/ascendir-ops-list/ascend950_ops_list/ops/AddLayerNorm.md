# AddLayerNorm

```c
REG_OP(AddLayerNorm)
    .INPUT(x1, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(x2, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(gamma, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(beta, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(bias, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(y, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(mean, ge::TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .OUTPUT(rstd, ge::TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .OUTPUT(x, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .ATTR(epsilon, Float, 1e-5f)
    .ATTR(additional_output, Bool, false)
    .OP_END_FACTORY_REG(AddLayerNorm)
```

## Brief

Fused Operator of Add and LayerNorm. 

## Inputs

- x1: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- x2: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- gamma: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- beta: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- bias: A optional input Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].

## Outputs

- y: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- mean: A Tensor. Support dtype: [float32], support format: [ND].
- rstd: A Tensor. Support dtype: [float32], support format: [ND].
- x: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].

## Attributes

- epsilon: A optional attribute, the type is float. Defaults to 1e-5.
- additional_output: A optional attribute, the type is bool. Defaults to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- input2 gamma: bfloat16,float16,float32
- input3 beta: bfloat16,float16,float32
- input4 bias: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
- output1 mean: float32
- output2 rstd: float32
- output3 x: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
