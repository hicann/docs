# ImageProjectiveTransformV2

```c
REG_OP(ImageProjectiveTransformV2)
    .INPUT(images, TensorType({DT_UINT8, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(transforms, TensorType({DT_FLOAT}))
    .INPUT(output_shape, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(fill_value, TensorType({DT_UINT8, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .REQUIRED_ATTR(interpolation, String)
    .ATTR(fill_mode, String, "CONSTANT")
    .OUTPUT(transformed_images, TensorType({DT_UINT8, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(ImageProjectiveTransformV2)
```

## Brief

image to transforms. 

## Inputs

- images: [batch, height, width, channels], 4-D tensor,
type support uint8, int32, int64, float32, double.
- transforms: [batch, 8] or [1, 8] matrix, 2-D tensor, type support float32.
- outout_shape: [new_height, new_width], 1-D tensor, type support int32.
- fill_value: [scalar], 1-D tensor, type support uint8, int32, int64, float32,
double, this argus is optional.

## Outputs

transformed_images: 4-D tensor with shape[batch, new_height, new_width,
channels], as images,support uint8, int32, int64, float32, double

## Attributes

- interpolation: Interpolation method, type is string,
support "NEAREST" or "BILINEAR".
- fill_mode: Fill mode, defaults is "CONSTANT" also support
"REFLECT", "WRAP", or "CONSTANT".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 images: float16,float32,int32,uint8
- input1 transforms: float32
- input2 output_shape: int32
- input3 fill_value: float16,float32,int32,uint8
- output0 transformed_images: float16,float32,int32,uint8

## Third-party framework compatibility.

Compatible with tensorflow ImageProjectiveTransformv2 operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
