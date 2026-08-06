# IsInf

```c
REG_OP(IsInf)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .OUTPUT(y, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(IsInf)
```

## Brief

Compute element-wise infiniteness, return a boolean tensor.

## Inputs

x: A Tensor of type float16, float32, double, bfloat16, format is ND.

## Outputs

y: A Tensor. Has the same shape as x. Returns which elements of x are isinf, format is ND, dtype is bool.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32
- output0 y: bool

## Third-party framework compatibility.

Compatible with tensorflow IsInf operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
