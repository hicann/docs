# ForeachTernaryWithScalarOp

```c
REG_OP(ForeachTernaryWithScalarOp)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT, DT_INT16, DT_INT32, DT_FLOAT16, DT_BF16, DT_COMPLEX32, DT_COMPLEX64}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT, DT_INT16, DT_INT32, DT_FLOAT16, DT_BF16, DT_COMPLEX32, DT_COMPLEX64}))
    .DYNAMIC_INPUT(x3, TensorType({DT_FLOAT, DT_INT16, DT_INT32, DT_FLOAT16, DT_BF16, DT_COMPLEX32, DT_COMPLEX64}))
    .INPUT(x4, TensorType({DT_FLOAT, DT_INT16, DT_INT32, DT_FLOAT16, DT_BF16, DT_COMPLEX32, DT_COMPLEX64}))
    .DYNAMIC_OUTPUT(y, TensorType({DT_FLOAT, DT_INT16, DT_INT32, DT_FLOAT16, DT_BF16, DT_COMPLEX32, DT_COMPLEX64}))
    .REQUIRED_ATTR(op_code, Int)
    .OP_END_FACTORY_REG(ForeachTernaryWithScalarOp)
```

## Brief

Provide the universal template for foreach operators, which have three tensorlist inputs,
one scalar input, and one output.

## Inputs

- x1: A tensor list containing multiple tensors, can be bfloat16, float16, float, int32,
int16, complex64, complex32.
- x2: A tensor list containing multiple tensors. dtype and format of input1 are same as x1.
- x3: A tensor list containing multiple tensors. dtype and format of input2 are same as x1.
- x4: A scalar, dtype and format of alpha are same as x1.

## Outputs

y:A tensor list containing multiple tensors. dtype and format of output are same as x1.

## Required Attributes

op_code: Determine operator type.Each number represents an operator, Please refer to API related materials.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
