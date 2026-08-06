# MaskedFill

```c
REG_OP(MaskedFill)
    .INPUT(x, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16, DT_INT8, DT_INT32, DT_INT64, DT_BOOL}))
    .INPUT(mask, TensorType({DT_BOOL}))
    .INPUT(value, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16, DT_INT8, DT_INT32, DT_INT64, DT_BOOL}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16, DT_INT8, DT_INT32, DT_INT64, DT_BOOL}))
    .OP_END_FACTORY_REG(MaskedFill)
```

## Brief

Replace the value of X with value according to mask.

## Inputs

Three inputs, including:
- x: A Tensor of dtype is bfloat16 or float16 or float32 or int64 or int32 or int8 or bool.
- mask: A Tensor of dtype bool.
- value: A Tensor of dtype bfloat16 or float16 or float32 or int64 or int32 or int8 or bool.

## Outputs

y: A tensor. Must be one of the following dtypes:
bfloat16, float16, float32, int64, int32, int8, bool.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,float16,float32,int8,int32
- input1 mask: bool
- input2 value: bfloat16,bool,float16,float32,int8,int32
- output0 y: bfloat16,bool,float16,float32,int8,int32
### AI CPU
- input0 x: float16,float32,int8,int32,int64
- input1 mask: bool
- input2 value: float16,float32,int8,int32,int64
- output0 y: float16,float32,int8,int32,int64

## Attention Constraints

- The input tensors of x and mask must meet the broadcast relationship.
- The dtype of value must be converted to the dtype of x.
- The shape of y is formed by broadcasting x, masked and value.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
