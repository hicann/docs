# ForeachNorm

```c
REG_OP(ForeachNorm)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(scalar, TensorType({DT_FLOAT, DT_INT64}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(ForeachNorm)
```

## Brief

Apply norm operation for each tensor in a tensor list in manner of element-wise

## Inputs

Two inputs:
- x: A tensor list containing multiple tensors. Shape dimension cannot be greater than 8 dimensions.
Format supports ND, and data type must be float16, float32 or bfloat16. The list supports a maximum length of 256.
- scalar: A scalar with one element, indicating the order of norm.
Format supports ND, and data type must be int64, float32.

## Outputs

y: A tensor list which store the tensors whose value are the norm value of the x.
Shape dimension cannot be greater than 8 dimensions, and shapesize should be 1.
Format supports ND, and data type must be float16, float32 or bfloat16. The list supports a maximum length of 256.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 scalar: float32,int64
- output0 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
