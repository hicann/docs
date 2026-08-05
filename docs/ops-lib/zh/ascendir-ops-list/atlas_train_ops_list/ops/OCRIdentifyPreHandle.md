# OCRIdentifyPreHandle

```c
REG_OP(OCRIdentifyPreHandle)
    .INPUT(imgs_data, TensorType({DT_UINT8}))
    .INPUT(imgs_offset, TensorType({DT_INT32}))
    .INPUT(imgs_size, TensorType({DT_INT32}))
    .OUTPUT(resized_imgs, TensorType({DT_UINT8}))
    .REQUIRED_ATTR(size, ListInt)
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(OCRIdentifyPreHandle)
```

## Brief

ocr identify prehandle.

## Inputs

- imgs_data: A Tensor of type uint8. Multi img data value.
- imgs_offset:A Tensor of type int32. Offset of every img data in input imgs_data.
- imgs_size:A Tensor of type int32. Shape of every img data.

## Outputs

resized_imgs: A Tensor of type uint8. Multi imgs after identify pre handle.

## Attributes

- size: An optional int. Size.
- data_format: An optional string from: '"NHWC", "NCHW"'. Defaults to
"NHWC". Data format.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
