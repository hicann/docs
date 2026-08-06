# ResizeGradD

```c
REG_OP(ResizeGradD)
    .INPUT(grads, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(original_size, ListInt)
    .ATTR(roi, ListInt, {})
    .ATTR(scales, ListFloat, {})
    .ATTR(coordinate_transformation_mode, String, "half_pixel")
    .ATTR(cubic_coeff_a, Float, -0.75)
    .ATTR(exclude_outside, Int, 0)
    .ATTR(extrapolation_value, Float, 0.0)
    .ATTR(mode, String, "nearest")
    .ATTR(nearest_mode, String, "round_prefer_floor")
    .ATTR(data_format, String, "NCHW")
    .OP_END_FACTORY_REG(ResizeGradD)
```

## Brief

Calculate the resize_grad_d function. 

## Inputs

One input, including:
grads: A 4D tensor, indicating the original size. Must be one of the following types:
float16, float32. The format must be NCHW. 

## Outputs

y: A 4D tensor, indicating the target size. Must have the same type and format as grads.
Shape depends on grads and original_size. 

## Attributes

- original_size: A required listInt. Shape of original_image.
- When mode is set to cubic, original_size supports four numbers.
The first two numbers are the same as the first two numbers of the input shape,
and the last two numbers are the same as the last two numbers of the output shape.
- When mode is set to linear, the value of original_size can be three numbers.
The first two numbers are the same as the first two numbers of the input shape,
and the second number is the same as the last number of the output shape.
- roi: An optional listInt.
Represents the coordinates that are normalized in the coordinate system of the input image.
1-D tensor given as [start1, ..., startN, end1, ..., endN], where N is the rank of X.
It only takes effect when coordinate_transformation_mode is "tf_crop_and_resize".
Defaults to none.
- scales: An optional listFloat. Array of scaling factors for each dimension.
It takes value greater than 0. If it's less than 1, it's sampling down, otherwise, it's upsampling.
Defaults to none.
- When mode is set to cubic, only one of 'scales' and 'original_size' can be specified.
If 'original_size' is specified, then set the scales to empty data (zero shape) in the input list of this operator.
- When mode is set to linear, the value of scales is: the last dimension of grads divided by the last dimension of original_size.
- coordinate_transformation_mode: An optional String.
This attribute describes how to transform the coordinate in the resized tensor
to the coordinate in the original tensor.
Support "half_pixel" and "align_corners". Defaults to "half_pixel".
- cubic_coeff_a: An optional float.
Indicates the calculation weight coefficient of the interpolation.
Two common choice are -0.5 (in some cases of TensorFlow) and -0.75 (in PyTorch).
This attribute is valid only if "mode" is "cubic".
Defaults to -0.75.
- exclude_outside: An optional int.
Whether input parameter excludes out-of-range points during interpolation.
If set to 1, the weight of sampling locations outside the tensor will be set to 0
and the weight will be renormalized so that their sum is 1.0.
Defaults to 0.
- extrapolation_value: An optional float.
The fill value used when the interpolation point is out of the data range.
When coordinate_transformation_mode is "tf_crop_and_resize" and x_original is outside
the range [0, length_original - 1], this value is used as the corresponding output value.
Defaults to 0.0.
- mode: An optional String. ResizeGradD interpolation mode.
Support "nearest", "linear" and "cubic". Defaults to "nearest".
Currently, this parameter cannot be set to nearest.
When mode is set to linear, the H axis of the operator input tensor must be 1.
- nearest_mode: An optional String. When processing non-integer coordinates,
the nearest neighbor interpolation selects the processing mode of the nearest pixel.
Only used by nearest interpolation.
Support "round_prefer_floor" and "round_prefer_ceil". Defaults to "round_prefer_floor".
- data_format: An optional String. Format of the input data converted during calculation.
Support "NCHW" and "HWNC". Defaults to "NCHW".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: float16,float32
- output0 y: float16,float32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
