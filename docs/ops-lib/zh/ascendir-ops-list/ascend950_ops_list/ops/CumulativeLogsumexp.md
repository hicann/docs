# CumulativeLogsumexp

```c
REG_OP(CumulativeLogsumexp)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(axis, TensorType({DT_INT32, DT_INT64, DT_INT16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16}))
    .ATTR(exclusive, Bool, false)
    .ATTR(reverse, Bool, false)
    .OP_END_FACTORY_REG(CumulativeLogsumexp)
```

## Brief

Computes the cumulative log-sum-exp of the tensor "x" along "axis".

## Inputs

Two inputs, including:
- x: A Tensor. Must be one of the following types: float32, float16.
- axis: A Tensor of type int32, int64 or int16. Specifies the dimension for accumulation.

## Outputs

y: A Tensor. Has the same type and shape as "x".

## Attributes

- exclusive: A bool. Defaults to "false". If "true", performs exclusive cumulative log-sum-exp.
- reverse: A bool. Defaults to "false". If "true", accumulates from the end of the tensor.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 axis: int16,int32,int64
- output0 y: float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
