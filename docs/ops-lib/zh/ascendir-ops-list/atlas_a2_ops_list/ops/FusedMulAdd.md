# FusedMulAdd

```c
REG_OP(FusedMulAdd)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .INPUT(x3, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .OP_END_FACTORY_REG(FusedMulAdd)
```

## Brief

Fused multiply-add: y = x1 * x2 + x3, element-wise with NumPy broadcasting.

## Inputs

Three inputs, including:
- x1: A ND tensor. Must be one of the following types: float16, float32, int32.
- x2: A ND tensor. Must have the same dtype as x1; shape must be broadcastable with x1.
- x3: A ND tensor. Must have the same dtype as x1; shape must be broadcastable with (x1 * x2).

## Outputs

y: A ND tensor. Has the same dtype as x1; shape is the broadcast shape of x1, x2 and x3. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32,int32
- input1 x2: float16,float32,int32
- input2 x3: float16,float32,int32
- output0 y: float16,float32,int32

## Third-party framework compatibility

Compatible with TensorFlow/PyTorch graph fusion of Mul followed by Add.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
