# ReduceMeanWithCount

```c
REG_OP(ReduceMeanWithCount)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(count, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(count_sum, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(axes, ListInt)
    .ATTR(keep_dims, Bool, false)
    .OP_END_FACTORY_REG(ReduceMeanWithCount)
```

## Brief

Calculate the total mean based on the mean of each device . 

## Inputs

Three inputs, including:
- x: A Tensor. Must be one of the following types: float16, float32 bfloat16 .
- count: A Tensor. Must be one of the following types: float16, float32 bfloat16 .
- count_sum: A Tensor. Must be one of the following types: float16, float32 bfloat16 .

## Outputs

y: The reduced tensor. Has the same type and format as input "x" . 

## Attributes

- axes: A required 1D list or tuple of int32 or int64. Specifies the dimensions to reduce.
- keepdims: An optional bool. If "true", retains reduced dimensions with length 1. Defaults to "false" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 count: bfloat16,float16,float32
- input2 count_sum: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Sum.


---

[Back to Operator Specifications (Ascend950)](../README.md)
