# IMGWarpResize

```c
REG_OP(IMGWarpResize)
    .INPUT(img, TensorType({DT_FLOAT16, DT_FLOAT32}))
    .INPUT(warp_index, TensorType({DT_FLOAT32}))
    .OUTPUT(warp_img, TensorType({DT_FLOAT16, DT_FLOAT32}))
    .OP_END_FACTORY_REG(IMGWarpResize)
```

## Brief

Resizes "images" with "offset" using bilinear interpolation. 

## Inputs

- img: input image, A 5-D tensor of shape `[n, 4, c, h, w]`,
and 4 mean input[(h_top, w_left), (h_top, w_right), (h_bottom, w_left),
(h_bottom, w_right)]. Must be one of the following types: float16, float32.
The format support ND.
- warp_index: the resize offset A 4-D float tensor of shape `[n, 2, h, w]`,
2 means (x, y) for resize point. The format support ND. Must be the type float32.

## Outputs

warp_img: A Tensor after ResizeBilinear, A 4-D tensor of shape `[n, c, h, w]`.
The format support ND. Must be one of the following types: float16, float32.
Must has the same type as "img". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 img: float16,float32
- input1 warp_index: float32
- output0 warp_img: float16,float32


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
