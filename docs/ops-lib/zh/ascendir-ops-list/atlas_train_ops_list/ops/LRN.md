# LRN

```c
REG_OP(LRN)
    .INPUT(x, TensorType({DT_FLOAT16,DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16,DT_FLOAT}))
    .ATTR(depth_radius, Int, 5)
    .ATTR(bias, Float, 1.0)
    .ATTR(alpha, Float, 1.0)
    .ATTR(beta, Float, 0.5)
    .ATTR(norm_region, String, "ACROSS_CHANNELS")
    .OP_END_FACTORY_REG(LRN)
```

## Brief

Local Response Normalization .

## Inputs

One input, including:
x: A Tensor. Must be 4-D shape, and only support the following types: float16, float32 . 

## Outputs

y: A Tensor. Has the same data type and shape as "x" . 

## Attributes

- depth_radius: An optional int32, specifying the half-width of the normalization window. Defaults to "5".
under the caffe framework, if local_size is provided and is an odd number,
depth_radius = (local_size - 1) / 2. local_size is the number of channels to sum over (for ACROSS_CHANNELS)
or the side length of the square region to sum over (for WITHIN_CHANNEL).
- bias: An optional float32. An offset, usually > 0 to avoid dividing by 0.
Defaults to "1.0".
- alpha: An optional float32. A scaling factor, usually positive.
Defaults to "1.0".
- beta: An optional float32. An exponent. Defaults to "0.75" for the caffe framework, Defaults to "0.5" for others.
- norm_region: An optional string. A mode option. "ACROSS_CHANNELS":0. Defaults to "ACROSS_CHANNELS" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Attention Constraints

This operator will be deprecated in the future. Replace it with LayerNorm operator. 

## Third-party framework compatibility

Compatible with the TensorFlow operator LRN.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
