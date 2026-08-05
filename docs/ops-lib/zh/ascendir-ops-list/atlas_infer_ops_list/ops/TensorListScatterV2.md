# TensorListScatterV2

```c
REG_OP(TensorListScatterV2)
    .INPUT(tensor, TensorType({DT_FLOAT16,DT_FLOAT,DT_DOUBLE,DT_INT8,
        DT_INT16,DT_INT32,DT_INT64,DT_UINT8,DT_UINT16,DT_QINT8,DT_QUINT8,
        DT_QINT16,DT_QUINT16,DT_QINT32,DT_BOOL,
        DT_STRING,DT_COMPLEX64,DT_COMPLEX128}))
    .INPUT(indices, TensorType({DT_INT32}))
    .INPUT(element_shape, TensorType({DT_INT32,DT_INT64}))
    .INPUT(num_elements, TensorType({DT_INT32}))
    .OUTPUT(output_handle, TensorType({DT_VARIANT}))
    .ATTR(element_dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(TensorListScatterV2)
```

## Brief

Creates a TensorList by indexing into a Tensor. 

## Inputs

- tensor: The input tensor.
- indices: The indices used to index into the list.
- element_shape: The shape of the elements in the list (can be less specified than
the shape of the tensor).
- num_elements: The size of the output list. Must be large enough to accommodate
the largest index in indices. If -1, the list is just large enough to include
the largest index in indices. 

## Outputs

output_handle: The TensorList. 

## Attributes

element_dtype: An optional attribute. The type of elements in the list. Defaults to DT_INT32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 tensor: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64
- input1 indices: int32
- input2 element_shape: int32,int64
- input3 num_elements: int32
- output0 output_handle: variant

## Third-party framework compatibility.

Compatible with tensorflow TensorListScatterV2 operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
