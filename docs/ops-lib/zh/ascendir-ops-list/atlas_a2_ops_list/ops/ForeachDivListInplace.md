# ForeachDivListInplace

```c
REG_OP(ForeachDivListInplace)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(ForeachDivListInplace)
```

## Brief

Apply Div operation for each tensor in a tensor list with each tensor in another
tensor list in manner of element-wise

## Inputs

Two inputs:
- x1: A tensor list containing multiple tensors
meanwhile, this value is also an output, store the value Div by the scalar.
- x2: Another tensor list containing multiple tensors

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32
- input1 x2: float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
