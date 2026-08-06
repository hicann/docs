# Sign

```c
REG_OP(Sign)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE, DT_INT32,
                          DT_INT64, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE, DT_INT32,
                           DT_INT64, DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(Sign)
```

## Brief

Computes the sign  of "x". 

## Inputs

x:An ND Tensor of type bfloat16, float16, float32, int32, int64, double,
    complex64, complex128. 

## Outputs

y:An ND Tensor with same type as "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int32
- output0 y: float16,float32,int32
### AI CPU
- input0 x: complex64,complex128,double,float16,float32,int32,int64
- output0 y: complex64,complex128,double,float16,float32,int32,int64

## Third-party framework compatibility

Compatible with the TensorFlow operator Sign.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
