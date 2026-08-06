# TensorMapLookup

```c
REG_OP(TensorMapLookup)
    .INPUT(input_handle, TensorType({DT_VARIANT}))
    .INPUT(key, TensorType({DT_INT32, DT_INT64, DT_STRING}))
    .OUTPUT(value, BasicType)
    .REQUIRED_ATTR(value_dtype, Type)
    .OP_END_FACTORY_REG(TensorMapLookup)
```

## Brief

Returns the value from a given key in a tensor map. 

## Inputs

- input_handle: The input map. Must be type: DT_VARIANT.
- key: A Tensor, the key to be looked up. Must be one of
the following types: int32,int64,string. 

## Outputs

value: A Tensor,the value found from the given key.

## Attributes

value_dtype: A int. Representing the type of value. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_handle: variant
- input1 key: int32,int64,string
- output0 value: bfloat16,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64


---

[Back to Operator Specifications (Ascend950)](../README.md)
