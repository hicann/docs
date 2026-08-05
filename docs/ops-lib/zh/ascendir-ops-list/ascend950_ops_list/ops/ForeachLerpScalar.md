# ForeachLerpScalar

```c
REG_OP(ForeachLerpScalar)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(weight, TensorType({DT_FLOAT}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(ForeachLerpScalar)
```

## Brief

Apply lerp operation for each tensor in tensor list with tensors in another tensor list and
a scalar in manner of element-wise

## Inputs

Three inputs:
- x1: A tensor list containing multiple tensors, the length cannot exceed 50,
        the dtype can be BFloat16, Float16 or Float32, and the format support ND.
- x2: Another tensor list containing multiple tensors, must has the same length, dtype and format as input "x1".
- weight: A scalar in form of tensor with only one element,
       the dtype can be Float32, and the format supports ND.

## Outputs

    y: A tensor list which store the tensors whose value are produced by lerp,
       has the same length, dtype and format as input "x1".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- input2 weight: float32
- output0 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
