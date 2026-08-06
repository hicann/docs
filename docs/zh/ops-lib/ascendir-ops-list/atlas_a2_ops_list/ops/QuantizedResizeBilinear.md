# QuantizedResizeBilinear

```c
REG_OP(QuantizedResizeBilinear)
    .INPUT(images, TensorType({DT_QUINT8,DT_QINT32,DT_FLOAT}))
    .INPUT(size, TensorType({ DT_INT32 }))
    .INPUT(min, TensorType({ DT_FLOAT }))
    .INPUT(max, TensorType({ DT_FLOAT }))
    .OUTPUT(resized_images, TensorType({DT_QUINT8,DT_QINT32,DT_FLOAT }))
    .OUTPUT(y_min, TensorType({ DT_FLOAT }))
    .OUTPUT(y_max, TensorType({ DT_FLOAT }))
    .ATTR(align_corners, Bool, false)
    .ATTR(half_pixel_centers, Bool, false)
    .OP_END_FACTORY_REG(QuantizedResizeBilinear)
```

## Brief

Resize quantized images to size using quantized bilinear interpolation . 

## Inputs

Input images must be a 4-D tensor. Inputs include:
- images: 4-D with shape [batch, height, width, channels]. The format must
be NHWC, Must be one of the following types: quint8, qint32, float.
- size: A 1-D int32 Tensor of 2 elements: new_height, new_width. The new
size for the images, tensor of type int32.
- min: A Tensor of type float.
- max: A Tensor of type float .

## Outputs

- resized_images: 4-D with shape [batch, new_height, new_width, channels], Must be one of the following types:
quint8, qint32, float, The format must be NHWC.
- y_min: A Tensor of type float.
- y_max: A Tensor of type float .

## Attributes

- align_corners: An optional bool. Defaults to False. If true, the centers
of the 4 corner pixels of the input and output tensors are aligned, preserving
the values at the corner pixels. Defaults to false.
- half_pixel_centers: An optional bool. Defaults to False. indicates if the offset coordinates are normalized .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 images: float32,qint32,quint8
- input1 size: int32
- input2 min: float32
- input3 max: float32
- output0 resized_images: float32,qint32,quint8
- output1 y_min: float32
- output2 y_max: float32

## Attention Constraints

Input images and output images must be quantized types . 

## Third-party framework compatibility

Compatible with tensorflow QuantizedResizeBilinear operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
