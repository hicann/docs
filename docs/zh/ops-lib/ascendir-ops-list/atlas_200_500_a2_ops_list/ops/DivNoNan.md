# DivNoNan

```c
REG_OP(DivNoNan)
    .INPUT(x1, TensorType({DT_FLOAT, DT_UINT8, DT_INT8, DT_INT32, DT_FLOAT16,
                           DT_DOUBLE, DT_BF16}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_UINT8, DT_INT8, DT_INT32, DT_FLOAT16,
                           DT_DOUBLE, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_UINT8, DT_INT8, DT_INT32, DT_FLOAT16,
                           DT_DOUBLE, DT_BF16}))
    .OP_END_FACTORY_REG(DivNoNan)
```

## Brief

Returns 0 if the denominator is zero, else, like Div.  Support broadcasting operations.

## Inputs

Two inputs, including:
- x1: A ND Tensor. Must be one of the following types:float16, float32, int32,
   int8, uint8, double, bfloat16.
- x2: A ND Tensor which has the same dtype as "x1". The shapes of "x1", "x2",
   and "y" must comply with the broadcast rule. 

## Outputs

y: A ND Tensor which has the same dtype as "x1".The shapes of "x1", "x2",
and "y" must comply with the broadcast rule. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32,int8,int32,uint8
- input1 x2: float16,float32,int8,int32,uint8
- output0 y: float16,float32,int8,int32,uint8
### AI CPU
- input0 x1: complex64,complex128,double,float16,float32
- input1 x2: complex64,complex128,double,float16,float32
- output0 y: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator DivNoNan.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
