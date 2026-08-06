# AddRmsNormCast

```c
REG_OP(AddRmsNormCast)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(y1, TensorType({DT_FLOAT}))
    .OUTPUT(y2, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(rstd, TensorType({DT_FLOAT}))
    .OUTPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .ATTR(epsilon, Float, 1e-6f)
    .OP_END_FACTORY_REG(AddRmsNormCast)
```

## Brief

AddRmsNormCast operator interface implementation. 
 calculating: x1, x2, gamma 
 x = x1 + x2 
 rstd = np.rsqrt(np.mean(np.power(x,2), reduce_axis, keepdims=True) + epsilon)) 
 y2 = gamma * (x * rstd) 
 y1 = cast16232(y2) 

## Inputs

Three inputs, including:
- x1: A tensor. Support dtype: float16/bfloat16, support format: ND.
- x2: A tensor. Support dtype: float16/bfloat16, support format: ND.
- gamma: A tensor. Support dtype: float16/bfloat16, support format: ND.

## Outputs

Four outputs, including:
- y1: A tensor. Support dtype: float32, support format: ND.
- y2: A tensor. Support dtype: float16/bfloat16, support format: ND.
- rstd: A tensor. Describing the reciprocal of (x1 + x2)'s standard deviation.
          Support dtype: float32, support format: ND.
- x: A tensor. Support dtype: float16/bfloat16, support format: ND.

## Attributes

epsilon: Input eps in the formula, which is used to prevent division-by-zero errors.
An optional attribute, the type is float. Defaults to 1e-6.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16
- input1 x2: bfloat16,float16
- input2 gamma: bfloat16,float16
- output0 y1: float32
- output1 y2: bfloat16,float16
- output2 rstd: float32
- output3 x: bfloat16,float16


---

[Back to Operator Specifications (Ascend950)](../README.md)
