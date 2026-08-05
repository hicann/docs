# ForeachLerpList

```c
REG_OP(ForeachLerpList)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DYNAMIC_INPUT(weight, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(ForeachLerpList)
```

## Brief

Apply lerp operation for each tensor in tensor list with tensors in another tensor list and
an additonal tensor in manner of element-wise

## Inputs

Three inputs:
- x1: A tensor list containing multiple tensors
- x2: Another tensor list containing multiple tensors
- weights: A tensor contain multiple elements

## Outputs

- y: A tensor list which store the tensors whose value are produced by lerp

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- input2 weight: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
