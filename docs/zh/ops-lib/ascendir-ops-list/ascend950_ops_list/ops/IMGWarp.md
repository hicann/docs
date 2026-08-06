# IMGWarp

```c
REG_OP(IMGWarp)
    .INPUT(img, TensorType({DT_UINT8, DT_FLOAT16, DT_FLOAT32}))
    .INPUT(warp_offset, TensorType({DT_FLOAT32}))
    .OUTPUT(warp_img, TensorType({DT_UINT8, DT_FLOAT16, DT_FLOAT32}))
    .OP_END_FACTORY_REG(IMGWarp)
```

## Brief

Resizes "images" with "offset" using bilinear interpolation. 

## Inputs

- img: input image, A 4-D tensor of shape `[n, h, w, c]`.
Must be one of the following types: uint8, float16, float. The format support ND.
- warp_offset: the resize offset A 4-D float tensor of shape `[n, h, w, 2]`, 2 means (x, y) for offset point.
The data type is float. The format support ND.

## Outputs

warp_img: A Tensor after resize. The shape is 4D of `[n, h, w, 2]`.
Must be one of the following types: uint8, float16, float. The format support ND.
Has the same data type as input "img". 


---

[Back to Operator Specifications (Ascend950)](../README.md)
