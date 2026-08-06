# AddRmsNorm

```c
REG_OP(AddRmsNorm)
    .INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(rstd, TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .OUTPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(epsilon, Float, 1e-6f)
    .OP_END_FACTORY_REG(AddRmsNorm)
```

## Brief

AddRmsNorm operator interface implementation. 
 calculating: x1, x2, gamma 
 x = x1 + x2 
 rstd = np.rsqrt(np.mean(np.power(x,2), reduce_axis, keepdims=True) + epsilon)) 
 y = gamma * (x * rstd)

## Inputs

Three inputs, including:
- x1: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- x2: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- gamma: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].

## Outputs

Three outputs, including:
- y: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- rstd: A Tensor. Support dtype: [float32], support format: [ND].
- x: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].

## Attributes

epsilon: Input eps in the formula, which is used to prevent division-by-zero errors.
A optional attribute, the type is float. Defaults to 1e-6.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- input2 gamma: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
- output1 rstd: float32
- output2 x: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
