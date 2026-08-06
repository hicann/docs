# ForeachUnaryOp

```c
REG_OP(ForeachUnaryOp)
    .DYNAMIC_INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .REQUIRED_ATTR(op_code, Int)
    .OP_END_FACTORY_REG(ForeachUnaryOp)
```

## Brief

Provide the universal template for foreach operators, which have one tensorlist input,
and one tensorlist output.

## Inputs

x: A tensor list containing multiple tensors, can be bfloat16, float16, float, int32.

## Outputs

y:A tensor list containing multiple tensors. dtype and format of output are same as x1.

## Required Attributes

op_code: Determine operator type.Each number represents an operator, Please refer to API related materials.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
