# ForeachUnaryWithScalarOp

```c
REG_OP(ForeachUnaryWithScalarOp)
    .DYNAMIC_INPUT(x1, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .INPUT(x2, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .REQUIRED_ATTR(op_code, Int)
    .OP_END_FACTORY_REG(ForeachUnaryWithScalarOp)
```

## Brief

Provide the universal template for foreach operators, which have one tensorlist input,
and a scalar input.

## Inputs

x1: A tensor list containing multiple tensors, can be bfloat16, float16, float, int32.
x2: A scalar, dtype and format of alpha are same as x1.

## Outputs

y:A tensor list containing multiple tensors. dtype and format of output are same as x1.

## Required Attributes

op_code: Determine operator type.


---

[Back to Operator Specifications (Ascend950)](../README.md)
