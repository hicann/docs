# ForeachPowScalarAndTensor

```c
REG_OP(ForeachPowScalarAndTensor)
    .INPUT(scalar, TensorType({DT_FLOAT, DT_INT64}))
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .OP_END_FACTORY_REG(ForeachPowScalarAndTensor)
```

## Brief

Apply power operation for each tensor in tensor list with a scalar in manner
of element-wise the number of tensors in tensor list shall be equal to the number of scalars
in scalar list

## Inputs

Two inputs:
- x: A tensor list containing multiple tensors
- scalar: A scalar

## Outputs

- y: A tensor list which store the tensors whose value are power with the scalars in scalar list

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 scalar: float32,int64
- input1 x: bfloat16,float16,float32,int32
- output0 y: bfloat16,float16,float32,int32


---

[Back to Operator Specifications (Ascend950)](../README.md)
