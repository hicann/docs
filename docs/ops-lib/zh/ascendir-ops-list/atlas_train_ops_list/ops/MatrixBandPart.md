# MatrixBandPart

```c
REG_OP(MatrixBandPart)
    .INPUT(x, TensorType({ DT_INT8, DT_UINT8, \
           DT_INT16, DT_UINT16, DT_INT32, DT_INT64,
           DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BOOL,
           DT_COMPLEX64, DT_COMPLEX128 }))
    .INPUT(num_lower, TensorType({ DT_INT32, DT_INT64 }))
    .INPUT(num_upper, TensorType({ DT_INT32, DT_INT64 }))
    .OUTPUT(y, TensorType({ DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, \
           DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BOOL,
           DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(MatrixBandPart)
```

## Brief

Copies a tensor setting everything outside a central band in each innermost matrix. 

## Inputs

Input "x" is a k-dimensional tensor. Inputs "num_lower" and "num_upper"
are 0D scalars.
- x: A rank k tensor.
- num_lower: A 0D tensor. Number of superdiagonals to keep. If negative,
keeps entire upper triangle.
- num_upper: A 0D tensor. Number of superdiagonals to keep. If negative,
keeps entire upper triangle. 

## Outputs

y: A rank k tensor. Has the same shape as input. The extracted banded tensor. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 num_lower: int32,int64
- input2 num_upper: int32,int64
- output0 y: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Attention Constraints

MatrixBandPart runs on the Ascend AI CPU, which delivers poor performance. 

## Third-party framework compatibility

Compatible with the TensorFlow operator MatrixBandPart.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
