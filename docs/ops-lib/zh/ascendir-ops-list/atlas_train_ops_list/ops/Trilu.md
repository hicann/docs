# Trilu

```c
REG_OP(Trilu)
    .INPUT(x, "T")
    .OPTIONAL_INPUT(k, "T_K")
    .ATTR(upper, Int, 0)
    .OUTPUT(y, "T")
    .DATATYPE(T, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE, DT_INT32, DT_UINT8, DT_INT16,
                          DT_INT8, DT_INT64, DT_QINT8, DT_QUINT8, DT_QINT32, DT_QUINT16, DT_QINT16,
                          DT_UINT16, DT_UINT32, DT_UINT64, DT_BOOL}))
    .DATATYPE(T_K, TensorType({DT_INT32, DT_INT64}))
    .OP_END_FACTORY_REG(Trilu)
```

## Brief

Returns the lower or upper triangular part of a matrix (2-D tensor) or batch of matrices input 

## Inputs

- x: A tensor, which supports 2-8 dimensions or be empty. Must be one of the following types:
float16, bfloat16, float32, double, int32, uint8, int16, int8, int64,
qint8, quint8, qint32, quint16, qint16, uint16, uint32, uint64, bool. 
- k: An optional input tensor indicates the diagonal to consider. Must be int32 or int64 type. If no input,
will be considerer as 0.

## Outputs

y: A tensor. Has the same type and shape as "x" . 

## Attributes

upper: An attribute indicates which part of the triangular matrix to be returned. Must be int32 type.
If upper is 1, returns the upper triangular matrix,
else if upper is 0, returns the lower triangular matrix. Default is 0. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 k: int32,int64
- output0 y: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
