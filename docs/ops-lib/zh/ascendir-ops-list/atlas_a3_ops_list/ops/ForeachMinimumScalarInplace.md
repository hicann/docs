# ForeachMinimumScalarInplace

```c
REG_OP(ForeachMinimumScalarInplace)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .INPUT(scalar, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .OP_END_FACTORY_REG(ForeachMinimumScalarInplace)
```

## Brief

Apply minimum operation for each tensor in tensor list with a scalar in manner of element-wise

## Inputs

Two inputs:
- x: A tensor list containing multiple tensors
meanwhile, this value is also an output, store the value minimum with the scalar.
- scalar: A scalar in form of tensor with only one element, the shape must be (1,)


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
