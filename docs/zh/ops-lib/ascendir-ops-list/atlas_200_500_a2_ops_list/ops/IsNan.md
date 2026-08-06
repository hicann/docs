# IsNan

```c
REG_OP(IsNan)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(IsNan)
```

## Brief

Returns which elements of x are NaN.

## Inputs

x: A Tensor, Format is ND, Support 1D ~ 8D.
Type must be one of the following types: float16, bfloat16, float32, double.

## Outputs

y: A Tensor of type bool, shape is same as x. Returns which elements of x are isnan

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: bool
### AI CPU
- input0 x: double,float16,float32
- output0 y: bool

## Third-party framework compatibility.

Compatible with tensorflow IsNan operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
