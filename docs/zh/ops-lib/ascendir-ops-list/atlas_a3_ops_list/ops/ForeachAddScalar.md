# ForeachAddScalar

```c
REG_OP(ForeachAddScalar)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .INPUT(scalar, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT32, DT_BF16}))
    .OP_END_FACTORY_REG(ForeachAddScalar)
```

## Brief

Apply add operation for each tensor in tensor list with a scalar in manner of element-wise

## Inputs

Two inputs:
- x: A tensor list containing multiple tensors, the length cannot exceed 50,
       the dtype can be BFloat16, Float16, Int32 or Float32, and the format support ND.
- scalar: A scalar in form of tensor with only one element,
       the dtype can be Float16, Int32 or Float32, and the format supports ND.

## Outputs

- y: A tensor list which store the tensors whose value are add by the scalar,
       has the same length, dtype and format as input "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int8,int16,int32,uint8
- input1 scalar: float16,float32,int32
- output0 y: bfloat16,float16,float32,int8,int16,int32,uint8


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
