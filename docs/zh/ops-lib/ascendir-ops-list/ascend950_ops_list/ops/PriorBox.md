# PriorBox

```c
REG_OP(PriorBox)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(img, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(min_size, ListFloat)
    .REQUIRED_ATTR(max_size, ListFloat)
    .REQUIRED_ATTR(aspect_ratio, ListFloat)
    .ATTR(img_h, Int, 0)
    .ATTR(img_w, Int, 0)
    .ATTR(step_h, Float, 0.0)
    .ATTR(step_w, Float, 0.0)
    .ATTR(flip, Bool, true)
    .ATTR(clip, Bool, false)
    .ATTR(offset, Float, 0.5)
    .ATTR(variance, ListFloat, {0.1})
    .OP_END_FACTORY_REG(PriorBox)
```

## Brief

Performs SSD prior box detection . 

## Inputs

Two inputs, including:
- x: An NCHW feature map of type is float32 or float16.
- img: source image. Has the same type and format as "x" .

## Outputs

y: An ND tensor of type float32 or float16, specifying the prior box information, including its coordinates and variance . 

## Attributes

- min_size: A required float32, specifying the minimum edge length of a square prior box.
- max_size: A required float32, specifying the maximum edge length of a square prior box: sqrt(min_size * max_size)
- aspect_ratio: An required float32, specifying the aspect ratio for generated rectangle boxes. The height
is min_size/sqrt(aspect_ratio), the width is min_size*sqrt(aspect_ratio). Defaults to "1.0".
- img_h: An optional int32, specifying the source image height. Defaults to "0".
- img_w: An optional int32, specifying the source image width. Defaults to "0".
- step_h: An optional float32, specifying the height step for mapping the center point from the feature map to the source image. Defaults to "0.0".
- step_w: An optional float32, specifying the width step for mapping the center point from the feature map to the source image. Defaults to "0.0".
- flip: An optional bool. If "True", "aspect_ratio" will be flipped. Defaults to "True".
- clip: An optional bool. If "True", a prior box is clipped to within [0, 1]. Defaults to "False".
- offset: An optional float32, specifying the offset. Defaults to "0.5".
- variance: An optional float32, specifying the variance of a prior box, either one or four variances. Defaults to "0.1" (one value) .

## Attention Constraints

This operator applies only to SSD networks.
@see SSDDetectionOutput()

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe.


---

[Back to Operator Specifications (Ascend950)](../README.md)
