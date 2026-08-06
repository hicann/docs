# WarpPerspective

```c
REG_OP(WarpPerspective)
    .INPUT(x, TensorType({DT_FLOAT, DT_UINT8}))
    .INPUT(matrix, TensorType({DT_DOUBLE, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_UINT8}))
    .REQUIRED_ATTR(out_height, Int)
    .REQUIRED_ATTR(out_width, Int)
    .ATTR(interpolation_mode, String, "bilinear")
    .ATTR(border_type, String, "BORDER_CONSTANT")
    .ATTR(constant, Float, 0)
    .ATTR(data_format, String, "CHW")
    .OP_END_FACTORY_REG(WarpPerspective)
```

## Brief

Applies a perspective transformation to an image . 

## Inputs

- x: input tensor, format could be NHWC or NCHW, type could be float or uint8.
- matrix: transformation matrix, format ND , shape must be (N, 9),
type could be float or double. 

## Outputs

- y: output tensor, format could be NHWC or NCHW, type could be float or uint8.

## Attributes

- out_height: output height, required.
- out_width: output width, required.
- interpolation_mode: interpolation method, support "bilinear" and "nearest",
defaults to "bilinear"
- border_type: border processing method, support "BORDER_CONSTANT" and "BORDER_REPLICATE",
default BORDER_CONSTANT.
- constant: border processed value, used when border_type is BORDER_CONSTANT.
- data_format: the data format of input tensor and output tensor, support "CHW" and "HWC",
defaults to "CHW" 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: float32
- input1 matrix: float32
- output0 y: float32


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
