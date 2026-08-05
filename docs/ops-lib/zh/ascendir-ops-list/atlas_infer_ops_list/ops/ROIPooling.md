# ROIPooling

```c
REG_OP(ROIPooling)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(rois, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OPTIONAL_INPUT(roi_actual_num, TensorType({DT_INT32}))
    .REQUIRED_ATTR(pooled_h, Int)
    .REQUIRED_ATTR(pooled_w, Int)
    .REQUIRED_ATTR(spatial_scale_h, Float)
    .REQUIRED_ATTR(spatial_scale_w, Float)
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(ROIPooling)
```

## Brief

Performs Region of Interest (ROI) Pooling . 

## Inputs

Three inputs, including:
- x: A tensor of type float16 or float32, describing the feature
map. The data of x must be greater than or equal to "0.0".
- rois: A tensor of type float16 or float32, with 3D shape
[batch, 5, roi_max_num], describing the RIOs. Each ROI consists of five
elements: "batch_id", "x1", "y1", "x2", and "y2", which "batch_id" indicates
the index of the input feature map, "x1", "y1", "x2", or "y2" must be
greater than or equal to "0.0".
roi_max_num must be less than or equal to 6000 and must be divided by 16.
The input data of the rois cannot exceed the width and height range of the x,
otherwise, the accuracy of the output result may not be as expected.
- roi_actual_num: A  optional tensor of type int32, with shape [batch, 8], specifying
the number of ROIs per batch . 

## Outputs

y: A tensor of type float16 or float32, describing the result
feature map . 

## Attributes

- pooled_h: A required int32, specifying the pooled H. Must be greater
than 0.
- pooled_w: A required int32, specifying the pooled W. Must be greater
than 0.
- spatial_scale_h: An required scaling factor for mapping the input
coordinates of height to the ROI coordinates.
- spatial_scale_w: An required scaling factor for mapping the input
coordinates of width to the ROI coordinates . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 rois: float16,float32
- input2 roi_actual_num: int32
- output0 y: float16,float32

## Attention Constraints

For the feature map input:
- If pooled_h = pooled_w = 2, the feature map size must not exceed 50.
- If pooled_h = pooled_w = 3, the feature map size must not exceed 60.
- If pooled_h = pooled_w = 4, the feature map size must not exceed 70.
- If pooled_h = pooled_w = 5, the feature map size must not exceed 70.
- If pooled_h = pooled_w = 6, the feature map size must not exceed 80.
- If pooled_h = pooled_w = 7, the feature map size must not exceed 80.
- If pooled_h = pooled_w = 8, the feature map size must not exceed 80.
- If pooled_h = pooled_w = 9, the feature map size must not exceed 70.
- If pooled_h = pooled_w = 10, the feature map size must not exceed 70.
- If pooled_h = pooled_w = 11, the feature map size must not exceed 70.
- If pooled_h = pooled_w = 12, the feature map size must not exceed 70.
- If pooled_h = pooled_w = 13, the feature map size must not exceed 70.
- If pooled_h = pooled_w = 14, the feature map size must not exceed 70.
- If pooled_h = pooled_w = 15, the feature map size must not exceed 70.
- If pooled_h = pooled_w = 16, the feature map size must not exceed 70.
- If pooled_h = pooled_w = 17, the feature map size must not exceed 50.
- If pooled_h = pooled_w = 18, the feature map size must not exceed 40.
- If pooled_h = pooled_w = 19, the feature map size must not exceed 40.
- If pooled_h = pooled_w = 20, the feature map size must not exceed 40.

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
