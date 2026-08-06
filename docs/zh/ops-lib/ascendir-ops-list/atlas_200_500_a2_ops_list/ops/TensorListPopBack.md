# TensorListPopBack

```c
REG_OP(TensorListPopBack)
    .INPUT(input_handle, TensorType({DT_VARIANT}))
    .INPUT(element_shape, TensorType({DT_INT32}))
    .OUTPUT(output_handle, TensorType({DT_VARIANT}))
    .OUTPUT(tensor, TensorType({DT_FLOAT16,DT_FLOAT,DT_DOUBLE,DT_INT8,
        DT_INT16,DT_INT32,DT_INT64,DT_UINT8,DT_UINT16,DT_QINT8,DT_QUINT8,
        DT_QINT16,DT_QUINT16,DT_QINT32,DT_BOOL,DT_RESOURCE,
        DT_STRING,DT_COMPLEX64,DT_COMPLEX128}))
    .ATTR(element_dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(TensorListPopBack)
```

## Brief

The last element of the input list as well as a
list with all but that element. 

## Inputs

- input_handle: The input list.
- element_shape: A shape compatible with that of elements in the list.

## Outputs

- output_handle:A list with the elements of the old list followed by tensor.
- tensor:The withdrawn last element of the list.

## Attributes

element_dtype: An optional attribute. The type of elements in the list. Defaults to DT_INT32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_handle: variant
- input1 element_shape: int32
- output0 output_handle: variant
- output1 tensor: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,resource,string,uint8,uint16,uint32,uint64,variant

## Third-party framework compatibility.

Compatible with tensorflow TensorListPopBack operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
