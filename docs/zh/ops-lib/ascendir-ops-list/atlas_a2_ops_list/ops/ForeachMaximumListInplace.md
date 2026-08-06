# ForeachMaximumListInplace

```c
REG_OP(ForeachMaximumListInplace)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .OP_END_FACTORY_REG(ForeachMaximumListInplace)
```

## Brief

Apply maximum operation for each tensor in a tensor list with each tensor in another
tensor list in manner of element-wise

## Inputs

Two inputs:
- x1: A tensor list containing multiple tensors
meanwhile, this value is also an output, store the value maximum with the scalar.
- x2: Another tensor list containing multiple tensors


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
