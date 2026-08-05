# RoiExtractor

```c
REG_OP(RoiExtractor)
    .DYNAMIC_INPUT(features, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(rois, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(index, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(finest_scale, Int, 56)
    .ATTR(roi_scale_factor, Float, 0)
    .ATTR(spatial_scale, ListFloat, {1.f / 4, 1.f / 8, 1.f / 16, 1.f / 32})
    .ATTR(pooled_height, Int, 7)
    .ATTR(pooled_width, Int, 7)
    .ATTR(sample_num, Int, 0)
    .ATTR(pool_mode, String, "avg")
    .ATTR(aligned, Bool, true)
    .OP_END_FACTORY_REG(RoiExtractor)
```

## Brief

Obtains the ROI feature matrix from the feature map list. It is a customized fused operator for mmdetection. 

## Inputs

Two inputs, including:
- features: A 5HD Tensor list of type float32 or float16.
- rois: ROI position. A 2D Tensor of float32 or float16 with shape (N, 5). "N" indicates the number of ROIs,
the value "5" indicates the indexes of images where the ROIs are located, "x0", "y0", "x1", and "y1".
- index: Optional input, provided by the operator inserted before fusion-pass under specific models.

## Outputs

output: Outputs the feature sample of each ROI position. The format is 5HD Tensor of type float32 or float16.
The axis N is the number of input ROIs. Axes H, W, and C are consistent with the values of "pooled_height",
"pooled_width", and "features", respectively.

## Attributes

- finest_scale: A optional attribute of type int, specifying the scale of calculate levels of "rois".
- roi_scale_factor: A optional attribute of type float32, specifying the rescaling of "rois" coordinates.
- spatial_scale: A optional attribute of type list float32, specifying the scaling ratio of "features"
to the original image.
- pooled_height: A optional attribute of type int32, specifying the H dimension.
- pooled_width: A optional attribute of type int32, specifying the W dimension.
- sample_num: An optional attribute of type int32, specifying the horizontal and vertical sampling frequency
of each output. If this attribute is set to "0", the sampling frequency is equal to the rounded up value of "rois",
which is a floating point number. Defaults to "0".
- pool_mode: An optional attribute of type string to indicate pooling mode. Defaults to "avg", only supports "avg".
- aligned: An optional attribute of type bool, specifying the align to corner. Defaults to true.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 features: float16,float32
- input1 rois: float16,float32
- input2 index: int32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with mmdetection SingleRoIExtractor operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
