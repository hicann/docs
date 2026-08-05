# Fill

```c
REG_OP(Fill)
    .INPUT(dims, TensorType::IndexNumberType())
    .INPUT(value, "T")
    .OUTPUT(y, "T")
    .DATATYPE(T, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT32, DT_UINT8, DT_INT16,
                              DT_INT8, DT_COMPLEX64, DT_INT64, DT_BOOL, DT_QINT8,
                              DT_QUINT8, DT_QINT32, DT_QINT16, DT_QUINT16, DT_UINT16,
                              DT_COMPLEX128, DT_FLOAT16, DT_BF16, DT_UINT32, DT_UINT64, DT_STRING}))
    .OP_END_FACTORY_REG(Fill)
```

## Brief

Creates a tensor filled with a scalar value.
This operation creates a tensor of shape "dims" and fills it with "value".

## Inputs

- dims: A 1D tensor of types int32 or int64. Represents the shape of the output tensor .
The size of each dimension must be less than or equal to 8. 
- value: A 0D scalar. Specifies the value to fill the returned tensor.
   Must be one of the following types:
   bfloat16, float16, float32, double, int32, uint8, int16, int8, complex64, int64, bool,
   qint8, quint8, qint32, qint16, quint16, uint16, complex128, uint32, uint64, string.

## Outputs

y: A tensor. Has the same type as "value".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dims: int32,int64
- input1 value: bool,float16,float32,int8,int32,int64
- output0 y: bool,float16,float32,int8,int32,int64
### AI CPU
- input0 dims: int32,int64
- input1 value: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

- Compatible with the TensorFlow operator Fill.
- Compatible with the Caffe operator Filler.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
