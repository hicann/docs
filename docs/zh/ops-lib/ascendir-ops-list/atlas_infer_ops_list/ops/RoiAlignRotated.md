# RoiAlignRotated

```c
REG_OP(RoiAlignRotated)
    .INPUT(x, TensorType({DT_FLOAT}))
    .INPUT(rois, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(pooled_h, Int)
    .REQUIRED_ATTR(pooled_w, Int)
    .REQUIRED_ATTR(spatial_scale, Float)
    .ATTR(sampling_ratio, Int, 0)
    .ATTR(aligned, Bool, true)
    .ATTR(clockwise, Bool, false)
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(RoiAlignRotated)
```

## Brief

Performs the backpropagation of ROI Align Rotated . 

## Inputs

- x: A tensor of type float32, describing the feature_map.
- rois: A tensor of type float32, with shape(n, 6) with each roi decoded as
(batch_index, center_x, center_y, w, h, angle).
The angle is in radian.

## Outputs

- y: A tensor of type float32, describing the result.

## Attributes

- pooled_h: A required int32, specifying the pooled H. Must be greater
than 0.
- pooled_w: A required int32, specifying the pooled W. Must be greater
than 0.
- spatial_scale: A required float32, scaling factor for mapping the input coordinates
to the ROI coordinates.
- sampling_ratio: A required int32, number of inputs samples to take for each output sample.
0 to take samples densely for current models.
- aligned: A required bool, if False, use the legacy implementation.
If True, align the results more perfectly. Default: True.
- clockwise: A required bool, if True, the angle in each proposal follows a clockwise
fashion in image space,
Otherwise, the angle is counterclockwise. Default: False. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- input1 rois: float32
- output0 y: float32

## Third-party framework compatibility

It has a corresponding operator in MMCV.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
