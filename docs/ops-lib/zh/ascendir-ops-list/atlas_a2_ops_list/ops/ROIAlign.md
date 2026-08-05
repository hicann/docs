# ROIAlign

```c
REG_OP(ROIAlign)
    .INPUT(features, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(rois, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(rois_n, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(spatial_scale, Float)
    .REQUIRED_ATTR(pooled_height, Int)
    .REQUIRED_ATTR(pooled_width, Int)
    .ATTR(sample_num, Int, 2)
    .ATTR(roi_end_mode, Int, 1)
    .ATTR(pool_mode, String, "avg")
    .OP_END_FACTORY_REG(ROIAlign)
```

## Brief

Obtains the ROI feature matrix from the feature map. It is a customized FasterRcnn operator . 

## Inputs

Three inputs, including:
- features: A 5HD Tensor of type float32 or float16.
- rois: ROI position. A 2D Tensor of float32 or float16 with shape (N, 5). "N" indicates the number of ROIs,
the value "5" indicates the indexes of images where the ROIs are located,
"x0", "y0", "x1", and "y1".
- rois_n: An optional input of type int32, specifying the number of valid ROIs. This parameter is reserved .

## Outputs

y: Outputs the feature sample of each ROI position. The format is 5HD Tensor of type float32 or float16.
The axis N is the number of input ROIs. Axes H, W, and C are consistent
with the values of "pooled_height",
"pooled_width", and "features", respectively.

## Attributes

- spatial_scale: A required attribute of type float32, specifying the scaling ratio of "features" to the original image.
- pooled_height: A required attribute of type int32, specifying the H dimension.
- pooled_width: A required attribute of type int32, specifying the W dimension.
- sample_num: An optional attribute of type int32, specifying the horizontal and vertical sampling frequency of each output. If this attribute is set to "0",
the sampling frequency is equal to the rounded up value of "rois", which is a floating point number. Defaults to "2".
- roi_end_mode: An optional attribute of type int32, specifying the align mode. Defaults to "1", supports 0/1/2/3.
"0" is compatible with align = False for all frameworks. 
"1" is compatible with align = True for TensorFlow. 
"2" is compatible with align = True for pyTorch. 
"3" is compatible with align = True for MmDetecion v0.6. 
- pool_mode: An optional attribute of type string, specifying the pooling mode. Defaults to "avg", supports "avg" and "max".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 features: float16,float32
- input1 rois: float16,float32
- input2 rois_n: int32
- output0 y: float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
