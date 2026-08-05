# Split

```c
REG_OP(Split)
    .INPUT(split_dim, TensorType({DT_INT32}))
    .INPUT(x, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT,  DT_FLOAT16, DT_INT16,
                          DT_INT32,      DT_INT64,     DT_INT8,   DT_QINT16, DT_QINT32,  DT_QINT8,
                          DT_QUINT16,    DT_QUINT8,    DT_UINT16, DT_UINT32, DT_UINT64,  DT_UINT8,
                          DT_BF16,       DT_BOOL}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT,  DT_FLOAT16, DT_INT16,
                                   DT_INT32,      DT_INT64,     DT_INT8,   DT_QINT16, DT_QINT32,  DT_QINT8,
                                   DT_QUINT16,    DT_QUINT8,    DT_UINT16, DT_UINT32, DT_UINT64,  DT_UINT8,
                                   DT_BF16,       DT_BOOL}))
    .REQUIRED_ATTR(num_split, Int)
    .OP_END_FACTORY_REG(Split)
```

## Brief

Splits a tensor along dimension "split_dim" into "num_split" smaller tensors .

## Inputs

Two inputs, including:
- split_dim: Must be the following type:int32. Specifies the dimension along which to split.
Supported format list ["ND"].
- x: An ND Tensor.
Must be one of the types:float16, float32, double, int64, int32, uint8,
uint16, uint32, uint64, int8, int16, bool, complex64, complex128, qint8,
quint8, qint16, quint16, qint32, bfloat16.Supported format list ["ND"].

## Outputs

- y: Dynamic output.A list of output tensors. Has the same type and format as "x".Supported format list ["ND"].

## Attributes

- num_split: A required int includes all types of int.
Specifies the number of output tensors. No default value.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 split_dim: int32,int64
- input1 x: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
- output0 y: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64
### AI CPU
- input0 split_dim: int32
- input1 x: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint16,qint32,quint8,quint16,uint8,uint16,uint32,uint64

## Attention Constraints

- "num_split" is greater than or equals to 1.
- "num_split" is divisible by the size of dimension "split_dim".
- "split_dim" is in the range [-len(x.shape), len(x.shape)-1].

## Third-party framework compatibility

Compatible with the TensorFlow operator Split.


---

[Back to Operator Specifications (Ascend950)](../README.md)
