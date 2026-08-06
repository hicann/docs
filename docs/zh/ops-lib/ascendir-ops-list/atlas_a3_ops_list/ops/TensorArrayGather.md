# TensorArrayGather

```c
REG_OP(TensorArrayGather)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .INPUT(indices, TensorType({DT_INT32}))
    .INPUT(flow_in, TensorType({DT_FLOAT}))
    .OUTPUT(value, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_INT8,
        DT_INT16, DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_BOOL,
        DT_STRING, DT_COMPLEX64, DT_COMPLEX128, DT_QINT8,
        DT_QUINT8, DT_QINT32}))
    .REQUIRED_ATTR(dtype, Type)
    .ATTR(element_shape, ListInt, ge::UNKNOWN_RANK)
    .OP_END_FACTORY_REG(TensorArrayGather)
```

## Brief

All elements selected by indices must have the same shape. 

## Inputs

The input handle must be type resource. Inputs include:
- handle: The handle to a TensorArray.
- indices: The locations in the TensorArray from which to read tensor
elements.
- flow_in: A float scalar that enforces proper chaining of operations.

## Outputs

value:  All of the elements in the TensorArray, concatenated along a new
axis (the new dimension 0). 

## Attributes

- dtype: The type of the elem that is returned.
- element_shape: The expected shape of an element, if known. Used to
validate the shapes of TensorArray elements. If this shape is not fully
specified, gathering zero-size TensorArrays is an error. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- input1 indices: int32
- input2 flow_in: float32
- output0 value: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,string,uint8,uint16

## Third-party framework compatibility

Compatible with tensorflow TensorArrayGather operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
