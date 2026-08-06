# Cross

```c
REG_OP(Cross)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT8, DT_UINT8,
                           DT_INT16, DT_DOUBLE, DT_INT64, DT_UINT16, DT_UINT32,
                           DT_UINT64, DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT8, DT_UINT8,
                           DT_INT16, DT_DOUBLE, DT_INT64, DT_UINT16, DT_UINT32,
                           DT_UINT64, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT8, DT_UINT8,
                           DT_INT16, DT_DOUBLE, DT_INT64, DT_UINT16, DT_UINT32,
                           DT_UINT64, DT_COMPLEX64, DT_COMPLEX128}))
    .ATTR(dim, Int, -65530)
    .OP_END_FACTORY_REG(Cross)
```

## Brief

Calculate the cross product of two tensors. 

## Inputs

One inputs, including:
- x1: A tensor. Must be one of the following types:
    float16, float32, int32, int8, uint8, int16, double,
    int64, uint16, uint32, uint64, complex64, complex128. 
- x2: A tensor. Must be one of the following types:
    float16, float32, int32, int8, uint8, int16, double,
    int64, uint16, uint32, uint64, complex64, complex128. 

## Outputs

y: A Tensor with the same type and shape of x1's. 

## Attributes

- dim: the dimination of compute.Defaults to -65530.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32,int8,int16,int32,uint8
- input1 x2: float16,float32,int8,int16,int32,uint8
- output0 y: float16,float32,int8,int16,int32,uint8
### AI CPU
- input0 x1: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 x2: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the Pytorch operator cross. 


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
