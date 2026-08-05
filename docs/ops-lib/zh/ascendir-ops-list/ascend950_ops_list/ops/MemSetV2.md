# MemSetV2

```c
REG_OP(MemSetV2)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8, DT_INT16, DT_INT32, DT_INT64,
        DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_BOOL}))
    .DYNAMIC_OUTPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_INT8, DT_INT16, DT_INT32, DT_INT64,
        DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_BOOL}))
    .ATTR(values_int, ListInt, {})
    .ATTR(values_float, ListFloat, {})
    .OP_END_FACTORY_REG(MemSetV2)
```

## Brief

Set initial values for memory of input tensor list . 

## Inputs

x: A list of input tensors. It's a dynamic input. 

## Outputs

x: A list of output tensor objects, with the same address as the input tensor list.It's a dynamic output. 

## Attributes

- values_int: integer values to be set, the default value is 0.
- values_float: float values to be set, the default value is 0.0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 x: bfloat16,bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64


---

[Back to Operator Specifications (Ascend950)](../README.md)
