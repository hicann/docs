# ForeachDivScalarInplace

```c
REG_OP(ForeachDivScalarInplace)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(scalar, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(ForeachDivScalarInplace)
```

## Brief

Apply div operation for each tensor in tensor list with a scalar in manner of element-wise

## Inputs

Two inputs:
- x: A tensor list containing multiple tensors
meanwhile, this value is also an output, store the value div by the scalar.
- scalar: A scalar in form of tensor with only one element, the shape must be (1,)


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
