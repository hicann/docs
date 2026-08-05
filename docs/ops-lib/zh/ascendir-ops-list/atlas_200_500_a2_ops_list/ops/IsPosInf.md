# IsPosInf

```c
REG_OP(IsPosInf)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BFLOAT16}))
    .OUTPUT(y, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(IsPosInf)
```

## Brief

Compute element-wise infiniteness, return a boolean tensor.

## Inputs

x: A tensor of type float16, float32, bfloat16, format is ND.

## Outputs

y: A tensor. Has the same shape as x. Returns which elements of x are isposinf,
format is ND, dtype is bool.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: bool

## Attention Constraints

Warning: The dtype of x does not support double now.

## Third-party framework compatibility.

Compatible with the Pytorch operator IsPosInf.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
