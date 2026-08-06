# ForeachATanInplace

```c
REG_OP(ForeachATanInplace)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(ForeachATanInplace)
```

## Brief

Apply arc tan operation for each tensor in a tensor list in manner of element-wise

## Inputs

One inputs:
- x: A tensor list containing multiple tensors meanwhile, this value is also an output


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
