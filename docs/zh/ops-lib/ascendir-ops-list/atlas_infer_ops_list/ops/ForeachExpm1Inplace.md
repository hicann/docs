# ForeachExpm1Inplace

```c
REG_OP(ForeachExpm1Inplace)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(ForeachExpm1Inplace)
```

## Brief

Apply expm1 operation for each tensor in a tensor list in manner of element-wise

## Inputs

One inputs:
- x: A tensor list containing multiple tensors meanwhile, this value is also an output


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
