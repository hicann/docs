# ForeachSign

```c
REG_OP(ForeachSign)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_INT8, DT_INT64, DT_BF16}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_INT8, DT_INT64, DT_BF16}))
    .OP_END_FACTORY_REG(ForeachSign)
```

## Brief

Apply sign operation for each tensor in a tensor list in manner of element-wise

## Inputs

One inputs:
x: A tensor list containing multiple tensors. The data type can only be float16, float, int32, int8, int64, bfloat16.
The format support ND. Shape support 1D ~ 8D.

## Outputs

y: A tensor list which store the tensors whose value are the sign value of the x.
The format support ND. The data type can only be float16, float, int32, int8, int64, bfloat16.
Shape support 1D ~ 8D. The data type and shape are same as input "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int8,int32,int64
- output0 y: bfloat16,float16,float32,int8,int32,int64


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
