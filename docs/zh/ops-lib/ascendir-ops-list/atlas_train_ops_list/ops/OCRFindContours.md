# OCRFindContours

```c
REG_OP(OCRFindContours)
    .INPUT(img, TensorType({DT_UINT8}))
    .OUTPUT(polys_data, TensorType({DT_INT32}))
    .OUTPUT(polys_offset, TensorType({DT_INT32}))
    .OUTPUT(polys_size, TensorType({DT_INT32}))
    .ATTR(value_mode, Int, 0)
    .OP_END_FACTORY_REG(OCRFindContours)
```

## Brief

find contours acording to img.

## Inputs

- img: A Tensor of type uint8. Img data value.

## Outputs

- polys_data: A Tensor of type int32. Point data of every contours.
- polys_offset:A Tensor of type int32. Offset of every contours .
- polys_size:A Tensor of type int32. Size of every contours.

## Attributes

- value_mode: An optional int. Defaults to 0.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
