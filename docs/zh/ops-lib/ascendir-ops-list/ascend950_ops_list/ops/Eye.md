# Eye

```c
REG_OP(Eye)
    .OUTPUT(y, TensorType({TensorType::BasicType(), DT_BOOL}))
    .REQUIRED_ATTR(num_rows, Int)
    .ATTR(num_columns, Int, 0)
    .ATTR(batch_shape, ListInt, {})
    .ATTR(dtype, Int, 0)
    .OP_END_FACTORY_REG(Eye)
```

## Brief

Returns a 2-D tensor with ones on the diagonal and zeros elsewhere.

## Inputs

No inputs

## Outputs

y: A Tensor with targeted type and shape. Must be one of the following types:
  complex128, complex64, double, float32, float16, int16, int32, int64, int8, qint16,
  qint32, qint8, quint16, quint8, uint16, uint32, uint64, uint8, bfloat16, complex32, bool. 

## Attributes

- num_rows: An required int.
- num_columns: An optional int.Defaults to 0.
- batch_shape: An optional ListInt.Defaults to [].
- dtype: An optional int.Defaults to 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- output0 y: bfloat16,bool,float16,float32,int8,int16,int32,int64,uint8

## Third-party framework compatibility

Compatible with the Pytorch operator Eye. 


---

[Back to Operator Specifications (Ascend950)](../README.md)
