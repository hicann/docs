# Crop

```c
REG_OP(Crop)
      .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64}))
      .INPUT(size, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64}))
      .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64}))
      .ATTR(axis, Int, 2)
      .REQUIRED_ATTR(offsets, ListInt)
      .OP_END_FACTORY_REG(Crop)
```

## Brief

Crops the input tensor x to the shape of size. For example:
(1) x: bottom to be cropped, with shape (20, 50, 512, 512);
(2) size: reference input for cropping, with shape (20, 10, 256, 256);
(3) axis = 1;
(4) offsets = (25, 128, 128);
(5) y = x[:, 25:25 + size.shape[1], 128:128 + size.shape[2], 128:128 +
size.shape[3]] .

## Inputs

Inputs include:
- x: A required Tensor. Must be one of the following types: float16,
float32, int8, uint8, int16, uint16, int32, uint32,int64, uint64.
The format support ND, NCHW, NHWC and NC1HWC0. Shape support 1D ~ 8D.
- size: A required Tensor. Must be one of the following types: float16,
float32, int8, uint8, int16, uint16, int32, uint32, int64, uint64.
The format support ND, NCHW, NHWC and NC1HWC0. Shape support 1D ~ 8D.
The format and type are same as "x".
Each dimension of "size" cannot exceed the corresponding dimension of "x". 

## Outputs

y: A required Tensor. The format support ND, NCHW, NHWC and NC1HWC0.
Shape support 1D ~ 8D. Must be one of the following types: float16,
float32, int8, uint8, int16, uint16, int32, uint32, int64, uint64.
Has the same type, format and shape as "size" . 

## Attributes

- axis: A required int, specifying the first dimension to crop. Defaults
to "2". When ori_format of x is equal to "NCHW", the ori_shape of x is
equal to 4 and the axis is greater than or equal to 2.
The Op Crop can support HC1HWC0 and ND.
- offsets: A required array,
specifying the shift for all/each dimension to align the cropped bottom with
the reference bottom. No default value.
Must be one of the following types: float16, float32, int8, uint8, int16,
uint16, int32, uint32, int64, uint64. 

## Attention Constraints

- "y" must have the same type and shape as "size". "x" must have the same
type as "size".
- "axis" must be less than the rank of "x".
- The "offsets" for each dimension must not exceed the maximum value of
the corresponding dimension of "x".
- The array length of "offsets" plus the value of "axis" equals to the
rank of "y".
- When ori_format of x is equal to "NCHW", the ori_shape of x is
equal to 4 and the axis is greater than or equal to 2.
The Op Crop can support HC1HWC0 and ND.

## Third-party framework compatibility

Compatible with the Caffe operator Crop.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
