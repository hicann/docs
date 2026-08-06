# ActiveRotatedFilter

```c
REG_OP(ActiveRotatedFilter)
    .INPUT(x, TensorType({DT_FLOAT16,DT_FLOAT,DT_INT32}))
    .INPUT(indices, TensorType({DT_INT32,DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16,DT_FLOAT,DT_INT32}))
    .OP_END_FACTORY_REG(ActiveRotatedFilter)
```

## Brief

Encoding the orientation information and generating orientation-sensitive features. 

## Inputs

Two inputs, including:
- x: Input features with shape [num_output_planes, num_input_planes, num_orientations, H, W].
- indices: Indices with shape [num_orientations, H, W, num_rotations].

## Outputs

One output, including:
- y: Refined features with shape [num_output_planes * num_rotations, num_input_planes * num_orientations, H, W].

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: float16,float32,int32
- input1 indices: int32,int64
- output0 y: float16,float32,int32

## Third-party framework compatibility

Compatible with the mmcv operator ActiveRotatedFilter.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
