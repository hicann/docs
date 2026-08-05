# Index

```c
REG_OP(Index)
    .INPUT(x, TensorType::BasicType())
    .INPUT(indexed_sizes, TensorType({DT_INT64}))
    .INPUT(indexed_strides, TensorType({DT_INT64}))
    .DYNAMIC_INPUT(indices, TensorType({DT_INT64, DT_INT32}))
    .OUTPUT(y, TensorType::BasicType())
    .OP_END_FACTORY_REG(Index)
```

## Brief

According to the indices, return the value.

## Inputs

Four inputs, including:
- x: A ND Tensor. Must be one of the following types: int64, int32, float32, float16, bfloat16, int8, uint8, bool.
- indexed_sizes: A 1D Tensor of int64 with shape (N). Sizes for each one of the indexed data.
- indexed_strides: A 1D Tensor of int64 with shape (N). Strides for each one of the indexed data.
- indices: Dynamic input. A ND Tensor of int64/int32. return the value according to the indices.

## Outputs

y: The indexed output tensor. Has the same type and format as input "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool,float16,float32,int8,int32,int64,uint8
- input1 indexed_sizes: int64
- input2 indexed_strides: int64
- input3 indices: int32,int64
- output0 y: bool,float16,float32,int8,int32,int64,uint8

## Attention Constraints

- The value in indexed_sizes Tensor is 0 or 1, where 1 indicates that the corresponding dimension in x is indexed.
    Must not be all zeros (at least one dimension must be indexed).
- Based on whether all the 1s in indexed_sizes are consective, it is categorized into a continuous axis scenario and a non-continuous axis scenario.
    Examples of the continuous axis scenario are as follows: x shape=(a, b, c, d), only 2 dim in the middle are indexed, indexed_sizes=[0, 1, 1, 0] indices shape (e, f）
    The value range of indices is [-b, b-1], [-c, c-1], then y shape is (a, e, f, d). Examples of the non-continuous axis scenario are as follows:x shape=(a, b, c, d),
    only the first and the third dim are indexed, indexed_sizes=[1, 0, 1, 0], indices shape=(e, f), then y shape is (e, f, b, d)


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
