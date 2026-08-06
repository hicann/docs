# EnsureShape

```c
REG_OP(EnsureShape)
    .INPUT(input, TensorType({DT_INT8,DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_INT64, DT_FLOAT16, \
                            DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(output, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_INT64, DT_FLOAT16, \
                            DT_FLOAT,DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .REQUIRED_ATTR(shape, ListInt)
    .OP_END_FACTORY_REG(EnsureShape)
```

## Brief

Ensures that the tensor's shape matches the expected shape. 

## Inputs

input: A Tensor. that need to be checked with desired shape
       Must be one of the following types:
       int8, uint8, int16, uint16, int32, int64, float16, float,
       double, complex64, complex128 

## Outputs

output: A tensor. has the same type and contents as input
       Must be one of the following types:
       int8, uint8, int16, uint16, int32, int64, float16, float,
       double, complex64, complex128 

## Attributes

shape: required, a desired tensor shape. type: list int 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output0 output: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
