# ResizeAndClipPolys

```c
REG_OP(ResizeAndClipPolys)
    .INPUT(polys_data, TensorType({DT_INT32}))
    .INPUT(polys_offset, TensorType({DT_INT32}))
    .INPUT(polys_size, TensorType({DT_INT32}))
    .INPUT(h_scale, TensorType({DT_FLOAT}))
    .INPUT(w_scale, TensorType({DT_FLOAT}))
    .INPUT(img_h, TensorType({DT_INT32}))
    .INPUT(img_w, TensorType({DT_INT32}))
    .OUTPUT(clipped_polys_data, TensorType({DT_INT32}))
    .OUTPUT(clipped_polys_offset, TensorType({DT_INT32}))
    .OUTPUT(clipped_polys_size, TensorType({DT_INT32}))
    .OUTPUT(clipped_polys_num, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(ResizeAndClipPolys)
```

## Brief

resize and clip polys.

## Inputs

- polys_data: A Tensor of type int32. point data of every poly.
- polys_offset:A Tensor of type int32. Offset of every poly .
- polys_size:A Tensor of type int32. Size of every poly.
- h_scale:A Tensor of type float. Expand scale of height.
- w_scale:A Tensor of type float. Expand scale of width.
- img_h:A Tensor of type int32. Height of original image.
- img_w:A Tensor of type int32. Width of original image.

## Outputs

- clipped_polys_data: A Tensor of type int32. point data of every clipped poly.
- clipped_polys_offset: A Tensor of type int32. Offset of every clipped poly .
- clipped_polys_size: A Tensor of type int32. Size of every clipped poly.
- clipped_polys_num: A Tensor of type int32. Number of clipped polys.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
