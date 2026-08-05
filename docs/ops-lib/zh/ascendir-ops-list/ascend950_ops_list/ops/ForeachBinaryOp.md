# ForeachBinaryOp

```c
REG_OP(ForeachBinaryOp)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT64, DT_BF16, DT_INT16,
                           DT_INT8, DT_UINT8, DT_DOUBLE, DT_COMPLEX128, DT_COMPLEX64, DT_COMPLEX32}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT64, DT_BF16, DT_INT16,
                           DT_INT8, DT_UINT8, DT_DOUBLE, DT_COMPLEX128, DT_COMPLEX64, DT_COMPLEX32}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT64, DT_BF16, DT_INT16,
                           DT_INT8, DT_UINT8, DT_DOUBLE, DT_COMPLEX128, DT_COMPLEX64, DT_COMPLEX32}))
    .REQUIRED_ATTR(op_code, Int)
    .OP_END_FACTORY_REG(ForeachBinaryOp)
```

## Brief

Provide the universal template for foreach operators, which have two tensorlist inputs,
and one tensorlist output.

## Inputs

- x1: A tensor list containing multiple tensors, can be bfloat16, float16, float, int32, int64,
int16, int8, uint8, double, complex128, complex64, complex32.
- x2: A tensor list containing multiple tensors. dtype and format of input1 are same as x1.

## Outputs

y:A tensor list containing multiple tensors. dtype and format of output are same as x1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32,int32
- input1 x2: bfloat16,float16,float32,int32
- output0 y: bfloat16,float16,float32,int32

## Required Attributes

op_code: Determine operator type.Each number represents an operator, Please refer to API related materials.


---

[Back to Operator Specifications (Ascend950)](../README.md)
