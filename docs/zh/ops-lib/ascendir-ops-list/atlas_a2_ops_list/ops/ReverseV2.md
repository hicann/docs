# ReverseV2

```c
REG_OP(ReverseV2)
    .INPUT(x, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_INT64, DT_BOOL, DT_FLOAT16, DT_FLOAT,
                          DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128, DT_STRING, DT_BF16}))
    .INPUT(axis, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_INT64, DT_BOOL, DT_FLOAT16, DT_FLOAT,
                           DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128, DT_STRING, DT_BF16}))
    .OP_END_FACTORY_REG(ReverseV2)
```

## Brief

Reverses specific dimensions of a tensor .

## Inputs

Two inputs, including:
- x: An ND Tensor (up to 8D).
Must be one of the following types: int8, uint8, int16, uint16, int32, int64, bool, bfloat16, float16, float32,
double, complex64, complex128, string.
- axis: A 1D Tensor.
Must be one of the following types: int32, int64 . 

## Outputs

y: A Tensor. Has the same type and format as "x" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,string,uint8,uint16
- input1 axis: int32,int64
- output0 y: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,string,uint8,uint16
### AI CPU
- input0 x: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,string,uint8,uint16
- input1 axis: int32,int64
- output0 y: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,string,uint8,uint16
### Dvpp
- input0 x: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,string,uint8,uint16
- input1 axis: int32
- output0 y: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,string,uint8,uint16

## Attention Constraints

"axis" must be within the rank of "x" . 

## Third-party framework compatibility

Compatible with the TensorFlow operator ReverseV2.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
