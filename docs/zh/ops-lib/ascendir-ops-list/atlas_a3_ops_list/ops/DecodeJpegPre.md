# DecodeJpegPre

```c
REG_OP(DecodeJpegPre)
    .INPUT(contents, TensorType({DT_STRING}))
    .OUTPUT(dvpp_support, BOOL)
    .REQUIRED_ATTR(w_range, ListInt)
    .REQUIRED_ATTR(h_range, ListInt)
    .OP_END_FACTORY_REG(DecodeJpegPre)
```

## Brief

DecodeJpegPre

## Inputs

- contents: A Tensor of type string. 0-D. The JPEG-encoded image.

## Outputs

- dvpp_support: indicates if the dvpp support this jpeg image decode.

## Attributes

- w_range: An required listInt contains width [min, max].
- h_range: An required listInt contains height [min, max].

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 contents: string
- output0 dvpp_support: bool

## Attention Constraints

- Only support in dvpp


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
