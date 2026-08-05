# ForeachSignInplace

```c
REG_OP(ForeachSignInplace)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .OP_END_FACTORY_REG(ForeachSignInplace)
```

## Brief

Apply sign operation for each tensor in a tensor list in manner of element-wise

## Inputs

One inputs:
- x: A tensor list containing multiple tensors meanwhile, this value is also an output.
The data type can only be float16, float, int32. The format support ND. Shape support 1D ~ 8D.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
