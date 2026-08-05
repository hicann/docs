# PSROIPoolingGradV2D

```c
REG_OP(PSROIPoolingGradV2D)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(rois, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(spatial_scale, Float)
    .REQUIRED_ATTR(output_dim, Int)
    .REQUIRED_ATTR(group_size, Int)
    .REQUIRED_ATTR(input_size, ListInt)
    .OP_END_FACTORY_REG(PSROIPoolingGradV2D)
```

## Brief

Performs Position Sensitive PS ROI Pooling Grad . 

## Inputs

Two inputs, including:
- x: A tensor of type float32, describing the result
feature map . 
- rois: A tensor of type float32, with shape
[batch, 5, rois_num], describing the ROIs, each ROI consists of five
elements: "batch_id", "x1", "y1", "x2", and "y2", which "batch_id" indicates
the index of the input feature map, "x1", "y1", "x2", or "y2" must be
greater than or equal to "0.0" . 

## Outputs

y: A tensor of type float32, describing the feature
map, dimension C1 must be equal to
(int(output_dim+15)/C0))*group_size*group_size.

## Attributes

- output_dim: A required int32, specifying the number of output channels,
must be greater than 0.
- group_size: A required int32, specifying the number of groups to encode
position-sensitive score maps, must be within the range (0, 128).
- spatial_scale: A required float32, scaling factor for mapping the input
coordinates to the ROI coordinates . 
- input_size: A required listInt, mapping the gradinput size: (H, W)

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- input1 rois: float32
- output0 y: float32

## Attention Constraints

x's and y's shape should be NC1HWC0; channel must be group_size squared,
rois_num is a multiple of 16; inputs and output temporily not support float16 type.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
