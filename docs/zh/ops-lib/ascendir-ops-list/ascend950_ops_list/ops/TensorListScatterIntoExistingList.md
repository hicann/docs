# TensorListScatterIntoExistingList

```c
REG_OP(TensorListScatterIntoExistingList)
    .INPUT(input_handle, TensorType({DT_VARIANT}))
    .INPUT(tensor, TensorType({DT_FLOAT16,DT_FLOAT,DT_DOUBLE,DT_INT8,
        DT_INT16,DT_INT32,DT_INT64,DT_UINT8,DT_UINT16,DT_QINT8,DT_QUINT8,
        DT_QINT16,DT_QUINT16,DT_QINT32,DT_BOOL,
        DT_STRING,DT_COMPLEX64,DT_COMPLEX128}))
    .INPUT(indices, TensorType({DT_INT32}))
    .OUTPUT(output_handle, TensorType({DT_VARIANT}))
    .ATTR(element_dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(TensorListScatterIntoExistingList)
```

## Brief

Scatters tensor at indices in an input list. 

## Inputs

- input_handle: The input tensor list.
- tensor: The input tensor.
- indices: The indices used to index into the list.

## Outputs

output_handle: The TensorList. 

## Attributes

element_dtype: An optional attribute. The type of elements in the list. Defaults to DT_INT32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_handle: variant
- input1 tensor: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64
- input2 indices: int32
- output0 output_handle: variant

## Third-party framework compatibility.

Compatible with tensorflow TensorListScatterIntoExistingList operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
