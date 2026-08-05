# AddRowRanges

```c
REG_OP(AddRowRanges)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(src, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(indices, TensorType({DT_INT32}))
    .OUTPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(AddRowRanges)
```

## Brief

For each row r of x, sum src rows in range [indices[r,0], indices[r,1])
      and add the sum to x(r, :).

## Inputs

Three inputs, including:
- x: A 2D ND Tensor. Must be one of the following types: float32, float16.
- src: A 2D ND Tensor. Must be one of the following types: float32, float16.
       src.shape[1] must equal x.shape[1].
- indices: A 2D ND Tensor of shape (M, 2). Must be of type int32.
       indices[r, 0] is start row, indices[r, 1] is end row (exclusive).
       (-1, -1) or start >= end means empty range (skip). 

## Outputs

x: A 2D ND Tensor. Same shape and dtype as input x.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- input1 src: float32
- input2 indices: int32
- output0 x: float32

## Third-party framework compatibility

Compatible with the Kaldi operator AddRowRanges.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
