# CaseCondition

```c
REG_OP(CaseCondition)
    .INPUT(x, TensorType({DT_INT32, DT_INT64, DT_UINT64}))
    .OUTPUT(y, TensorType({DT_INT32}))
    .ATTR(algorithm, String, "LU")
    .OP_END_FACTORY_REG(CaseCondition)
```

## Brief

x[0] is i, x[1] is j and x[2] is k when algorithm is LU,
y = 0 when i >= k && j < k,
y = 1 when i == k && j == k,
y = 2 when i > k && j == k,
y = 3 when i == k && j > k,
y = 4 when i > k && j > k,
default y = 5
use for lu decomposition

## Inputs

x: A Tensor of type int32/int64/uint64. 

## Outputs

y: A Tensor of type int32.

## Attributes

algorithm: A string, only support LU now.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: int32,int64,uint64
- output0 y: int32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
