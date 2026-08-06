# Voxelization

```c
REG_OP(Voxelization)
    .INPUT(points, TensorType({DT_DOUBLE,DT_FLOAT,DT_FLOAT16}))
    .INPUT(voxel_size, TensorType({DT_DOUBLE,DT_FLOAT,DT_FLOAT16}))
    .INPUT(coors_range, TensorType({DT_DOUBLE, DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(voxels, TensorType({DT_DOUBLE,DT_FLOAT,DT_FLOAT16}))
    .OUTPUT(coors, TensorType({DT_INT32}))
    .OUTPUT(num_points_per_voxel, TensorType({DT_INT32}))
    .OUTPUT(voxel_num, TensorType({DT_INT32}))
    .ATTR(max_points, Int, 35)
    .ATTR(max_voxels, Int, 20000)
    .ATTR(deterministic, Bool, true)
    .OP_END_FACTORY_REG(Voxelization)
```

## Brief

Calculate the voxels of cloud points 

## Inputs

Three inputs, including:
- points: the shape is [M, C], points[:3] contain xyz points and points[3:] contain other information.
- voxel_size: the size of voxel with the shape of [3].
- coors_range:the coordinate range of voxel with the shape of [6].

## Outputs

Four outputs, including:
- voxels: the output voxels with the shape of [M, max_points, C].
- coors: the voxel coordinates with shape of [M, 3].
- num_points_per_voxel: the number of points per voxel with the shape of [M].
- voxel_num: the number of voxels.

## Attributes

Three attrs, including:
- max_points: maximum points contained in a voxel.
- max_voxels: maximum voxels this op create.
- deterministic: An optional attr, only support true now, false is faster.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 points: double,float16,float32
- input1 voxel_size: double,float16,float32
- input2 coors_range: double,float16,float32
- output0 voxels: double,float16,float32
- output1 coors: int32
- output2 num_points_per_voxel: int32
- output3 voxel_num: int32

## Third-party framework compatibility

Compatible with the mmcv operator Voxelization.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
