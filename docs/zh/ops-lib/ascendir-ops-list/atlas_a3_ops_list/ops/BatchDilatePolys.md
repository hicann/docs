# BatchDilatePolys

```c
REG_OP(BatchDilatePolys)
    .INPUT(polys_data, TensorType({DT_INT32}))
    .INPUT(polys_offset, TensorType({DT_INT32}))
    .INPUT(polys_size, TensorType({DT_INT32}))
    .INPUT(score, TensorType({DT_FLOAT}))
    .INPUT(min_border, TensorType({DT_INT32}))
    .INPUT(min_area_thr, TensorType({DT_INT32}))
    .INPUT(score_thr, TensorType({DT_FLOAT}))
    .INPUT(expands_cale, TensorType({DT_FLOAT}))
    .OUTPUT(dilated_polys_data, TensorType({DT_INT32}))
    .OUTPUT(dilated_polys_offset, TensorType({DT_INT32}))
    .OUTPUT(dilated_polys_size, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(BatchDilatePolys)
```

## Brief

batch dilate polygons according to expand_scale.

## Inputs

- polys_data: A Tensor of type int32. point data of every polygon.
- polys_offset:A Tensor of type int32. Offset of every polygon .
- polys_size:A Tensor of type int32. Size of every polygon.
- score:A Tensor of type float. Score of every point in image.
- min_border:A Tensor of type int32. Minimum width of each polygon.
- min_area_thr:A Tensor of type int32. Minimum area of each polygon.
- score_thr:A Tensor of type float. Minimum confidence score of each polygon.
- expands_cale:A Tensor of type float. Polygon expansion multiple.

## Outputs

- dilated_polys_data: A Tensor of type int32. Point data of every dilated polygon.
- dilated_polys_offset: A Tensor of type int32. Offset of every dilated polygon .
- dilated_polys_size: A Tensor of type int32. Size of every dilated polygon.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
