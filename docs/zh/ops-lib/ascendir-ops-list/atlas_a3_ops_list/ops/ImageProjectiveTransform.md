# ImageProjectiveTransform

```c
REG_OP(ImageProjectiveTransform)
    .INPUT(images, TensorType({DT_UINT8, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(transforms, TensorType({DT_FLOAT}))
    .INPUT(output_shape, TensorType({DT_INT32}))
    .REQUIRED_ATTR(interpolation, String)
    .ATTR(fill_mode, String, "CONSTANT")
    .OUTPUT(transformed_images, TensorType({DT_UINT8, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(ImageProjectiveTransform)
```

## Brief

Applies the given transform to each of the images.

## Inputs

- images: 4-D tensor with shape of [batch, height, width, channels].
Must be one of the following types: uint8, int32, int64, float16, float32, double
- transforms: 2-D tensor with shape of [batch, 8] or [1, 8].
Must be one of the following types: float32.
- output_shape: 1-D tensor [new_height, new_width].
Must be one of the following types: int32.

## Outputs

transformed_images: Has the same type as images,
4-D tensor with shape[batch, new_height, new_width, channels]. 

## Attributes

- interpolation: A required string. Interpolation method, "NEAREST" or "BILINEAR".
- fill_mode: An optional string.
Defaults to "CONSTANT". Fill mode, "REFLECT", "WRAP", or "CONSTANT".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 images: float16,float32,int32,uint8
- input1 transforms: float32
- input2 output_shape: int32
- output0 transformed_images: float16,float32,int32,uint8
### AI CPU
- input0 images: double,float16,float32,int32,int64,uint8
- input1 transforms: float32
- input2 output_shape: int32
- output0 transformed_images: double,float16,float32,int32,int64,uint8

## Third-party framework compatibility.

Compatible with tensorflow ImageProjectiveTransform operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
