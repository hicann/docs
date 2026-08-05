# ForeachDivScalarList

```c
REG_OP(ForeachDivScalarList)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(scalars, TensorType({DT_FLOAT}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(ForeachDivScalarList)
```

## Brief

Apply division operation for each tensor in tensor list with a list of scalar in manner
of element-wise the number of tensors in tensor list shall be equal to the number of scalars
in scalar list.

## Inputs

Two inputs:
- x: A tensor list containing multiple tensors, the length cannot exceed 50,
       the dtype can be BFloat16, Float16 or Float32, and the format support ND.
- scalars: A scalar list in form of tensor with only multiple elements,
       the dtype can be Float32, and the format supports ND.

## Outputs

A tensor list which store the tensors whose value are x divide by the scalars in scalar list,
      has the same length, dtype and format as input "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 scalars: float32
- output0 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
