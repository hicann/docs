# Trace

```c
REG_OP(Trace)
    .INPUT(x, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_BOOL, DT_INT8,
                          DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64, DT_BF16}))
    .OUTPUT(y, TensorType({DT_COMPLEX128, DT_COMPLEX64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT64, DT_UINT64, DT_BF16}))
    .OP_END_FACTORY_REG(Trace)
```

## Brief

Returns the sum of the elements of the diagonal of the input 2-D matrix. 

## Inputs

x: A Tensor. Must be one of the following types:complex128, complex64, float64, float32, float16, bool,
                                                int8, uint8, int16, uint16, int32, uint32, int64, uint64, bfloat16,. 

## Outputs

y: A Tensor. Must be one of the following types:complex128, complex64, float64, float32, float16, int64, uint64, bfloat16. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: complex64,complex128,double,float16,float32,int64,uint64

## Third-party framework compatibility

Compatible with the Pytorch operator Trace.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
