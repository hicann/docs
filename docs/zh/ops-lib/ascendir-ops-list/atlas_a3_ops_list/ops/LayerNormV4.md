# LayerNormV4

```c
REG_OP(LayerNormV4)
    .INPUT(x, "T1")
    .INPUT(normalized_shape, "T2")
    .OPTIONAL_INPUT(gamma, "T3")
    .OPTIONAL_INPUT(beta, "T4")
    .OUTPUT(y, "T5")
    .OUTPUT(mean, "T6")
    .OUTPUT(rstd, "T6")
    .ATTR(epsilon, Float, 0.00001f)
    .DATATYPE(T1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DATATYPE(T2, TensorType({DT_INT32, DT_INT64}))
    .DATATYPE(T3, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DATATYPE(T4, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DATATYPE(T5, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DATATYPE(T6, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(LayerNormV4)
```

## Brief

LayernormV4 operator interface implementation 
 calculating: x, gamma, beta 
 mean  = np.mean(x, reduce_axis, keepdims=True) 
 rstd = np.rsqrt(np.mean(np.power((x - mean),2), reduce_axis, keepdims=True) + epsilon)) 
 y = gamma*((x - mean) * rstd) + beta

## Inputs

Four inputs, including:
- x: A ND Tensor. Must be one of the following types: float16, float32, bfloat16.
- normalized_shape: A ND Tensor. Must be one of the following types: int32, int64
- gamma: A ND Tensor. Must be one of the following types: float16, float32, bfloat16. Shape is normalized_shape.
- beta: A ND Tensor. Must be one of the following types: float16, float32, bfloat16. Shape is normalized_shape.

## Outputs

Three outputs, including:
- y: A ND Tensor. Must be one of the following types: float16, float32, bfloat16.
- mean: A ND Tensor. Must be one of the following types: float16, float32, bfloat16.
- rstd: A ND Tensor. Must be one of the following types: float16, float32, bfloat16.

## Attributes

- epsilon: An optional attribute, the type is float32. Defaults to 1e-5 .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 normalized_shape: int32
- input2 gamma: bfloat16,float16,float32
- input3 beta: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
- output1 mean: float32
- output2 rstd: float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
