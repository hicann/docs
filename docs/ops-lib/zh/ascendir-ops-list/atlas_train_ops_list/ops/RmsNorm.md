# RmsNorm

```c
REG_OP(RmsNorm)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(rstd, TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .ATTR(epsilon, Float, 1e-6f)
    .OP_END_FACTORY_REG(RmsNorm)
```

## Brief

RmsNorm operator interface implementation. 
 calculating: x, gamma 
 rstd = np.rsqrt(np.mean(np.power(x,2), reduce_axis, keepdims=True) + epsilon)) 
 y = gamma * (x * rstd)

## Inputs

Two inputs, including:
- x: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- gamma: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].

## Outputs

Two outputs, including:
- y: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- rstd: A Tensor. Support dtype: [float32], support format: [ND].

## Attributes

epsilon: A optional attribute, the type is float. Defaults to 1e-6.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 gamma: float16,float32
- output0 y: float16,float32
- output1 rstd: float32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
