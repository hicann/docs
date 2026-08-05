# ResizeBicubicV2Grad

```c
REG_OP(ResizeBicubicV2Grad)
    .INPUT(grads, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(original_image, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(align_corners, Bool, false)
    .ATTR(scales, ListFloat, {0.0f, 0.0f})
    .OP_END_FACTORY_REG(ResizeBicubicV2Grad)
```

## Brief

Backwards calculation of ResizeBicubicV2.

## Inputs

- grads: A 4D tensor, represents the gradient of output of ResizeBicubicV2. Format must be NCHW or NHWC. Data dtype
must be float32, float16 or bfloat16.
- original_image: A 4D tensor, represents the resized image of ResizeBicubicV2. Format and data dtype must be the
same as grads.The N, C dimension must be the same as grads.

## Outputs

y: A 4D tensor, represents the gradient of original_image. Format and data dtype and shape must be the same as original_image.

## Attributes

- align_corners: An optional bool. If true, the centers of the 4 corner pixels of the input and output tensors are
aligned, preserving the values at the corner pixels. If false, calculate interpolation using half pixel centers.
Defaults to false.
- scales: An optional listfloat which has two elements. The first element represents the ratio of the H axis
subscripts of pixels in grads to the H axis subscripts of pixels in y, only takes effect when align_corners is
true and the value is greater than 0. The second element represents the ratio of the W axis subscripts of pixels in
grads to the W axis subscripts of pixels in y, only takes effect when align_corners is true and the value is
greater than 0.0f. Defaults to {0.0f, 0.0f}.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: bfloat16,float16,float32
- input1 original_image: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with PyTorch upsample_bicubic2d_backward operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
