# ROIAlignGrad

```c
REG_OP(ROIAlignGrad)
    .INPUT(ydiff, TensorType({DT_FLOAT}))
    .INPUT(rois, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(rois_n, TensorType({DT_INT32}))
    .OUTPUT(xdiff, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(xdiff_shape, ListInt)
    .REQUIRED_ATTR(pooled_width, Int)
    .REQUIRED_ATTR(pooled_height, Int)
    .REQUIRED_ATTR(spatial_scale, Float)
    .ATTR(sample_num, Int, 2)
    .ATTR(roi_end_mode, Int, 1)
    .OP_END_FACTORY_REG(ROIAlignGrad)
```

## Brief

Performs the backpropagation of ROIAlign for training scenarios . 

## Inputs

Three inputs, including:
- ydiff: A 5HD gradient input of type float32.
- rois: ROI position. A 2D Tensor of float32 with shape (N, 5). "N" indicates the number of ROIs,
the value "5" indicates the indexes of images where the ROIs are located, "x0", "x1", "y0", and "y1".
- rois_n: An optional input, specifying the number of valid ROIs. This parameter is reserved .

## Outputs

xdiff: Gradient added to input "features". Has the same 5HD shape as input "features".

## Attributes

- xdiff_shape: A required list of 4 ints, obtained based on the shape of "features" of ROIAlign.
- pooled_width: A required attribute of type int, specifying the W dimension.
- pooled_height: A required attribute of type int, specifying the H dimension.
- spatial_scale: A required attribute of type float, specifying the scaling ratio of "features" to the original image.
- sample_num: An optional attribute of type int, specifying the horizontal and vertical
sampling frequency of each output. If this attribute is set to "0", the sampling frequency is
equal to the rounded up value of "rois", which is a floating point number. Defaults to "2" .
- roi_end_mode: An optional attribute of type int, specifying the align mode . Defaults to "1".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 ydiff: float32
- input1 rois: float32
- input2 rois_n: int32
- output0 xdiff: float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
