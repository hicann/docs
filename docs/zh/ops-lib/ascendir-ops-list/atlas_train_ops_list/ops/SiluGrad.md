# SiluGrad

```c
REG_OP(SiluGrad)
    .INPUT(dy, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(dx, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(SiluGrad)
```

## Brief

Computes the gradient for the Silu of "x" .

## Inputs

Two inputs, including:
- dy: A tensor, which supports 1D-8D defaultly. Format support ND. Must be one of the following types: float16, bfloat16, float32.
- x: A tensor of the same type, shape and format as "dy".

## Outputs

dx: A tensor of the same type, shape and format as "dy".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: float16,float32
- input1 x: float16,float32
- output0 dx: float16,float32

## Third-party framework compatibility

Compatible with the Torch operator SiluGrad


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
