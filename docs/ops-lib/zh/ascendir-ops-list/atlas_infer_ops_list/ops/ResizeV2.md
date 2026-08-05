# ResizeV2

```c
REG_OP(ResizeV2)
    .INPUT(x, TensorType({DT_FLOAT, DT_UINT8}))
    .INPUT(dst_size, TensorType({DT_INT32,DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_UINT8}))
    .ATTR(interpolation, String, "nearest")
    .ATTR(data_format, String, "HWC")
    .OP_END_FACTORY_REG(ResizeV2)
```

## Brief

change an image size. 

## Inputs

- x: An tensor of at least 3 dimensions, type must be float32 or uint8.
- dst_size: Required int32 and int64, shape must be (1, 2), specifying the size of the output image.

## Outputs

y: output tensor of at least 3 dimensions, type must be float32 or uint8.

## Attributes

- interpolation: An optional string. Interpolation type, only support "bilinear"/"nearest"/"cubic"/"area",
default "nearest".
- data_format: An optional string. Could be "HWC" or "CHW". Defaults to "HWC".
Value used for inferring real format of images. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: float32,uint8
- input1 dst_size: int32,int64
- output0 y: float32,uint8


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
