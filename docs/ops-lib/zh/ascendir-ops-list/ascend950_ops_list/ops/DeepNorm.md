# DeepNorm

```c
REG_OP(DeepNorm)
  .INPUT(x, TensorType({DT_FLOAT,DT_FLOAT16,DT_BF16}))
  .INPUT(gx, TensorType({DT_FLOAT,DT_FLOAT16,DT_BF16}))
  .INPUT(beta, TensorType({DT_FLOAT,DT_FLOAT16,DT_BF16}))
  .INPUT(gamma, TensorType({DT_FLOAT,DT_FLOAT16,DT_BF16}))
  .OUTPUT(mean, TensorType({DT_FLOAT,DT_FLOAT,DT_FLOAT}))
  .OUTPUT(rstd, TensorType({DT_FLOAT,DT_FLOAT,DT_FLOAT}))
  .OUTPUT(y, TensorType({DT_FLOAT,DT_FLOAT16,DT_BF16}))
  .ATTR(alpha, Float, 0.3f)
  .ATTR(epsilon, Float, 1e-06f)
  .OP_END_FACTORY_REG(DeepNorm)
```

## Brief

DeepNorm operator. 
 calculating: x, gx, gamma, beta, alpha 
 new_x = x * alpha + gx 
 y = gamma*(new_x - mean) / np.sqrt(variance + 1e-6) + beta

## Inputs

Four inputs, including:
- x: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- gx: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- gamma: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- beta: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].

## Outputs

Three outputs, including:
- mean: A Tensor. Support dtype: [float32], support format: [ND].
- rstd: A Tensor. Support dtype: [float32], support format: [ND].
- y: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].

## Attributes

- alpha: An optional attribute, the type is float. Defaults to 0.3.
- eps: An optional attribute, the type is float. Defaults to 1e-06.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 gx: bfloat16,float16,float32
- input2 beta: bfloat16,float16,float32
- input3 gamma: bfloat16,float16,float32
- output0 mean: float32
- output1 rstd: float32
- output2 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
