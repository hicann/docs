# DiagPart

```c
REG_OP(DiagPart)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_INT64, DT_DOUBLE,
                          DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_INT64, DT_DOUBLE,
                           DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(DiagPart)
```

## Brief

Returns the batched diagonal part of a batched tensor . 

## Inputs

x: A Tensor. Must be one of the following types:
   float16, float32, int32, int64, double, complex64, complex128. Supported format list ["ND"]. 

## Outputs

y: A Tensor. Has the same type as "x". Supported format list ["ND"]. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int32
- output0 y: float16,float32,int32
### AI CPU
- input0 x: double,float16,float32,int32,int64
- output0 y: double,float16,float32,int32,int64

## Third-party framework compatibility

Compatible with the TensorFlow operator DiagPart.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
