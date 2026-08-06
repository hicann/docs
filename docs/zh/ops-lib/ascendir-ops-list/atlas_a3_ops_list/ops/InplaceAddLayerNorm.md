# InplaceAddLayerNorm

```c
REG_OP(InplaceAddLayerNorm)
    .INPUT(x1, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(x2, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(gamma, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(beta, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(bias, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(x1, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(mean, ge::TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .OUTPUT(rstd, ge::TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .OUTPUT(x2, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .ATTR(epsilon, Float, 1e-5f)
    .ATTR(additional_output, Bool, false)
    .OP_END_FACTORY_REG(InplaceAddLayerNorm)
```

## Brief

Fused Operator of Add and LayerNorm.

## Inputs

- x1: A tensor for add compute. Support dtype: [float32, float16, bfloat16], support format: [ND], support shape 1D ~ 8D.
- x2: A tensor for add compute. Support dtype: [float32, float16, bfloat16], support format: [ND], support shape 1D ~ 8D.
Has the same dtype and shape as "x1".
- gamma: Represents the weight parameter, used to scale the normalized output. Support dtype: [float32, float16, bfloat16], support format: [ND], support shape 1D ~ 8D.
Has the same dtype as "x1". The dimension value of gamma shape must be the same as the dimension value of "x1" that needs to be normalized.
- beta: Indicates the bias parameter, used to offset the normalized output. Support dtype: [float32, float16, bfloat16], support format: [ND], support shape 1D ~ 8D.
Has the same dtype as "x1". The dimension value of beta shape must be the same as the dimension value of "x1" that needs to be normalized.
- bias: Indicates an optional bias term that will be added to the result of x1 + x2. Support dtype: [float32, float16, bfloat16], support format: [ND], support shape 1D ~ 8D.
Has the same dtype as "x1". The bias shape can be consistent with either "gamma"/"beta" or "x1"/"x2".

## Outputs

- x1: Represents the output tensor of the final layer normalization. Support dtype: [float32, float16, bfloat16], support format: [ND], support shape 1D ~ 8D.
Has the same dtype as "x1".
- mean: Indicates the mean of the results of the addition operation (x1 + x2 + bias) during the computation. Support dtype: [float32], support format: [ND].
The dimensions of the first few dimensions of "mean" are the same as those of the first few dimensions of "x1", while the remaining dimensions are 1.
The total dimensionality is the same as that of "x1" (where the first few dimensions refer to the dimensions of "x1" minus the dimensions of gamma,
representing the dimensions that do not require normalization).
- rstd: Indicates the reciprocal of the standard deviation of the addition operation results during the output calculation process. Support dtype: [float32], support format: [ND].
The dimensions of the first few dimensions of "rstd" are the same as those of the first few dimensions of "x1", while the remaining dimensions are 1.
The total dimensionality is the same as that of "x1" (where the first few dimensions refer to the dimensions of "x1" minus the dimensions of gamma,
representing the dimensions that do not require normalization).
- x2: Represents the tensor resulting from the addition operation. Support dtype: [float32, float16, bfloat16], support format: [ND], support shape 1D ~ 8D.
Has the same dtype and shape as "x1".

## Attributes

- epsilon: A optional attribute, the type is float32. Indicates the value added to the denominator to ensure numerical stability. Defaults to 1e-5.
- additional_output: A optional attribute, the type is bool. Indicates whether to output the result tensor of the addition operation. Defaults to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- input2 gamma: bfloat16,float16,float32
- input3 beta: bfloat16,float16,float32
- input4 bias: bfloat16,float16,float32
- output0 x1: bfloat16,float16,float32
- output1 mean: float32
- output2 rstd: float32
- output3 x2: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
