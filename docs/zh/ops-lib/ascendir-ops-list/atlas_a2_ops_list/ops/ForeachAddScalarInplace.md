# ForeachAddScalarInplace

```c
REG_OP(ForeachAddScalarInplace)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .INPUT(scalar, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .OP_END_FACTORY_REG(ForeachAddScalarInplace)
```

## Brief

Apply add operation for each tensor in tensor list with a scalar in manner of element-wise

## Inputs

Two inputs:
- x: A tensor list containing multiple tensors
meanwhile, this value is also an output, store the value add by the scalar.
- scalar: A scalar in form of tensor with only one element, the shape must be (1,)


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
