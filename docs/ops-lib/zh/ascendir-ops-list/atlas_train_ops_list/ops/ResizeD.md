# ResizeD

```c
REG_OP(ResizeD)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(sizes, ListInt)
    .ATTR(scales, ListFloat, {})
    .ATTR(roi, ListInt, {})
    .ATTR(coordinate_transformation_mode, String, "half_pixel")
    .ATTR(cubic_coeff_a, Float, -0.75)
    .ATTR(exclude_outside, Int, 0)
    .ATTR(extrapolation_value, Float, 0.0)
    .ATTR(mode, String, "nearest")
    .ATTR(nearest_mode, String, "round_prefer_floor")
    .ATTR(data_format, String, "NCHW")
    .OP_END_FACTORY_REG(ResizeD)
```

## Brief

Calculate the resize_d function. 

## Inputs

One input, including:
x: A 4D tensor, indicating the original size. Must be one of the following types:
float16, float32. The format must be NCHW. 

## Outputs

y: A 4D tensor, indicating the target size. Must have the same type and format as x.
Shape depends on x and sizes.

## Attributes

- sizes: A required listInt.
Size of the output parameter shape in the H and W dimensions.
- scales: An optional listFloat. Scaling factor of the output data.
Defaults to none.
- roi: An optional listInt. Coordinates of the roi,
which are normalized in the coordinate system of the input image.
Defaults to none.
- coordinate_transformation_mode: An optional String.
Alignment mode in Bicubic interpolation mode.
Defaults to "half_pixel", other optional: align_corners.
- cubic_coeff_a: An optional float.
Indicates the calculation weight coefficient of the interpolation.
Defaults to -0.75.
- exclude_outside: An optional int.
Whether input parameter excludes out-of-range points during interpolation.
Defaults to 0.
- extrapolation_value: An optional float.
The fill value used when the interpolation point is out of the data range.
Defaults to 0.0.
- mode: An optional String. ResizeD interpolation mode.
Defaults to "nearest", other optional: linear or cubic.
Currently, this parameter cannot be set to nearest.
When mode is set to linear, the H axis of the operator input tensor must be 1.
- nearest_mode: An optional String. When processing non-integer coordinates,
the nearest neighbor interpolation selects the processing mode of the nearest pixel.
Defaults to "round_prefer_floor",
other optional: "round_prefer_ceil", "floor", "ceil".
- data_format: An optional String. Format of the input data converted during calculation.
Defaults to "NCHW", other optional: "HWNC".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Attention Constraints

- The operator will not be enhanced in the future.
- For Ascend 910D AI Processors, replace it with ResizeLinear and ResizeBicubicV2 operators.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
