# ForeachTernaryOp

```c
REG_OP(ForeachTernaryOp)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT, DT_INT16, DT_INT32, DT_FLOAT16, DT_BF16, DT_COMPLEX32, DT_COMPLEX64}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT, DT_INT16, DT_INT32, DT_FLOAT16, DT_BF16, DT_COMPLEX32, DT_COMPLEX64}))
    .DYNAMIC_INPUT(x3, TensorType({DT_FLOAT, DT_INT16, DT_INT32, DT_FLOAT16, DT_BF16, DT_COMPLEX32, DT_COMPLEX64}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .REQUIRED_ATTR(op_code, Int)
    .OP_END_FACTORY_REG(ForeachTernaryOp)
```

## Brief

Provide the universal template for foreach operators, which have three tensorlist inputs,
and one tensorlist output.

## Inputs

- x1: A tensor list containing multiple tensors, can be bfloat16, float16, float, int32,
int16, complex64, complex32.
- x2: A tensor list containing multiple tensors. dtype and format of input1 are same as x1.
- x3: A tensor list containing multiple tensors. dtype and format of input2 are same as x1.

## Outputs

y:A tensor list containing multiple tensors. dtype and format of output are same as x1.

## Required Attributes

op_code: Determine operator type.Each number represents an operator, Please refer to API related materials.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
