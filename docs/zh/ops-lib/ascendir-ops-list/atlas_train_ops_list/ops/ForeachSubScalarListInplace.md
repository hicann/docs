# ForeachSubScalarListInplace

```c
REG_OP(ForeachSubScalarListInplace)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .INPUT(scalars, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .OP_END_FACTORY_REG(ForeachSubScalarListInplace)
```

## Brief

Apply sub operation for each tensor in tensor list with a list of scalar in manner
of element-wise the number of tensors in tensor list shall be equal to the number of scalars
in scalar list

## Inputs

Two inputs:
- x: A tensor list containing multiple tensors
meanwhile, this value is also an output, store the value sub by the scalar.
- scalars: A scalar list in form of tensor with only multiple elements


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
