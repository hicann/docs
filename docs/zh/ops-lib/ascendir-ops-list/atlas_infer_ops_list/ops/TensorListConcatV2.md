# TensorListConcatV2

```c
REG_OP(TensorListConcatV2)
    .INPUT(input_handle, TensorType({DT_VARIANT}))
    .INPUT(element_shape, TensorType({DT_INT32,DT_INT64}))
    .INPUT(leading_dims, TensorType({DT_INT64}))
    .OUTPUT(tensor, TensorType({DT_FLOAT16,DT_FLOAT,DT_DOUBLE,DT_INT8,
        DT_INT16,DT_INT32,DT_INT64,DT_UINT8,DT_UINT16,DT_QINT8,DT_QUINT8,
        DT_QINT16,DT_QUINT16,DT_QINT32,DT_BOOL,
        DT_STRING,DT_COMPLEX64,DT_COMPLEX128}))
    .OUTPUT(lengths, TensorType({DT_INT64}))
    .ATTR(element_dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(TensorListConcatV2)
```

## Brief

Concats all tensors in the list along the 0th dimension.
Requires that all tensors have the same shape except the first dimension. 

## Inputs

- input_handle: The input list.
- element_shape: The shape of the uninitialized elements in the list.
If the first dimension is not -1, it is assumed that all list elements have
the same leading dim.
- leading_dims: The list of leading dims of uninitialized list elements. Used if
the leading dim of input_handle.element_shape or the element_shape input arg
is not already set. 

## Outputs

- tensor: The concated result.
- lengths: Output tensor containing sizes of the 0th dimension of tensors
in the list, used for computing the gradient. 

## Attributes

element_dtype: An optional attribute. The type of elements in the list. Defaults to DT_INT32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_handle: variant
- input1 element_shape: int32,int64
- input2 leading_dims: int64
- output0 tensor: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64
- output1 lengths: int64

## Third-party framework compatibility.

Compatible with tensorflow TensorListConcatV2 operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
