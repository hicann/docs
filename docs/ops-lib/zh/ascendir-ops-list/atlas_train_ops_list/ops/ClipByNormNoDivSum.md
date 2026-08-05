# ClipByNormNoDivSum

```c
REG_OP(ClipByNormNoDivSum)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(greater_zeros, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(select_ones, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(maximum_ones, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OP_END_FACTORY_REG(ClipByNormNoDivSum)
```

## Brief

Performs element-wise ClipByNormNoDivSum operation.
      y = Max(Select(x <= greater_zeros, x, Sqrt(Select(x > greater_zeros, x, select_ones))), maximum_ones)
      All inputs support NumPy-style broadcast.

## Inputs

- x: An ND Tensor. Must be one of the following types: float16, float32.
- greater_zeros: An ND Tensor. Same dtype as x.
- select_ones: An ND Tensor. Same dtype as x.
- maximum_ones: An ND Tensor. Same dtype as x.

## Outputs

- y: An ND Tensor. Same dtype and shape as broadcasted inputs.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 greater_zeros: float16,float32
- input2 select_ones: float16,float32
- input3 maximum_ones: float16,float32
- output0 y: float16,float32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
