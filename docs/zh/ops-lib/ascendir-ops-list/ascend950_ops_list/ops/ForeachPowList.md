# ForeachPowList

```c
REG_OP(ForeachPowList)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .OP_END_FACTORY_REG(ForeachPowList)
```

## Brief

Apply power operation for a scalar with each tensor in a tensor list
in manner of element-wise

## Inputs

Two inputs:
- x1: A tensor list containing multiple tensors
- x2: Another tensor list containing multiple tensorsr

## Outputs

- y: A tensor list which store the tensors whose value are power with the scalars in scalar list

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32,int32
- input1 x2: bfloat16,float16,float32,int32
- output0 y: bfloat16,float16,float32,int32


---

[Back to Operator Specifications (Ascend950)](../README.md)
