# HardSwishGrad

```c
REG_OP(HardSwishGrad)
    .INPUT(grad, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(HardSwishGrad)
```

## Brief

Computes the gradient for the hard_swish of "x" .

## Inputs

Two inputs, including:
- grad: A tensor. Must be one of the following types: float16, float32, bfloat16
- x: A tensor with the same type as "grad" .

## Outputs

y: A tensor with the same type as "grad".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad: bfloat16,float16,float32
- input1 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the Torch operator HardSwishGrad.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
