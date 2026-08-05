# ForeachAddcdivScalarInplace

```c
REG_OP(ForeachAddcdivScalarInplace)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16}))
    .DYNAMIC_INPUT(x3, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(scalars, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(ForeachAddcdivScalarInplace)
```

## Brief

Apply AddcDiv operation for each tensor in tensor list with a scalar in manner
of element-wise

## Inputs

Three inputs:
- x1: A tensor list containing multiple tensors, which is also used for the output
- x2: Second tensor list containing multiple tensors
- x3: Third tensor list containing multiple tensors
- scalar: A scalar value


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
