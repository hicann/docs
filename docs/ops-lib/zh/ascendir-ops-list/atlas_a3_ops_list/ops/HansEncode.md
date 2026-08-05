# HansEncode

```c
REG_OP(HansEncode)
    .INPUT(input_tensor, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .INPUT(pdf, TensorType({DT_INT32}))
    .OUTPUT(pdf, TensorType({DT_INT32}))
    .OUTPUT(mantissa, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(fixed, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(var, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .ATTR(statistic, Bool, false)
    .ATTR(reshuff, Bool, false)
    .OP_END_FACTORY_REG(HansEncode)
```

## Brief

Losslessly compress the exponent bits of the input tensor.

## Inputs

Two inputs, including:
- input_tensor: A continuous tensor to be compressed. Number of elements must be a multiple of 64.
Must be one of the following types: bfloat16, float16, float32.
- pdf: A tensor of type int32, with shape(1, 256). Exponential bit frequency distribution of input tensor.

## Outputs

- pdf: An int32 tensor specifying the exponential bit frequency distribution of the input tensor,
valid when statistic is true.
- mantissa: Mantissa output. The type must be the same as input_tensor.
- fixed: Compress output part 1. The type must be the same as input_tensor.
- var: Compress output part 2. The type must be the same as input_tensor.

## Attributes

- statistic: An optional bool, specifying whether to compute the statistic PDF.
True: use the online statistical pdf;
False: use the input pdf. Defaults to false.
- reshuff: An optional bool, specifying whether reshuff compression results on continuous memory. Default to false.
True: the result of multi-core compression is not reshuffled;
False: the result of multi-core compression is reshuffled in memory. Default to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_tensor: bfloat16,float16,float32
- input1 pdf: int32
- output0 pdf: int32
- output1 mantissa: bfloat16,float16,float32
- output2 fixed: bfloat16,float16,float32
- output3 var: bfloat16,float16,float32

## Attention Constraints

The sum of fixed tensor and var tensor size must be greater than
(size(input_tensor) + size(input_tensor) / 64 + 8448 * processCoreDim + 512).

## Third-party framework compatibility

Compatible with the PyTorch operator HansEncode.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
