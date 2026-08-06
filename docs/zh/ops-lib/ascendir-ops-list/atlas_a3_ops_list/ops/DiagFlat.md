# DiagFlat

```c
REG_OP(DiagFlat)
    .INPUT(x, "T")
    .ATTR(diagonal, Int, 0)
    .OUTPUT(y, "T")
    .DATATYPE(T, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE,
                             DT_INT8, DT_INT16, DT_INT32, DT_INT64,
                             DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64,
                             DT_BOOL, DT_COMPLEX64}))
    .OP_END_FACTORY_REG(DiagFlat)
```

## Brief

Create a diagonal tensor

## Inputs

One input, include:
x: A Tensor. Must be one of the
    following types:
    float16, float32, double, int8, int16,int32, int64, complex32, complex64, complex128.

## Outputs

y: A mutable Tensor. Has the same type as "x".
@see DiagFlat()

## Attributes

- diagonal: An optional int value. Defaults to 0, this attribute controls which diagonal to consider:
              If diagonal = 0, it is the main diagonal.
              If diagonal > 0, it is above the main diagonal.
              If diagonal < 0, it is below the main diagonal.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,complex64,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bfloat16,complex64,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator Diag.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
