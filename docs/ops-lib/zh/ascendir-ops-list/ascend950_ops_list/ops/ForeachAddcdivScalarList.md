# ForeachAddcdivScalarList

```c
REG_OP(ForeachAddcdivScalarList)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DYNAMIC_INPUT(x3, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(scalars, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(ForeachAddcdivScalarList)
```

## Brief

Apply AddcDiv operation for each tensor in tensor list with a list of scalar in manner
of element-wise the number of tensors in tensor list shall be equal to the number of scalars
in scalar list

## Inputs

Four inputs:
- x1: A tensor list containing multiple tensors
- x2: Second tensor list containing multiple tensors
- x3: Third tensor list containing multiple tensors
- scalars: A list of scalar value

## Outputs

- y: A tensor list which store the tensors whose value are AddcDiv with the scalar

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- input2 x3: bfloat16,float16,float32
- input3 scalars: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
