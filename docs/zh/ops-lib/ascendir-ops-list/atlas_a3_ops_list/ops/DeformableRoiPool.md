# DeformableRoiPool

```c
REG_OP(DeformableRoiPool)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(rois, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(offset, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(spatial_scale, Float, 1.0)
    .REQUIRED_ATTR(output_size, ListInt)
    .ATTR(sampling_ratio, Int, 0)
    .ATTR(gamma, Float, 0.1f)
    .OP_END_FACTORY_REG(DeformableRoiPool)
```

## Brief

Obtains the ROI feature matrix from the feature map. It is a customized FasterRcnn operator . 

## Inputs

Three inputs, including:
- features: A 5HD Tensor of type float32 or float16.
- rois: ROI position. A 2D Tensor of float32 or float16 with shape (N, 5). "N" indicates the number of ROIs,
    the value "5" indicates the indexes of images where the ROIs are located, "x0", "y0", "x1", and "y1".
- offset: An optional input of type float32 or float16, offset of height and width defaults to a Tensor of zero .

## Outputs

output: Outputs the feature sample of each ROI position. The format is 5HD Tensor of type float32 or float16.
The axis N is the number of input ROIs. Axes H, W, and C are consistent
with the values of "pooled_height",
"pooled_width", and "features", respectively.

## Attributes

- spatial_scale: A required attribute of type float32, specifying the scaling ratio of "features"
    to the original image.
- pooled_height: A required attribute of type int32, specifying the H dimension.
- pooled_width: A required attribute of type int32, specifying the W dimension.
- sampling_ratio: An optional attribute of type int32, specifying the horizontal and vertical sampling frequency
    of each output. If this attribute is set to "0",
the sampling frequency is equal to the rounded up value of "rois", which is a floating point number. Defaults to "0".
- gamma: An optional attribute of type float32. Defaults to "0.1" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 rois: float16,float32
- input2 offset: float16,float32
- output0 y: float16,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
