# WarpAffine

```c
REG_OP(WarpAffine)
    .INPUT(x, TensorType({DT_FLOAT}))
    .INPUT(matrix, TensorType({ DT_FLOAT }))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(out_height, Int)
    .REQUIRED_ATTR(out_width, Int)
    .ATTR(interpolation_mode, String, "bilinear")
    .ATTR(padding_mode, String, "const")
    .ATTR(padding_value, Int, 0)
    .OP_END_FACTORY_REG(WarpAffine)
```

## Brief

Applies a affine transformation to an image. 

## Inputs

- x: An NCHW tensor of type float32 or float32.
- matrix: transformation matrix, format ND , shape must be (2, 3), type must be float32.

## Outputs

y: output tensor, format NCHW, type must be float32.

## Attributes

- out_height: A required int32, specifying the height of the output image.
Must be greater than "0".
- out_width: A required int32, specifying the width of the output image.
Must be greater than "0".
- interpolation_mode: Interpolation mode, only support "bilinear" and "nearest", default "bilinear".
- padding_mode: padding mode, only support "zeros", "border" and "reflection", default "zeros".


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
