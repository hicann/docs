# StatelessRandomChoiceWithMask

```c
REG_OP(StatelessRandomChoiceWithMask)
    .INPUT(x, TensorType({DT_BOOL}))
    .INPUT(count, TensorType({DT_INT32}))
    .INPUT(seed, TensorType({DT_INT64}))
    .INPUT(offset, TensorType({DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT32}))
    .OUTPUT(mask, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(StatelessRandomChoiceWithMask)
```

## Brief

Generate stateless random choice for tensor input . 

## Inputs

include:
- x: 1-D. The shape of the input tensor. A tensor of type bool.
- count: A tensor of type int32.
must be greater than or equal to 0.
- seed: If seed is set to be -1, and offset is set to be 0, the random number
generator is seeded by a random seed. Otherwise, it is seeded by the given seed.
A tensor of type int64.
- offset: To avoid seed collision. A tensor of type int64.

## Outputs

y: A tensor. The tensor of type support int32.
mask: A tensor. The tensor of type support bool.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool
- input1 count: int32
- input2 seed: int64
- input3 offset: int64
- output0 y: int32
- output1 mask: bool


---

[Back to Operator Specifications (Ascend950)](../README.md)
