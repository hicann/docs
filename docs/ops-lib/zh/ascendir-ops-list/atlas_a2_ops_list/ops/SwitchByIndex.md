# SwitchByIndex

```c
REG_OP(SwitchByIndex)
    .INPUT(x1, TensorType({DT_INT32}))
	.INPUT(x2, TensorType({DT_UINT64}))
    .OP_END_FACTORY_REG(SwitchByIndex)
```

## Brief

Writes the input data of the corresponding subscript to the specified register.

## Inputs

Two inputs:
- x1: A 1D tensor, dtype is int32, format is ND, shape is (1,).
- x2: A 1D tensor, dtype is uint64, the format is ND.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
