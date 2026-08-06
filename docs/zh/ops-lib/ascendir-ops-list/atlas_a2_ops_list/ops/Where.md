# Where

```c
REG_OP(Where)
    .INPUT(x, TensorType({BasicType(), DT_BOOL}))
    .OUTPUT(y, TensorType({DT_INT64}))
    .OP_END_FACTORY_REG(Where)
```

## Brief

Returns locations of nonzero / true values in a tensor. 

## Inputs

Including:
x: A Tensor. Must be one of the following types:
DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT8, DT_UINT8, DT_QINT8,
DT_QUINT8, DT_INT16, DT_UINT16, DT_INT32, DT_UINT32, DT_QINT32,
DT_INT64, DT_UINT64, DT_BOOL, DT_COMPLEX64, DT_COMPLEX128 

## Outputs

y: A Tensor of type DT_INT64. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: int64

## Attention Constraints

Where runs on the Ascend AI CPU, which delivers poor performance.

## Third-party framework compatibility

Compatible with the TensorFlow operator Where.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
