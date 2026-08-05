# RealDiv

```c
REG_OP(RealDiv)
    .INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16, DT_DOUBLE, DT_UINT8, DT_INT8,
                           DT_UINT16, DT_INT16, DT_INT32, DT_INT64, DT_BOOL,
                           DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_DOUBLE, DT_UINT8, DT_INT8,
                           DT_UINT16, DT_INT16, DT_INT32, DT_INT64, DT_BOOL,
                           DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_DOUBLE, DT_UINT8, DT_INT8,
                           DT_UINT16, DT_INT16, DT_INT32, DT_INT64,
                           DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(RealDiv)
```

## Brief

Returns x1/x2 element-wise for real types. Support broadcasting operations.

## Inputs

Two inputs, including:
- x1: A ND Tensor.
Must be one of the following types: bfloat16, float16, float32, double, uint16,
int8, uint8, int16, int32, int64, complex64, complex128, bool.
- x2: A ND Tensor.
Must be one of the following types: bfloat16, float16, float32, double, uint16,
int8, uint8, int16, int32, int64, complex64, complex128, bool. 

## Outputs

y: A ND Tensor. Has the same dtype and format as input "x1" if the type of "x1" is not bool.
If the type of "x1" is bool, y is float type. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x1: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 x2: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Third-party framework compatibility

Compatible with the TensorFlow operator RealDiv.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
