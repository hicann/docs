# CropAndResize

```c
REG_OP(CropAndResize)
    .INPUT(x, TensorType({DT_UINT8, DT_UINT16, DT_INT8, \
        DT_INT16, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(boxes, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(box_index, TensorType({DT_INT32}))
    .INPUT(crop_size, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(extrapolation_value, Float, 0)
    .ATTR(method, String, "bilinear")
    .OP_END_FACTORY_REG(CropAndResize)
```

## Brief

Extracts crops from the input image tensor and resizes them. Extracts
crops from the input image tensor and resizes them using bilinear sampling or
nearest neighbor sampling to a common output size specified by crop_size . 

## Inputs

Input x must be a 4-D tensor. Inputs include:
- x: A Tensor. Must be one of the following types:uint8, uint16, int8,
int16, int32, int64, float16, float, double. A 4-D tensor of shape
[batch, image_height, image_width, depth]. The format must be NHWC.
- boxes: A Tensor. Must be one of the following types: float16, float. A 2-D tensor of shape [num_boxes, 4].
- box_index: A Tensor of type int32. A 1-D tensor of shape [num_boxes] with
int32 values in [0, batch).
- crop_size: A Tensor of type int32. A 1-D tensor of 2 elements, crop_size
= [crop_height, crop_width]. All cropped image patches are resized to this size . 

## Outputs

y: A Tensor. Must be one of the following types: float16, float. The format must be NHWC. 

## Attributes

- extrapolation_value: An optional float. Defaults to 0. Value used for
extrapolation, when applicable.
- method: An optional string from: '"bilinear", "nearest"'. Defaults to
"bilinear". Currently two sampling methods are supported: Bilinear and
NearestNeighbor . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 boxes: float32
- input2 box_index: int32
- input3 crop_size: int32
- output0 y: float32

## Attention Constraints

Input images must be a 4-D tensor . 

## Third-party framework compatibility

Compatible with tensorflow CropAndResize operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
