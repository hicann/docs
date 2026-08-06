# AdaLayerNorm

```c
REG_OP(AdaLayerNorm)
    .INPUT(x, "T1")
    .INPUT(scale, "T1")
    .INPUT(shift, "T1")
    .OUTPUT(y, "T1")
    .OUTPUT(ln_res, "T1")
    .OUTPUT(mean, "T2")
    .OUTPUT(rstd, "T2")
    .ATTR(epsilon, Float, 0.00001f)
    .DATATYPE(T1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DATATYPE(T2, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(AdaLayerNorm)
```

## Brief

AdaLayerNorm operator interface implementation
 calculating: x, scale, shift
 mean  = np.mean(x, reduce_axis, keepdims=True)
 rstd = np.rsqrt(np.mean(np.power((x - mean),2), reduce_axis, keepdims=True) + epsilon))
 y = ((x - mean) * rstd) * (1 + scale) + shift 

## Inputs

Three inputs, including:
- x: A Tensor. Must be one of the following types: float16, float32, bfloat16.
- scale: A Tensor. Must be one of the following types: float16, float32, bfloat16.
- shift: A Tensor. Must be one of the following types: float16, float32, bfloat16.

## Outputs

Four outputs, including:
- y: A Tensor. Must be one of the following types: float16, float32, bfloat16.
- ln_res: A Tensor. Must be one of the following types: float16, float32, bfloat16.
- mean: A Tensor. Must be one of the following types: float32.
- rstd: A Tensor. Must be one of the following types: float32.

## Attributes

- epsilon: A optional attribute, the type is float32. Defaults to 1e-5 .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 scale: bfloat16,float16,float32
- input2 shift: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
