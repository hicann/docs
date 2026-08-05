# ResizeGrad

```c
REG_OP(ResizeGrad)
    .INPUT(grads, TensorType({OrdinaryType, DT_STRING}))
    .OPTIONAL_INPUT(roi, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OPTIONAL_INPUT(scales, TensorType({DT_FLOAT}))
    .INPUT(original_size, TensorType({DT_INT64, DT_INT32}))
    .OUTPUT(y, TensorType({OrdinaryType, DT_STRING}))
    .ATTR(coordinate_transformation_mode, String, "half_pixel")
    .ATTR(cubic_coeff_a, Float, -0.75)
    .ATTR(exclude_outside, Int, 0)
    .ATTR(extrapolation_value, Float, 0.0)
    .ATTR(mode, String, "nearest")
    .ATTR(nearest_mode, String, "round_prefer_floor")
    .OP_END_FACTORY_REG(ResizeGrad)
```

## Brief

Calculate the resize_grad function.
support resize_grad image tensor using nearest(1d) and linear(1d) and bicubic(2d) interpolation. 

## Inputs

Input grads must be a 4-D tensor. Inputs include:
- grads: A Tensor. Must be one of the following types: uint8, uint16, uint32, uint64, int16,
int32, int64, float16, float, double. 4-D with shape [batch, height, width, channels]
or shape [batch, channels, height, width]. The format support ND.
- roi: A 1-D Tensor. Must be one of the following types: float16, float, double.
Only takes effect when attr coordinate_transformation_modeis "tf_crop_and_resize". The format support ND.
- scales: A 1-D float Tensor, the scale array along each dimension. The format support ND.
- original_size: A 1-D int64 or int32 Tensor, The size of the output tensor. The format support ND.

## Outputs

- y: A Tensor with the same type of grads's, shape depends on grads and sizes.
The format support ND. Must be one of the following types: uint8, uint16, uint32, uint64,
int16, int32, int64, float16, float, double. 

## Attributes

- coordinate_transformation_mode: String. Defaults to half_pixel. how to transform
the coordinate in the resized tensor to the coordinate in the original tensor.
other optional: pytorch_half_pixel, align_corners, asymmetric, tf_half_pixel_for_nn,
tf_crop_and_resize.
- cubic_coeff_a: Float. Defaults to -0.75, only used in cubic interpolation.
other optional: -0.5
- exclude_outside: Int. Defaults to 0, If set to 1, the weight of sampling
locations outside the tensor will be set to 0 and the weight will be renormalized
so that their sum is 1.0.
- extrapolation_value: Float. Defaults to 0.0f. When coordinate_transformation_mode
is "tf_crop_and_resize" and x_original is outside the range [0, length_original - 1],
this value is used as the corresponding output value.
- mode: String. Defaults to nearest. Three interpolation modes: nearest (default),
linear and cubic.
- nearest_mode: String. Defaults to round_prefer_floor. Four modes: round_prefer_floor,
round_prefer_ceil, floor, ceil. Only used by nearest interpolation. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 grads: double,float16,float32,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 roi: double,float16,float32
- input2 scales: float32
- input3 original_size: int32,int64
- output0 y: double,float16,float32,int16,int32,int64,uint8,uint16,uint32,uint64


---

[Back to Operator Specifications (Ascend950)](../README.md)
