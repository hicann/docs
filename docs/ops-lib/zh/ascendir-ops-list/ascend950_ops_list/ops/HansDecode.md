# HansDecode

```c
REG_OP(HansDecode)
    .INPUT(mantissa, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .INPUT(fixed, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .INPUT(var, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .INPUT(pdf, TensorType({DT_INT32}))
    .OUTPUT(output, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .ATTR(reshuff, Bool, false)
    .OP_END_FACTORY_REG(HansDecode)
```

## Brief

Losslessly decompress.

## Inputs

Four inputs, including:
- mantissa: Encode mantissa output. Must be one of the following types: bfloat16, float16, float32.
- fixed: Compress output part 1. The type must be the same as mantissa.
- var: Compress output part 1. The type must be the same as mantissa.
- pdf: A tensor of type int32, with shape(1, 256). Exponential bit frequency distribution of input tensor.

## Outputs

output: A continuous tensor to be decompressed. The type must be the same as mantissa.

## Attributes

- reshuff: An optional bool, specifying whether reshuff results on continuous memory.
True: the result of multi-core compression is not reshuffled;
False: the result of multi-core compression is reshuffled in memory. Default to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 mantissa: bfloat16,float16,float32
- input1 fixed: bfloat16,float16,float32
- input2 var: bfloat16,float16,float32
- input3 pdf: int32
- output0 output: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the PyTorch operator HansDecode.


---

[Back to Operator Specifications (Ascend950)](../README.md)
