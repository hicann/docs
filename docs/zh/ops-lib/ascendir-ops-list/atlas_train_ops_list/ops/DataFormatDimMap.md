# DataFormatDimMap

```c
REG_OP(DataFormatDimMap)
    .INPUT(x, TensorType::IndexNumberType())
    .ATTR(src_format, String, "NHWC")
    .ATTR(dst_format, String, "NCHW")
    .OUTPUT(y, TensorType::IndexNumberType())
    .OP_END_FACTORY_REG(DataFormatDimMap)
```

## Brief

Returns the dimension index in the destination data format given the one in
the source data format.

## Inputs

x: An ND or 5HD tensor. Support 1D~8D. Must be one of the following types:int32, int64.
    A Tensor with each element as a dimension index in source data format.
    Must be in the range [-4, 4).

## Outputs

y: A tensor. Has the same type as "x". Must be in the range [0, 4).

## Attributes

- src_format: An optional string. Supports NHWC and NCHW, Defaults to NHWC.
    source data format. Must of length 4.
- dst_format: An optional string. Supports NHWC and NCHW, Defaults to NCHW.
    destination data format. Must of length 4.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: int32
- output0 y: int32
### AI CPU
- input0 x: int32,int64
- output0 y: int32,int64

## Third-party framework compatibility

Compatible with the TensorFlow operator DataFormatDimMap.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
