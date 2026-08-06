# ForeachAddListInplace

```c
REG_OP(ForeachAddListInplace)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .OPTIONAL_INPUT(alpha, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .OP_END_FACTORY_REG(ForeachAddListInplace)
```

## Brief

Apply add operation for each tensor in a tensor list with each tensor in another
tensor list in manner of element-wise

## Inputs

Three inputs:
- x1: A tensor list containing multiple tensors
meanwhile, this value is also an output, store the value add by the scalar.
- x2: Another tensor list containing multiple tensors
- alpha: The elements in x2 should perform multipy with alpha which is a scalar

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32,int32
- input1 x2: float16,float32,int32
- input2 alpha: float16,float32,int32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
