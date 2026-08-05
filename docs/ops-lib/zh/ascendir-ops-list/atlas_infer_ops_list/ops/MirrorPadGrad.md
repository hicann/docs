# MirrorPadGrad

```c
REG_OP(MirrorPadGrad)
    .INPUT(x, TensorType({ DT_INT8, DT_UINT8, DT_INT16, DT_UINT16,
              DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE,
              DT_COMPLEX64, DT_COMPLEX128 }))
    .INPUT(paddings, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({ DT_INT8, DT_UINT8, DT_INT16, DT_UINT16,
              DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE,
              DT_COMPLEX64, DT_COMPLEX128 }))
    .REQUIRED_ATTR(mode, String)
    .OP_END_FACTORY_REG(MirrorPadGrad)
```

## Brief

Gradient op for MirrorPad op. Folds a mirror-padded tensor. 

## Inputs

Inputs "x" and "y" are 1D vectors.
- x: A tensor of type int8, uint8, int16, uint16, int32, int64, float16, float,
double, complex64 and complex128. The input tensor to be folded.
- paddings: A tensor of type int32 or int64. A two-column matrix
specifying the padding sizes. 

## Outputs

y: A tensor. Has the same type as "x". 

## Attributes

mode: A string from: "REFLECT", "SYMMETRIC". The mode used in the MirrorPad op. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 paddings: int32,int64
- output0 y: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

MirrorPadGrad runs on the Ascend AI CPU, which delivers poor performance. 

## Third-party framework compatibility

Compatible with the TensorFlow operator MirrorPadGrad.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
