# ResizeBilinearV2Grad

```c
REG_OP(ResizeBilinearV2Grad)
    .INPUT(grads, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(original_image, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(align_corners, Bool, false)
    .ATTR(half_pixel_centers, Bool, false)
    .ATTR(scales, ListFloat, {0.0f, 0.0f})
    .OP_END_FACTORY_REG(ResizeBilinearV2Grad)
```

## Brief

Backwards calculation of ResizeBilinearV2.

## Inputs

- grads: A 4D Tensor, represents the gradient of output of ResizeBilinearV2. Format must be NCHW or NHWC.
Dtype must be float32, float16 or bfloat16.
- original_image: A 4D Tensor, represents the resized image of ResizeBilinearV2. Format must be the same as grads.
When the dtype of grads is float16 or bfloat16, the dtype of original_image must be the same as grads, when the
dtype of grads is float32, the dtype of original_image can be float32, float16 or bfloat16.The N, C dimension
must be the same as grads.

## Outputs

y: A 4D Tensor, represents the gradient of original_image. Format and dtype and shape must be the same as original_image.

## Attributes

- align_corners: An optional bool. If true, the centers of the 4 corner pixels of the input and output tensors are
aligned, preserving the values at the corner pixels. Defaults to false.
- half_pixel_centers: An optional bool. If true, the center of pixels locate in [0.5, 0.5]. Defaults to False.
- scales: An optional listfloat which has two elements. The first element represents the ratio of the H axis
subscripts of pixels in grades to the H axis subscripts of pixels in y, only takes effect when align_corners is
true and the value is greater than 0. The second element represents the ratio of the W axis subscripts of pixels in
grades to the W axis subscripts of pixels in y, only takes effect when align_corners is true and the value is
greater than 0.0f. Defaults to {0.0f, 0.0f}.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: float32
- input1 original_image: float32
- output0 y: float32
### AI CPU
- input0 grads: float32
- input1 original_image: int32
- output0 y: float32

## Third-party framework compatibility

Compatible with tensorflow and pytorch ResizeBilinearV2Grad operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
