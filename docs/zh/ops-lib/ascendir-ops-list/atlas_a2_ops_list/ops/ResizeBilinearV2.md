# ResizeBilinearV2

```c
REG_OP(ResizeBilinearV2)
    .INPUT(x, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32,
                          DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .INPUT(size, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_UINT8, DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(align_corners, Bool, false)
    .ATTR(half_pixel_centers, Bool, false)
    .ATTR(dtype, Type, DT_FLOAT)
    .ATTR(scales, ListFloat, {0.0f, 0.0f})
    .OP_END_FACTORY_REG(ResizeBilinearV2)
```

## Brief

Resize images to size using bilinear interpolation . 

## Inputs

Input images must be a 4-D tensor. Inputs include:
- x: 4-D tensor. Must set the format, supported format list ["NCHW, NHWC"].
- size: A 1-D int32 Tensor of 2 elements: new_height, new_width. The new
size for the images . 

## Outputs

y: 4-D tensor, format must be the same as x. support format list ["NCHW", "NHWC"].
When the dtype of y is float32, the dtype of x can be float32, float16 or bfloat16. When the dtype of y is
float16 or bfloat16, then the dtype of y must be the same as x.The N, C dimension must be the same as x.

## Attributes

- align_corners: An optional bool. If true, the centers of the 4 corner pixels of the input and
output tensors are aligned, preserving the values at the corner pixels.
Defaults to false .
- half_pixel_centers: An optional bool. If true, the center of pixels locate in [0.5, 0.5]. When "align_corners" is true, "half_pixel_centers" cannot be true.
Defaults to False .
- dtype: An optional Type attr, support type list [uint8, float32, float16, bfloat16].
The data type of output y.
Defaults to float32 .
- scales: An optional listfloat. Multiplier for spatial size. Defaults to {0.0f, 0.0f} .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 size: int32
- output0 y: float16,float32
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 size: int32
- output0 y: float32
### Dvpp
- input0 x: float32,uint8
- input1 size: int32
- output0 y: float32,uint8

## Third-party framework compatibility

Compatible with TensorFlow and PyTorch ResizeBilinearV2 operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
