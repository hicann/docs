# DiagV2

```c
REG_OP(DiagV2)
    .INPUT(x, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64,
                          DT_FLOAT, DT_FLOAT16, DT_BF16, DT_DOUBLE, DT_BOOL,
                          DT_COMPLEX32, DT_COMPLEX128, DT_COMPLEX64}))
    .ATTR(diagonal, Int, 0)
    .OUTPUT(y, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64,
                           DT_FLOAT, DT_FLOAT16, DT_BF16, DT_DOUBLE, DT_BOOL,
                           DT_COMPLEX32, DT_COMPLEX128, DT_COMPLEX64}))
    .OP_END_FACTORY_REG(DiagV2)
```

## Brief

Create a diagonal tensor

## Inputs

One input, include:
x: A mutable Tensor must be 2D tensor. Type must be one of the
    following types:
    DT_FLOAT, DT_INT32, DT_INT64, DT_FLOAT16, DT_BF16, DT_INT16, DT_UINT16, DT_UINT32, DT_UINT64,
DT_INT8, DT_UINT8, DT_DOUBLE, DT_BOOL,
DT_COMPLEX32, DT_COMPLEX128, DT_COMPLEX64 . 

## Outputs

y: A mutable Tensor. Has the same type as "x" . 
@see Diag()

## Attributes

diagonal: A optional int32. Specifies the position of output tensors'value. Defaults to "0" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,complex64,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bfloat16,bool,complex64,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator Diag.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
