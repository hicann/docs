# TensorListStack

```c
REG_OP(TensorListStack)
    .INPUT(input_handle, TensorType({DT_VARIANT}))
    .INPUT(element_shape, TensorType({DT_INT32}))
    .OUTPUT(tensor, TensorType({DT_FLOAT16,DT_FLOAT,DT_DOUBLE,DT_INT8,
        DT_INT16,DT_INT32,DT_INT64,DT_UINT8,DT_UINT16,DT_QINT8,DT_QUINT8,
        DT_QINT16,DT_QUINT16,DT_QINT32,DT_BOOL,
        DT_STRING,DT_COMPLEX64,DT_COMPLEX128}))
    .ATTR(element_dtype, Type, DT_INT32)
    .ATTR(num_elements, Int, -1)
    .OP_END_FACTORY_REG(TensorListStack)
```

## Brief

Stacks all tensors in the list. 

## Inputs

- input_handle: The input tensor list.
- element_shape: A shape compatible with that of elements in the tensor.

## Outputs

tensor: The tensor of list. 

## Attributes

- element_dtype: An optional attribute. The type of elements in the list. Defaults to DT_INT32.
- num_elements: An optional int. The number of elements in the list. Default is -1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_handle: variant
- input1 element_shape: int32
- output0 tensor: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,string,uint8,uint16,uint32,uint64

## Third-party framework compatibility.

Compatible with tensorflow TensorListStack operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
