# DynamicDualLevelMxQuant

```c
REG_OP(DynamicDualLevelMxQuant)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(smooth_scale, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT4_E2M1}))
    .OUTPUT(level0_scale, TensorType({DT_FLOAT}))
    .OUTPUT(level1_scale, TensorType({DT_FLOAT8_E8M0}))
    .ATTR(round_mode, String, "rint")
    .ATTR(level0_block_size, Int, 512)
    .ATTR(level1_block_size, Int, 32)
    .OP_END_FACTORY_REG(DynamicDualLevelMxQuant)
```

## Brief

Online quantizes the input tensor per block.Then performs dynamic MX quantization on the output tensor.

## Inputs

- x: An input tensor of type float16 or bfloat16.the input x last dimension of the shape must be divisible by 2.
The shape supports at least 1 dimension, and at most 7 dimensions.
- smooth_scale: An optional tensor, the smooth scale for x

## Outputs

- y: Quantized output tensor. It has the same shape and rank as input x.
- level0_scale: An output tensor of type float. if x is [M,N],level0_scale shape is [M,ceil(N/level0_block_size)]
- level1_scale: An output tensor of type FLOAT8_E8M0. Shape needs to meet the following conditions:
- if x is [M,N]
- axis_change = axis if axis >= 0 else axis + rank(x).
- level1_scale shape is [M,ceil(N/(level1_block_size * 2)),2]
- level1_scale tensor is padded with zeros to ensure its size along the quantized axis is even.

## Attributes

- round_mode: An optional string.
The value range is ["rint", "round", "floor"]. Defaults to "rint".
- level0_block_size: An optional int, specifying the block size of block quantization.
Defaults and only supports 512.
- level1_block_size: An optional int, specifying the block size of mx quantization.
Defaults and only supports 32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- input1 smooth_scale: bfloat16,float16
- output0 y: float4_e2m1
- output1 level0_scale: float32
- output2 level1_scale: float8_e8m0

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe, ONNX, TensorFlow, or PyTorch.


---

[Back to Operator Specifications (Ascend950)](../README.md)
