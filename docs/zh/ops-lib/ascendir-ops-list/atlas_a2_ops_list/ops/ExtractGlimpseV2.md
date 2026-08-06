# ExtractGlimpseV2

```c
REG_OP(ExtractGlimpseV2)
    .INPUT(input, TensorType({DT_FLOAT}))
    .INPUT(size, TensorType({DT_INT32}))
    .INPUT(offsets, TensorType({DT_FLOAT}))
    .OUTPUT(glimpse, TensorType({DT_FLOAT}))
    .ATTR(centered, Bool, true)
    .ATTR(normalized, Bool, true)
    .ATTR(uniform_noise, Bool, true)
    .ATTR(noise, String, "uniform")
    .OP_END_FACTORY_REG(ExtractGlimpseV2)
```

## Brief

Extracts a glimpse from the input tensor . 

## Inputs

Input input must be a 4-D tensor. Inputs include:
- input: A 4-D float tensor of shape [batch_size, height, width, channels].
The format must be NHWC.
- size: A ND(Support 1D) int32 tensor of 2 elements containing the size of the
glimpses to extract. The glimpse height must be specified first, following
by the glimpse width.
- offsets: A ND(Support 2D) float32 tensor of shape [batch_size, 2] containing the y,
x locations of the center of each window . 

## Outputs

glimpse:A float32 tensor representing the glimpses [batch_size,
glimpse_height, glimpse_width, channels]. The format must be NHWC. 

## Attributes

- centered: bool indicates if the offset coordinates are centered
relative to the image, in which case the (0, 0) offset is relative to the
center of the input images. If false, the (0,0) offset corresponds to the
upper left corner of the input images.
- normalized: bool indicates if the offset coordinates are normalized.
- uniform_noise: bool indicates if the noise should be generated using a
uniform distribution or a Gaussian distribution.
- noise: string indicates if the noise should uniform, gaussian, or zero.
The default is uniform which means the the noise type will be decided by
uniform_noise . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input: float32
- input1 size: int32
- input2 offsets: float32
- output0 glimpse: float32

## Third-party framework compatibility

Compatible with tensorflow ExtractGlimpseV2 operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
