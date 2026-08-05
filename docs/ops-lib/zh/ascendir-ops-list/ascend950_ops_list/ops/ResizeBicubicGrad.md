# ResizeBicubicGrad

```c
REG_OP(ResizeBicubicGrad)
    .INPUT(grads, TensorType({DT_FLOAT}))
    .INPUT(original_image, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE}))
    .ATTR(align_corners, Bool, false)
    .ATTR(half_pixel_centers, Bool, false)
    .OP_END_FACTORY_REG(ResizeBicubicGrad)
```

## Brief

Computes the gradient of bicubic interpolation . 

## Inputs

Input grads must be a 4-D tensor. Inputs include:
- grads: A Tensor of type float. 4-D with shape [batch, height, width,
channels]. The format must be NHWC.
- original_image: A Tensor. Must be one of the following types: float,
double. 4-D with shape [batch, orig_height, orig_width, channels], The image
tensor that was resized. The format must be NHWC. 

## Outputs

y: A Tensor. Has the same type as original_image. The format must be NHWC. 

## Attributes

- align_corners: An optional bool. Defaults to False. If true, the centers
of the 4 corner pixels of the input and grad tensors are aligned. Defaults to
false.
- half_pixel_centers: An optional bool. Defaults to False .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 grads: float32
- input1 original_image: double,float32
- output0 y: double,float32

## Attention Constraints

Input images can be of different types but output images are always float .

## Third-party framework compatibility

Compatible with tensorflow ResizeBicubicGrad operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
