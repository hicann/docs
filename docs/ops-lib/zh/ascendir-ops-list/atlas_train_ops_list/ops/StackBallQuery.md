# StackBallQuery

```c
REG_OP(StackBallQuery)
    .INPUT(xyz, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(center_xyz, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(xyz_batch_cnt, TensorType({DT_INT32, DT_INT64}))
    .INPUT(center_xyz_batch_cnt, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(idx, TensorType({DT_INT32}))
    .REQUIRED_ATTR(max_radius, Float)
    .REQUIRED_ATTR(sample_num, Int)
    .OP_END_FACTORY_REG(StackBallQuery)
```

## Brief

Find nearby points in spherical space. 

## Inputs

Four inputs, including:
- xyz: A 2D Tensor of type float16 or float32, xyz coordinates of the features.
- center_xyz: A 2D Tensor of type float16 or float32. Centers coordinates of the ball query.
- xyz_batch_cnt: A 1D Tensor of type int32 or int64, Stacked input xyz coordinates nums in
each batch, just like (N1, N2, ...).
- center_xyz_batch_cnt: A 1D Tensor of type int32 or int64. Stacked input centers coordinates nums in
each batch, just like (M1, M2, ...). 

## Outputs

One outputs:
- idx: A 2D(M, sample_num) Tensor of type int32 with the indices of the features that form the query balls.

## Attributes

- max_radius: A required float, maximum radius of the balls.
- sample_num: A required int, maximum number of features in the balls.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 xyz: float16,float32
- input1 center_xyz: float16,float32
- input2 xyz_batch_cnt: int32,int64
- input3 center_xyz_batch_cnt: int32,int64
- output0 idx: int32

## Third-party framework compatibility

Compatible with the MMCV operator BallQuery(StackBallQuery branch).


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
