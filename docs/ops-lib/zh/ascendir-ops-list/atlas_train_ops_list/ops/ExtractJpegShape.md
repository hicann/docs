# ExtractJpegShape

```c
REG_OP(ExtractJpegShape)
    .INPUT(contents, TensorType({DT_STRING}))
    .OUTPUT(image_shape, TensorType({DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(output_type, Type)
    .OP_END_FACTORY_REG(ExtractJpegShape)
```

## Brief

Extract the shape information of a JPEG-encoded image . 

## Inputs

Input contents must be 0-D. Inputs include:
contents: 0-D. The JPEG-encoded image . 

## Outputs

image_shape: 1-D. The image shape with format [height, width, channels] . 

## Attributes

output_type: The output type of the operation (int32 or int64). Defaults
to int32 . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 contents: string
- output0 image_shape: int32,int64

## Third-party framework compatibility

Compatible with tensorflow ExtractJpegShape operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
