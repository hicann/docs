# ForeachLerpScalarInplace

```c
REG_OP(ForeachLerpScalarInplace)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(weight, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(ForeachLerpScalarInplace)
```

## Brief

Apply lerp operation for each tensor in tensor list with tensors in another tensor list and
a scalar in manner of element-wise

## Inputs

Three inputs:
- x1: A tensor list containing multiple tensors. meanwhile, this value is also an output,
store the value produced by lerp.
- x2: Another tensor list containing multiple tensors
- weight: A scalar in form of tensor with only one element, the shape must be (1,)


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
