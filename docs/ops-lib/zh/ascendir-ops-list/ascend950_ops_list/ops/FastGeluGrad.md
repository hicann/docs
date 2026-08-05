# FastGeluGrad

```c
REG_OP(FastGeluGrad)
    .INPUT(dy, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(z, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(FastGeluGrad)
```

## Brief

Computes the gradient for the fast_gelu of "x" .

## Inputs

Two inputs, including:
- dy: A Tensor. Must be one of the following types: bfloat16, float16, float32
- x: A Tensor of the same type as "dy" .

## Outputs

z: A Tensor. Has the same type as "dy".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: bfloat16,float16,float32
- input1 x: bfloat16,float16,float32
- output0 z: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator FastGeluGrad


---

[Back to Operator Specifications (Ascend950)](../README.md)
