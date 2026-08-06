# TensorMapInsert

```c
REG_OP(TensorMapInsert)
    .INPUT(input_handle, TensorType({DT_VARIANT}))
    .INPUT(key, TensorType({DT_INT32, DT_INT64, DT_STRING}))
    .INPUT(value, BasicType)
    .OUTPUT(output_handle, TensorType({DT_VARIANT}))
    .OP_END_FACTORY_REG(TensorMapInsert)
```

## Brief

Returns a map that is the 'input_handle'
with the given key-value pair inserted. 

## Inputs

- input_handle: The original map, Must be type: DT_VARIANT.
- key: A Tensor,the key to be inserted.Must be one of
the following types: int32, int64, string.
- value: A Tensor,the value to be inserted.Must be
one of BasicType types. 

## Outputs

output_handle: The map with key and value inserted.
Must be type: DT_VARIANT. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_handle: variant
- input1 key: int32,int64,string
- input2 value: bfloat16,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- output0 output_handle: variant


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
