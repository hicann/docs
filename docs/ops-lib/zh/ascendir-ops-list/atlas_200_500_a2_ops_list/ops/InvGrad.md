# InvGrad

```c
REG_OP(InvGrad)
    .INPUT(x, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16, DT_INT32, DT_INT8}))
    .INPUT(grad, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16, DT_INT32, DT_INT8}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16, DT_INT32, DT_INT8}))
    .OP_END_FACTORY_REG(InvGrad)
```

## Brief

Computes "x" reciprocal grad, dx = -1*dy*y*y, where, "y = 1/x",
and "dy" is the corresponding input gradient.  Support broadcasting operations.

## Inputs

Two inputs, including:
- x: A ND Tensor. Must be one of the following types: float16, float32, bfloat16.
int32, int8.
- grad: A ND Tensor. Has the same dtype as "x".

## Outputs

y: A ND Tensor, Has the same dtype as "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8,int32
- input1 grad: float16,float32,int8,int32
- output0 y: float16,float32,int8,int32
### AI CPU
- output0 y: complex64,complex128,double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator InvGrad.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
