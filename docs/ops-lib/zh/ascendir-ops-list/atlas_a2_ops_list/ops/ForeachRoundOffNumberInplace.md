# ForeachRoundOffNumberInplace

```c
REG_OP(ForeachRoundOffNumberInplace)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(roundMode, TensorType({DT_INT8}))
    .OP_END_FACTORY_REG(ForeachRoundOffNumberInplace)
```

## Brief

round off number foreach element in each tensor in tesnorlist, this is an in-place operation.

## Inputs

Two inputs
- x: A tensor list containing multiple tensors, can be float16, float.
- roundMode: mode of round off which currently supports 2(floor) and 3(ceil).


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
