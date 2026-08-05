# TensorListSetItem

```c
REG_OP(TensorListSetItem)
    .INPUT(input_handle, TensorType({DT_VARIANT}))
    .INPUT(index, TensorType({DT_INT32}))
    .INPUT(item, TensorType({DT_FLOAT16,DT_FLOAT,DT_DOUBLE,DT_INT8,
        DT_INT16,DT_INT32,DT_INT64,DT_UINT8,DT_UINT16,DT_QINT8,DT_QUINT8,
        DT_QINT16,DT_QUINT16,DT_QINT32,DT_BOOL,DT_RESOURCE,
        DT_STRING,DT_COMPLEX64,DT_COMPLEX128}))
    .OUTPUT(output_handle, TensorType({DT_VARIANT}))
    .ATTR(element_dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(TensorListSetItem)
```

## Brief

Sets the index-th position of the list to contain the given tensor. 

## Inputs

- input_handle: The input list.
- index: The position in the list to which the tensor will be assigned.
- item: The element to be assigned to that position.

## Outputs

output_handle: An output tensor list . 

## Attributes

element_dtype: An optional attribute. The type of elements in the list. Defaults to DT_INT32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_handle: variant
- input1 index: int32
- input2 item: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,resource,string,uint8,uint16,uint32,uint64
- output0 output_handle: variant

## Third-party framework compatibility.

Compatible with tensorflow TensorListSetItem operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
