# MulAddn

```c
REG_OP(MulAddn)
    .DYNAMIC_INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DYNAMIC_INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(N, Int)
    .OP_END_FACTORY_REG(MulAddn)
```

## Brief

Confuse broadcast, addn and n mul operation. Support broadcasting operations.

## Inputs

Two inputs, including:
- x1: A ND tensor. Must be one of the following types:bfloat16 float16, float32.
- x2: A ND tensor of the same dtype as "x1".

## Outputs

@ y: A ND tensor. Has the same dtype as "x1". 

## Attributes

N:Represent the number of fusion mul operations, which is grater than or equal to 2.
The support type is the int.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Attention Constraints

- The third dimension of x1 and the second dimension of x2 are both 1.
- The third dimension of x2 must be less than or equal to 2040.


---

[Back to Operator Specifications (Ascend950)](../README.md)
