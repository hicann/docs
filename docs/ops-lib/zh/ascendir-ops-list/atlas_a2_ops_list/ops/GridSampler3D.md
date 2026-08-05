# GridSampler3D

```c
REG_OP(GridSampler3D)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(grid, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .ATTR(interpolation_mode, String, "bilinear")
    .ATTR(padding_mode, String, "zeros")
    .ATTR(data_format, String, "NCDHW")
    .ATTR(align_corners, Bool, false)
    .OP_END_FACTORY_REG(GridSampler3D)
```

## Brief

This operation samples 3d input x by using interpolation based on
flow field grid, which is usually gennerated by affine_grid.

## Inputs

- x: 5-D Tensor with shape `[batch, channels, depth, height, width]`.
Must be one of the following types: float16, float, double.
The format support NDHWC, NCDHW, ND.
- grid: flow field grid, 5-D Tensor with shape `[batch, depth, height,
width, 3]` and has same dtype as `x`. The format support ND.
Must be one of the following types: float16, float, double. 

## Outputs

y: Returns 5-D Tensor with the same format and dtype as `x`.
Must be one of the following types: float16, float, double.
The format support NDHWC, NCDHW, ND. 

## Attributes

- interpolation_mode: An optional string specifying the interpolation
method, either 'bilinear' or 'nearest'. Defaults to "bilinear".
- padding_mode: An optional string specifying the pad method,
either 'zeros', 'border' or 'reflection'. Defaults to "zeros".
- data_format: An optional string specifying the data formats,
either 'NCDHW', 'NDHWC' or 'ND'. Defaults to "NCDHW".
- align_corners: An optional bool. If "true", the centers of the corner
pixels of the input and output tensors are aligned. Defaults to "false" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- input1 grid: float32
- output0 y: float32
### AI CPU
- input0 x: double,float16,float32
- input1 grid: double,float16,float32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with pytorch GridSampler3D operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
