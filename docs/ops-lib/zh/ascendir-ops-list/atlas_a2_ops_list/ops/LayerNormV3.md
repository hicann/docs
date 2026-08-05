# LayerNormV3

```c
REG_OP(LayerNormV3)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(beta, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(mean, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(rstd, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(begin_norm_axis, Int, 0)
    .ATTR(begin_params_axis, Int, 0)
    .ATTR(epsilon, Float, 0.00001f)
    .OP_END_FACTORY_REG(LayerNormV3)
```

## Brief

LayernormV3 operator interface implementation 
 calculating: x, gamma, beta 
 mean  = np.mean(x, reduce_axis, keepdims=True) 
 rstd = np.rsqrt(np.mean(np.power((x - mean),2), reduce_axis, keepdims=True) + epsilon)) 
 y = gamma*((x - mean) * rstd) + beta 
 Notes: the shape of gamma/beta is the slice shape of x(x_shape[begin_norm_axis])

## Inputs

Three inputs, including:
- x: A ND Tensor. Must be one of the following dtypes: float16, float32, bfloat16.
The shape is [A1,...,Ai,R1,...,Rj].
- gamma: A ND Tensor. Must be one of the following dtypes: float16, float32, bfloat16.
Has the same dtype and shape as beta. The shape is [R1,...,Rj].
- beta: A ND Tensor. Must be one of the following dtypes: float16, float32, bfloat16.
Has the same dtype and shape as gamma. The shape is [R1,...,Rj]. 

## Outputs

Three outputs, including:
- y: A ND Tensor. Must be one of the following dtypes: float16, float32, bfloat16.
Has the same dtype, shape and format as x.
- mean: A ND Tensor. Must be one of the following dtypes: float16, float32, bfloat16.
Has the same shape as rstd, which is [A1,...,Ai,1,...,1], where there are j 1's after Ai.
- rstd: A ND Tensor. Must be one of the following dtypes: float16, float32, bfloat16.
Has the same shape as mean, which is [A1,...,Ai,1,...,1], where there are j 1's after Ai.

## Attributes

- begin_norm_axis: An optional attribute, the dtype is int32. Defaults to 0.
Indicates the index of the R1 axis in the shape of x.
- begin_params_axis: An optional attribute, the dtype is int32. Defaults to 0.
In Ascend 950 AI Processor, begin_params_axis and begin_norm_axis refer to the same axis in the shape of x.
- epsilon: An optional attribute, the dtype is float32. Defaults to 1e-5 .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 gamma: bfloat16,float16,float32
- input2 beta: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
- output1 mean: bfloat16,float16,float32
- output2 rstd: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
