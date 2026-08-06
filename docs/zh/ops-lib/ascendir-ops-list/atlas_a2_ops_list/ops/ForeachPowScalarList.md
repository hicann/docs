# ForeachPowScalarList

```c
REG_OP(ForeachPowScalarList)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .INPUT(scalars, TensorType({DT_FLOAT, DT_INT64}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .OP_END_FACTORY_REG(ForeachPowScalarList)
```

## Brief

Apply power operation for each tensor in tensor list with a list of scalar in manner
of element-wise the number of tensors in tensor list shall be equal to the number of scalars
in scalar list

## Inputs

Two inputs:
- x: A tensor list containing multiple tensors
- scalars: A scalar list in form of tensor with only multiple elements

## Outputs

- y: A tensor list which store the tensors whose value are power with the scalars in scalar list

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int32
- input1 scalars: float32,int64
- output0 y: bfloat16,float16,float32,int32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
