# MirrorPad

```c
REG_OP(MirrorPad)
    .INPUT(x, TensorType({ DT_INT8, DT_UINT8, DT_INT16, DT_UINT16,
      DT_INT32, DT_INT64, DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BOOL,
      DT_COMPLEX64, DT_COMPLEX128 }))
    .INPUT(paddings, TensorType({ DT_INT32, DT_INT64 }))
    .OUTPUT(y, TensorType({ DT_INT8, DT_UINT8, DT_INT16, DT_UINT16,
      DT_INT32, DT_INT64, DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BOOL,
      DT_COMPLEX64, DT_COMPLEX128 }))
    .REQUIRED_ATTR(mode, String)
    .OP_END_FACTORY_REG(MirrorPad)
```

## Brief

Fills the tensor with the mirror value. 

## Inputs

- x: The tensor to be padded. Format support ND,
support 1D ~ 5D. Type must be one of the following
types: int8, uint8, int16, uint16, int32, int64, float16, float,
double, bool, complex64, complex128, bfloat16.
- paddings: A two-column matrix specifying the padding sizes.
The number of rows has the same rank as "x", type must be int32 or int64. 

## Outputs

y: The padded tensor. 

## Attributes

mode: Either "REFLECT" or "SYMMETRIC". In reflect mode the padded regions
do not include the borders, while in symmetric mode the padded regions
do include the borders. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int16,int32,int64,uint16,uint32
- input1 paddings: int32,int64
- output0 y: float16,float32,int16,int32,int64,uint16,uint32
### AI CPU
- input0 x: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 paddings: int32,int64
- output0 y: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

MirrorPad runs on the Ascend AI CPU, which delivers poor performance. 

## Third-party framework compatibility

Compatible with the TensorFlow operator MirrorPad.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
