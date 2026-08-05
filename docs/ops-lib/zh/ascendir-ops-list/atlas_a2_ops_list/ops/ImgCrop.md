# ImgCrop

```c
REG_OP(ImgCrop)
    .INPUT(x, TensorType({DT_FLOAT, DT_UINT8}))
    .INPUT(boxes, TensorType({DT_UINT32, DT_INT32}))
    .INPUT(box_index, TensorType({DT_UINT32, DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_UINT8}))
    .ATTR(data_format, String, "CHW")
    .OP_END_FACTORY_REG(ImgCrop)
```

## Brief

Applies crop to image. 

## Inputs

- x: An tensor of at least 3 dimensions, type must be float32 or uint8.
- boxes: A Tensor of type uint32 or int32. A 2-D tensor of shape
[num_boxes, 4], 4 numbers represent [left, top, left+width, top+height].
- box_index: A Tensor of type uint32 or int32. A 1-D tensor of shape
[num_boxes] with int32 values in [0, batch).

## Outputs

y: output tensor, NHWC or NCHW, type must be float32 or uint8. 

## Attributes

- data_format: An optional string. Could be "HWC" or "CHW". Defaults to
"CHW". Value used for inferring real format of images.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### Dvpp
- input0 x: float32,uint8
- input1 boxes: int32,uint32
- input2 box_index: int32,uint32
- output0 y: float32,uint8

## Attention Constraints

This operator will be deprecated in the future.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
