# TensorListPushBackBatch

```c
REG_OP(TensorListPushBackBatch)
    .INPUT(input_handles, TensorType({DT_VARIANT}))
    .INPUT(tensor, TensorType({DT_FLOAT16,DT_FLOAT,DT_DOUBLE,DT_INT8,
        DT_INT16,DT_INT32,DT_INT64,DT_UINT8,DT_UINT16,DT_QINT8,DT_QUINT8,
        DT_QINT16,DT_QUINT16,DT_QINT32,DT_BOOL,
        DT_STRING,DT_COMPLEX64,DT_COMPLEX128}))
    .OUTPUT(output_handles, TensorType({DT_VARIANT}))
    .ATTR(element_dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(TensorListPushBackBatch)
```

## Brief

Push tensor to list. 

## Inputs

- input_handles: The input tensor lists.
- tensor: The tensor push into tensor list.

## Outputs

output_handles: The output tensor lists. 

## Attributes

element_dtype: An optional attribute. The type of elements in the list. Defaults to DT_INT32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_handles: variant
- input1 tensor: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64
- output0 output_handles: variant

## Third-party framework compatibility.

Compatible with tensorflow TensorListPushBackBatch operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
