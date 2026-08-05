# ForeachCopy

```c
REG_OP(ForeachCopy)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16, DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_UINT32, DT_INT64, DT_DOUBLE, DT_BOOL}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16, DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_UINT32, DT_INT64, DT_DOUBLE, DT_BOOL}))
    .OP_END_FACTORY_REG(ForeachCopy)
```

## Brief

Apply copy operation for each tensor in a tensor list in manner of element-wise

## Inputs

One inputs:
x: A tensor list containing multiple tensors. The data type can only be
float16, float, bfloat16, int8, int16, int32, uint8, uint16, uint32, int64, float64, bool.
The format support ND. Shape support 1D ~ 8D.

## Outputs

y: A tensor list which store the tensors whose value are the copy value of the x.
The data type can only be float16, float, bfloat16, int8, int16, int32, uint8, uint16, uint32, int64, float64, bool.
The format support ND. Shape support 1D ~ 8D. Has the same dtype adn shape as input "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32
- output0 y: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
