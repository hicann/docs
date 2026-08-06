# EncodeJpeg

```c
REG_OP(EncodeJpeg)
    .INPUT(image, TensorType({DT_UINT8}))
    .OUTPUT(contents, TensorType({DT_STRING}))
    .ATTR(format, String, "")
    .ATTR(quality, Int, 95)
    .ATTR(progressive, Bool, false)
    .ATTR(optimize_size, Bool, false)
    .ATTR(chroma_downsampling, Bool, true)
    .ATTR(density_unit, String, "in")
    .ATTR(x_density, Int, 300)
    .ATTR(y_density, Int, 300)
    .ATTR(xmp_metadata, String, "")
    .OP_END_FACTORY_REG(EncodeJpeg)
```

## Brief

JPEG-encode an image. 

## Inputs

Input image must be unit8 type. Inputs include:
image: A 3-D uint8 Tensor of shape [height, width, channels] . 

## Outputs

contents: 0-D. JPEG-encoded image. 

## Attributes

- format: An optional string, default is "". Per pixel image format.
- quality: An optional int, default is 95. Quality of the compression from 0 to 100 (higher is better
and slower).
- progressive: An optional bool, default is false. If true, create a JPEG that loads progressively (coarse
to fine).
- optimize_size: An optional bool, default is false. If true, spend CPU/RAM to reduce size with no quality
change.
- chroma_downsampling: An optional bool, default is true.
- density_unit: An optional string, default is "in". Unit used to specify x_density and y_density: pixels per
inch ('in') or centimeter ('cm').
- x_density: An optional int, default is 300. Horizontal pixels per density unit.
- y_density: An optional int, default is 300. Vertical pixels per density unit.
- xmp_metadata: An optional string, default is "". If not empty, embed this XMP metadata in the image header .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 image: uint8
- output0 contents: string

## Third-party framework compatibility

Compatible with tensorflow EncodeJpeg operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
