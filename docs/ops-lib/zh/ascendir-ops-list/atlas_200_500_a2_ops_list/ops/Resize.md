# Resize

```c
REG_OP(Resize)
    .INPUT(x, TensorType({DT_INT8,DT_UINT8,DT_INT16,DT_UINT16,DT_INT32,
                          DT_INT64,DT_FLOAT16,DT_FLOAT,DT_DOUBLE}))
    .OPTIONAL_INPUT(roi, TensorType({DT_FLOAT16,DT_FLOAT,DT_DOUBLE}))
    .OPTIONAL_INPUT(scales, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(sizes, TensorType({DT_INT64,DT_INT32}))
    .OUTPUT(y, TensorType({DT_INT8,DT_UINT8,DT_INT16,DT_UINT16,DT_INT32,
                           DT_INT64,DT_FLOAT16,DT_FLOAT,DT_DOUBLE}))
    .ATTR(coordinate_transformation_mode, String, "half_pixel")
    .ATTR(cubic_coeff_a, Float, -0.75)
    .ATTR(exclude_outside, Int, 0)
    .ATTR(extrapolation_value, Float, 0.0)
    .ATTR(mode, String, "nearest")
    .ATTR(nearest_mode, String, "round_prefer_floor")
    .OP_END_FACTORY_REG(Resize)
```

## Brief

Resize the input tensor. 
currently, only support resize image tensor using nearest neighbor and linear interpolation.

## Inputs

Input x must be a 4-D tensor. Inputs include: 
- x: A Tensor. Must be one of the following types: uint8, int8, int16,
int32, int64, float16, float, double. 4-D with shape [batch, height, width, channels] 
or shape [batch, channels, height, width].
- roi: A 1-D float Tensor. Only takes effect when attr coordinate_transformation_mode
is "tf_crop_and_resize". Must be one of the following types: float16, float, double.
- scales: A 1-D float Tensor, the scale array along each dimension, Only one of
'scales' and 'sizes' can be specified. Must be float type.
- sizes: A 1-D int64 Tensor, The size of the output tensor. Only one of
'scales' and 'sizes' can be specified.  If 'size' is specified, then set scales 
to empty data (zero shape) in this operator's input list. Must be one of 
the following types: int32, int64.

## Outputs

y: A Tensor. Has the same type as x.

## Attributes

- coordinate_transformation_mode: An optional String. how to transform
the coordinate in the resized tensor to the coordinate in the original tensor. 
options: pytorch_half_pixel, align_corners, asymmetric, 
tf_crop_and_resize.
- cubic_coeff_a: An optional Float. Defaults to -0.75, only used in cubic interpolation.
other optional: -0.5
- exclude_outside: An optional Int. Defaults to 0, If set to 1, the weight of sampling
locations outside the tensor will be set to 0 and the weight will be renormalized 
so that their sum is 1.0.
- extrapolation_value: An optional Float. Defaults to 0.0f. When coordinate_transformation_mode
is "tf_crop_and_resize" and x_original is outside the range [0, length_original - 1], 
this value is used as the corresponding output value.
- mode: An optional String. Defaults to nearest. Three interpolation modes: nearest (default),
linear and cubic.
- nearest_mode: An optional String. Defaults to round_prefer_floor. Four modes: round_prefer_floor,
round_prefer_ceil, floor, ceil. Only used by nearest interpolation.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 roi: double,float16,float32
- input2 scales: float32
- input3 sizes: int32,int64
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Third-party framework compatibility

Compatible with tensorflow ResizeNearestNeighborV2 operator.

## Attention Constraints: 

Input x must be a 4-D tensor.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
