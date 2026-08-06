# TensorListGetItem

```c
REG_OP(TensorListGetItem)
    .INPUT(input_handle, TensorType({DT_VARIANT}))
    .INPUT(index, TensorType({DT_INT32}))
    .INPUT(element_shape, TensorType({DT_INT32}))
    .OUTPUT(item, TensorType({DT_FLOAT16,DT_FLOAT,DT_DOUBLE,DT_INT8,
        DT_INT16,DT_INT32,DT_INT64,DT_UINT8,DT_UINT16,DT_QINT8,DT_QUINT8,
        DT_QINT16,DT_QUINT16,DT_QINT32,DT_BOOL,
        DT_STRING,DT_COMPLEX64,DT_COMPLEX128}))
    .ATTR(element_dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(TensorListGetItem)
```

## Brief

Get input tensor list elements of index position. 

## Inputs

- input_handle: The input list.
- index: A tensor of position.
- element_shape: A shape compatible with that of elements in the list.

## Outputs

item: An output tensor value of index position . 

## Attributes

element_dtype: An optional attribute. The type of elements in the list. Defaults to DT_INT32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_handle: variant
- input1 index: int32
- input2 element_shape: int32
- output0 item: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64

## Third-party framework compatibility.

Compatible with tensorflow TensorListGetItem operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
