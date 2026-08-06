# Add

```c
REG_OP(Add)
    .INPUT(x1, TensorType({DT_BOOL, DT_FLOAT, DT_INT32, DT_INT64, DT_FLOAT16, DT_BF16, DT_INT16,
                           DT_INT8, DT_UINT8, DT_DOUBLE, DT_COMPLEX128,
                           DT_COMPLEX64, DT_STRING, DT_COMPLEX32}))
    .INPUT(x2, TensorType({DT_BOOL, DT_FLOAT, DT_INT32, DT_INT64, DT_FLOAT16, DT_BF16, DT_INT16,
                           DT_INT8, DT_UINT8, DT_DOUBLE, DT_COMPLEX128,
                           DT_COMPLEX64, DT_STRING, DT_COMPLEX32}))
    .OUTPUT(y, TensorType({DT_BOOL, DT_FLOAT, DT_INT32, DT_INT64, DT_FLOAT16, DT_BF16, DT_INT16,
                           DT_INT8, DT_UINT8, DT_DOUBLE, DT_COMPLEX128,
                           DT_COMPLEX64, DT_STRING, DT_COMPLEX32}))
    .OP_END_FACTORY_REG(Add)
```

## Brief

Returns x1 + x2 element-wise. Support broadcasting operations.

## Inputs

Two inputs, including:
- x1: A ND Tensor. Must be one of the following types: bool, int8, int16, int32, int64, uint8, float64,
    float16, bfloat16, float32, complex128, complex64, complex32, string.
- x2: A ND Tensor. Must be one of the following types: bool, int8, int16, int32, int64, uint8, float64,
    float16, bfloat16, float32, complex128, complex64, complex32, string. 

## Outputs

y: A ND Tensor. Must be one of the following types: bool, int8, int16, int32, int64, uint8, float64,
    float16, bfloat16, float32, complex128, complex64, complex32, string.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x1: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 x2: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator Add.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
