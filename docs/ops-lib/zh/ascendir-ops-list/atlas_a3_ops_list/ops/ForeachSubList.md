# ForeachSubList

```c
REG_OP(ForeachSubList)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .INPUT(alpha, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .OP_END_FACTORY_REG(ForeachSubList)
```

## Brief

Apply sub operation for each tensor in a tensor list with each tensor in another
tensor list in manner of element-wise

## Inputs

Three inputs:
- x1: A tensor list containing multiple tensors
- x2: Another tensor list containing multiple tensors
- alpha: The elements in x2 should perform multipy with alpha which is a scalar

## Outputs

- y: A tensor list which store the tensors whose value are sub by the scalars in scalar list

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32,int32
- input1 x2: bfloat16,float16,float32,int32
- input2 alpha: float16,float32,int32
- output0 y: bfloat16,float16,float32,int32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
