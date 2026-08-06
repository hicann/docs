# OCRDetectionPostHandle

```c
REG_OP(OCRDetectionPostHandle)
    .INPUT(img, TensorType({DT_UINT8}))
    .INPUT(polys_data, TensorType({DT_INT32}))
    .INPUT(polys_offset, TensorType({DT_INT32}))
    .INPUT(polys_size, TensorType({DT_INT32}))
    .OUTPUT(imgs_data, TensorType({DT_UINT8}))
    .OUTPUT(imgs_offset, TensorType({DT_INT32}))
    .OUTPUT(imgs_size, TensorType({DT_INT32}))
    .OUTPUT(rect_points, TensorType({DT_INT32}))
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(OCRDetectionPostHandle)
```

## Brief

ocr detection post handle.

## Inputs

- img: A Tensor of type uint8. original image data.
- polys_data: A Tensor of type int32. point data of every poly.
- polys_offset:A Tensor of type int32. Offset of every poly.
- polys_size:A Tensor of type int32. Size of every poly.

## Outputs

- imgs_data: A Tensor of type uint8. imgs_data of original image.
- imgs_offset: A Tensor of type int32. Offset of every imgs data.
- imgs_size: A Tensor of type int32. Shape of every imgs data.
- rect_points: A Tensor of type int32. Rect points of every imgs.

## Attributes

- data_format: An optional string from: '"NHWC", "NCHW"'. Defaults to
"NHWC". Data format.


---

[Back to Operator Specifications (Ascend950)](../README.md)
