# ExtractImagePatches

```c
REG_OP(ExtractImagePatches)
    .INPUT(x, TensorType::RealNumberType())
    .OUTPUT(y, TensorType::RealNumberType())
    .REQUIRED_ATTR(ksizes, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(rates, ListInt)
    .REQUIRED_ATTR(padding, String)
    .OP_END_FACTORY_REG(ExtractImagePatches)
```

## Brief

Extract "patches" from "images" and stacks them in the "depth"
dimension of the output . 

## Inputs

x: A Tensor with shape [batch, depth, in_rows, in_cols] or [batch, depth1, in_rows, in_cols, depth0].
Support dtype: [float16, float32, bfloat16, int8, uint8]
Support format: When x dtype is in [float16, float32, bfloat16], format support: [NCHW, NC1HWC0].
When x dtype is in [int8, uint8], format support: [NC1HWC0].

## Outputs

y: A Tensor with shape [batch, out_rows, out_cols, ksize_rows *
ksize_cols * depth] containing image patches with size ksize_rows x ksize_cols
x depth vectorized in the "depth" dimension. Note "out_rows" and "out_cols"
are the dimensions of the output patches . Support dtype: [float16, float32, bfloat16, int8, uint8],
Support format: [NHWC] 

## Attributes

- ksizes: A required list or tuple. The size of the sliding window for each
dimension of images.
- strides: A required list or tuple. How far the centers of two consecutive
patches are in the images. Must be: [1, stride_rows, stride_cols, 1].
- rates: A required list or tuple. Must be: [1, rate_rows, rate_cols, 1].
This is the input stride, specifying how far two consecutive patch
samples are in the input. Equivalent to extracting patches
with patch_sizes_eff = patch_sizes + (patch_sizes - 1) *
(rates - 1), followed by subsampling them spatially by a factor of rates.
This is equivalent to rate in dilated (a.k.a. Atrous) convolutions.
- padding: A required string. The type of padding algorithm to use,
support "SAME" or "VALID". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

"ksizes", "strides" and "rates" are lists of integers . 

## Third-party framework compatibility

Compatible with the TensorFlow operator ExtractImagePatches.


---

[Back to Operator Specifications (Ascend950)](../README.md)
