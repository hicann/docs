# ResizeLinearGrad

```c
REG_OP(ResizeLinearGrad)
    .INPUT(grads, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(original_image, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(align_corners, Bool, false)
    .ATTR(scale, Float, 0.0f)
    .OP_END_FACTORY_REG(ResizeLinearGrad)
```

## Brief

Backwards calculation of ResizeLinear.

## Inputs

- grads: A 3D tensor, represents the gradient of output of ResizeLinear. Format must be NCL.
Dtype must be float32, float16 or bfloat16.
- original_image: A 3D tensor, represents the resized image of ResizeLinear. Format and dtype must be the same as grads.
The N, C dimension must be the same as grads.

## Outputs

y: A 3D tensor, represents the gradient of original_image. Format and dtype and shape must be the same as original_image.

## Attributes

- align_corners: An optional bool. If true, the centers of the 2 corner pixels of the input and output tensors are
aligned, preserving the values at the corner pixels.If false, calculate interpolation using half pixel centers.
Defaults to false.
- scale: An optional float. The element represents the ratio of the L axis
subscripts of pixels in grades to the L axis subscripts of pixels in y, only takes effect when align_corners is
true and the value is greater than 0. Defaults to 0.0f.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: bfloat16,float16,float32
- input1 original_image: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with PyTorch upsample_linear1d_backward operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
