# TensorArrayConcat

```c
REG_OP(TensorArrayConcat)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .INPUT(flow_in, TensorType({DT_FLOAT}))
    .OUTPUT(value, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_INT8,
        DT_INT16, DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_BOOL,
        DT_STRING, DT_COMPLEX64, DT_COMPLEX128, DT_QINT8,
        DT_QUINT8, DT_QINT32}))
    .OUTPUT(lengths, TensorType({DT_INT64}))
    .REQUIRED_ATTR(dtype, Type)
    .ATTR(element_shape_except0, ListInt, ge::UNKNOWN_RANK)
    .OP_END_FACTORY_REG(TensorArrayConcat)
```

## Brief

Concat the elements from the TensorArray into value value. 

## Inputs

The input handle must be type resource. Inputs include:
- handle: The handle to a TensorArray.
- flow_in: A float scalar that enforces proper chaining of operations.

## Outputs

- value: All of the elements in the TensorArray, concatenated along
the first axis.
- lengths: A vector of the row sizes of the original T elements in the
value output. 

## Attributes

- dtype: The type of the elem that is returned.
- element_shape_except0: The expected shape of an element, if known,
excluding the first dimension. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- input1 flow_in: float32
- output0 value: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,string,uint8,uint16
- output1 lengths: int64

## Third-party framework compatibility

Compatible with tensorflow TensorArrayConcat operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
