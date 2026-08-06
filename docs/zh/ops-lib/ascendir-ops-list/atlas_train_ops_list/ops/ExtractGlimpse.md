# ExtractGlimpse

```c
REG_OP(ExtractGlimpse)
    .INPUT(x, TensorType({DT_FLOAT}))
    .INPUT(size, TensorType({DT_INT32}))
    .INPUT(offsets, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .ATTR(centered, Bool, true)
    .ATTR(normalized, Bool, true)
    .ATTR(uniform_noise, Bool, true)
    .ATTR(noise, String, "uniform")
    .OP_END_FACTORY_REG(ExtractGlimpse)
```

## Brief

Extracts a glimpse from the input tensor . 

## Inputs

Input x must be a 4-D tensor. Inputs include:
- x: A 4-D float tensor of shape [batch_size, height, width, channels].
The format must be NHWC, tensor of type float.
- size: A 1-D tensor of 2 elements containing the size of the glimpses to
extract. The glimpse height must be specified first, following by the glimpse
width, tensor of type int32.
- offsets: A 2-D integer tensor of shape [batch_size, 2] containing the y,
x locations of the center of each window , tensor of type float. 

## Outputs

y:A tensor representing the glimpses [batch_size, glimpse_height,
glimpse_width, channels]. The format must be NHWC. 

## Attributes

- centered: An optional bool, default is true, indicates if the offset coordinates are centered relative to
the image, in which case the (0, 0) offset is relative to the center of the
input images. If false, the (0,0) offset corresponds to the upper left corner
of the input images.
- normalized: An optional bool, default is true, indicates if the offset coordinates are normalized.
- uniform_noise: An optional bool, default is true, indicates if the noise should be generated using a
uniform distribution or a Gaussian distribution.
- noise: An optional string, default is "uniform", indicates if the noise should uniform, gaussian, or zero.
The default is uniform which means the the noise type will be decided by
uniform_noise . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: float32
- input1 size: int32
- input2 offsets: float32
- output0 y: float32

## Attention Constraints

Input x must be a 4-D tensor . 

## Third-party framework compatibility

Compatible with tensorflow CropAndResizeGradImage operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
