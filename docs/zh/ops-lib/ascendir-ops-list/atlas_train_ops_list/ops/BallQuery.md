# BallQuery

```c
REG_OP(BallQuery)
    .INPUT(xyz, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(center_xyz, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(idx, TensorType({DT_INT32}))
    .REQUIRED_ATTR(min_radius, Float)
    .REQUIRED_ATTR(max_radius, Float)
    .REQUIRED_ATTR(sample_num, Int)
    .OP_END_FACTORY_REG(BallQuery)
```

## Brief

Find nearby points in spherical space or spherical layer. 

## Inputs

Two inputs, including:
- xyz: A 3D Tensor of type float16 or float32, xyz coordinates of the features.
- center_xyz: A 3D Tensor of type float16 or float32. centers coordinates of the ball query.

## Outputs

One outputs:
- idx: A 3D(B, M, sample_num) Tensor of type int32 with the indices of the features that form the query balls.

## Attributes

- min_radius: A required float, minimum radius of the balls.
- max_radius: A required float, maximum radius of the balls.
- sample_num: A required int, maximum number of features in the balls.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 xyz: float16,float32
- input1 center_xyz: float16,float32
- output0 idx: int32

## Third-party framework compatibility

Compatible with the MMCV operator BallQuery(BallQuery branch).


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
