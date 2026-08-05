# MaskedScatter

```c
REG_OP(MaskedScatter)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_UINT8, DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_BOOL,
                          DT_BF16}))
    .INPUT(mask, TensorType({DT_BOOL}))
    .INPUT(updates, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_UINT8, DT_INT8, DT_INT16, DT_INT32, DT_INT64,
                                DT_BOOL, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_UINT8, DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_BOOL,
                           DT_BF16}))
    .OP_END_FACTORY_REG(MaskedScatter)
```

## Brief

update the value of X with value according to mask.

## Inputs

three inputs, including:
 @li x: A Tensor of dtype is float16 or float32 or float64 or
     int64 or int32 or int16 or int8 or uint8 or bool or bfloat16.
 @li mask: A Tensor of dtype is bool.
 @li updates: A tensor with the same type as x. 

## Outputs

 @li y: A tensor with the same type as x. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8
- input1 mask: bool
- input2 updates: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8
- output0 y: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8
### AI CPU
- input0 x: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8
- input1 mask: bool
- input2 updates: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8
- output0 y: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8


---

[Back to Operator Specifications (Ascend950)](../README.md)
