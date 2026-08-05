# GridUnnormal

```c
REG_OP(GridUnnormal)
    .INPUT(grid, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(assist, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(diff, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(position, TensorType({DT_INT32}))
    .ATTR(align_corners, Bool, false)
    .OP_END_FACTORY_REG(GridUnnormal)
```

## Brief

This operation unnormalize input Grid, which is usually gennerated by affine_grid.

## Inputs

- grid: flow field grid, 4-D Tensor with shape `[batch, height, width, 2]`.
Must be one of the following types: float16, float32.
- assist: Assist matrix, a 4-D tensor with the same shape and dtype as `grid`.

## Outputs

- diff: Returns 4-D Tensor with the same shape and dtype as `grid`.
- position: Returns 4-D Tensor with the same shape as `grid`.

## Attributes

align_corners: An optional bool. If "true", the centers of the corner
pixels of the input and output tensors are aligned. Defaults to "false" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grid: float16,float32
- input1 assist: float16,float32
- output0 diff: float16,float32
- output1 position: int32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
