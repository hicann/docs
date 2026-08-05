# FusedMulAddAdd

```c
REG_OP(FusedMulAddAdd)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .INPUT(x3, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .INPUT(x4, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .OP_END_FACTORY_REG(FusedMulAddAdd)
```

## Brief

Fused multiply-add-add: y = x1 * x2 + x3 + x4, element-wise. x1 must carry
       the full output shape; x2, x3 and x4 are broadcast up to x1 (NumPy rules).

## Inputs

Four inputs, including:
- x1: A ND tensor. Must be one of the following types: float16, float32, int32.
    Its shape is the output shape.
- x2: A ND tensor. Must have the same dtype as x1; shape must be broadcastable up to x1.
- x3: A ND tensor. Must have the same dtype as x1; shape must be broadcastable up to x1.
- x4: A ND tensor. Must have the same dtype as x1; shape must be broadcastable up to x1.

## Outputs

y: A ND tensor. Has the same dtype and shape as x1. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32,int32
- input1 x2: float16,float32,int32
- input2 x3: float16,float32,int32
- input3 x4: float16,float32,int32
- output0 y: float16,float32,int32

## Attention Constraints

The runtime currently requires x1 to be the full output shape. Cases where x1 itself
must be broadcast up (i.e. x1 is smaller than the output, e.g. x1=[1] with x3=[3,4])
are not supported and fail at runtime.

## Third-party framework compatibility

Compatible with the graph fusion of Mul followed by two Add operators
(e.g. BatchMatmul + bias + residual patterns).


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
