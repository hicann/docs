# OCRDetectionPreHandle

```c
REG_OP(OCRDetectionPreHandle)
    .INPUT(img, TensorType({DT_UINT8}))
    .OUTPUT(resized_img, TensorType({DT_UINT8}))
    .OUTPUT(h_scale, TensorType({DT_FLOAT}))
    .OUTPUT(w_scale, TensorType({DT_FLOAT}))
    .ATTR(data_format, String, "NHWC")
    .OP_END_FACTORY_REG(OCRDetectionPreHandle)
```

## Brief

ocr detection pre handle.

## Inputs

img: A Tensor of type uint8. img data value. 

## Outputs

- resized_img: A Tensor of type uint8. Img after detection pre handle.
- h_scale: A Tensor of type float. H scale.
- w_scale: A Tensor of type float. W scale.

## Attributes

data_format: An optional string from: '"NHWC", "NCHW"'. Defaults to
"NHWC". Data format.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
