# ForeachLerpListInplace

```c
REG_OP(ForeachLerpListInplace)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(weights, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(ForeachLerpListInplace)
```

## Brief

Apply lerp operation for each tensor in tensor list with tensors in another tensor list and
an additonal tensor in manner of element-wise

## Inputs

Three inputs:
- x1: A tensor list containing multiple tensors. meanwhile, this value is also an output,
store the value produced by lerp.
- x2: Another tensor list containing multiple tensors
- weights: A tensor contain multiple elements


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
