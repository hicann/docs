# ExtractVolumePatches

```c
REG_OP(ExtractVolumePatches)
    .INPUT(x, TensorType::REALNUMBERTYPE())
    .OUTPUT(y, TensorType::REALNUMBERTYPE())
    .REQUIRED_ATTR(ksizes, ListInt)
    .REQUIRED_ATTR(strides, ListInt)
    .REQUIRED_ATTR(padding, String)
    .OP_END_FACTORY_REG(ExtractVolumePatches)
```

## Brief

Extract "patches" from "input" and put them in the "depth"
dimension of the output . 

## Inputs

x: A Tensor with shape [batch, in_planes, depth1, in_rows, in_cols, depth0] . 
   Support dtype: [float16,int8,uint8] 
   Support format: [NDC1HWC0] 

## Outputs

Output: A Tensor with shape [batch, out_planes, out_rows, out_cols, ksize_planes *
ksize_rows * ksize_cols * depth] containing patches with size (ksize_rows * ksize_cols
* depth) vectorized in the "depth" dimension. Note "out_planes", "out_rows" and "out_cols"
are the dimensions of the output patches . 
   Support dtype: [float16,int8,uint8]. 
   Support format: [NDC1HWC0] 

## Attributes

- ksizes: A required list or tuple. The size of the sliding window for each
dimension of "x".
- strides: A required list or tuple. How far the centers of two consecutive
patches are in "x". Must be: [1, stride_planes, stride_rows, stride_cols, 1].
- padding: A required string. The type of padding algorithm to use ,
support "SAME" or "VALID" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,int8,uint8
- output0 y: float16,int8,uint8

## Attention Constraints

"ksizes" and "strides" are lists of integers.

## Third-party framework compatibility

Compatible with the TensorFlow operator ExtractVolumePatches.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
