# ForeachMulListInplace

```c
REG_OP(ForeachMulListInplace)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .OP_END_FACTORY_REG(ForeachMulListInplace)
```

## Brief

Apply mul operation for each tensor in a tensor list with each tensor in another
tensor list in manner of element-wise

## Inputs

Two inputs:
- x1: A tensor list containing multiple tensors
meanwhile, this value is also an output, store the value mul by the scalar.
- x2: Another tensor list containing multiple tensors

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32,int32
- input1 x2: bfloat16,float16,float32,int32


---

[Back to Operator Specifications (Ascend950)](../README.md)
