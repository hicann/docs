# ForeachCoshInplace

```c
REG_OP(ForeachCoshInplace)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(ForeachCoshInplace)
```

## Brief

Apply cosh operation for each tensor in a tensor list in manner of element-wise

## Inputs

One inputs:
- x: A tensor list containing multiple tensors meanwhile, this value is also an output


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
