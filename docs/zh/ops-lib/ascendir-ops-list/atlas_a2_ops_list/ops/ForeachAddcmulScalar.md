# ForeachAddcmulScalar

```c
REG_OP(ForeachAddcmulScalar)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .DYNAMIC_INPUT(x3, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .INPUT(scalar, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .OP_END_FACTORY_REG(ForeachAddcmulScalar)
```

## Brief

Apply AddcMul operation for each tensor in tensor list with a scalar in manner
of element-wise

## Inputs

Three inputs:
- x1: A tensor list containing multiple tensors, the length cannot exceed 50,
        the dtype can be BFloat16, Float16, Int32 or Float32, and the format support ND.
- x2: Second tensor list containing multiple tensors, must has the same length, dtype and format as input "x1".
- x3: Third tensor list containing multiple tensors, must has the same length, dtype and format as input "x1".
- scalar: A scalar in form of tensor with only one element,
       the dtype can be Float16, Int32 or Float32, and the format supports ND.

## Outputs

- y: A tensor list which store the tensors whose value are AddcMul with the scalar,
       has the same length, dtype and format as input "x1".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32,int32
- input1 x2: bfloat16,float16,float32,int32
- input2 x3: bfloat16,float16,float32,int32
- input3 scalar: float16,float32,int32
- output0 y: bfloat16,float16,float32,int32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
