# Quantize

```c
REG_OP(Quantize)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(scales, TensorType({DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(zero_points, TensorType({DT_INT8, DT_UINT8, DT_INT32, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_INT8, DT_UINT8, DT_INT32, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .REQUIRED_ATTR(dtype, String)
    .ATTR(axis, Int, 1)
    .OP_END_FACTORY_REG(Quantize)
```

## Brief

Quantizes the input, scales/zero_points support broadcasting operations. 

## Inputs

- x: A required tensor of type float16, float32 or bfloat16, specifying the input.
- scales: A required tensor of type float32 or bfloat16, specifying the scaling ratio.
- zero_points: An optional tensor of type int8, uint8, int32, float32 or bfloat16, specifying the offset.

## Outputs

y: A required tensor of type int8, uint8, int32, hifloat8, float8_e5m2 or float8_e4m3fn, shape should be the same
with input x, dtype should be consistent with attributes[dtype]. 

## Attributes

- dtype: A required string from "torch.qint8, torch.quint8, torch.qint32, torch.hifloat8, torch.float8_e5m2,
torch.float8_e4m3fn", specifying the quantified dtype.
- axis: An optional int, must be in the range [-rank(input x), rank(input x)), describes which dimension of the
input tensor x to be processed. When scales's dimension number and size is 1, axis makes no effect. Default is 1. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 scales: float32
- input2 zero_points: int8,int32,uint8
- output0 y: int8,int32,uint8

## Attention Constraints

- When scales or zero_points's dtype is bfloat16, other inputs' dtype should also be bfloat16.
- Scales and zero_points's shape should be the same.
- Scales and zero_points's dimension number should be 1 or the same with x.
- When scales's dimension number is 1, it should be 1 or the same with the dimension specified by attributes[axis]
of input x.
- When scales's dimension number is the same with x, the dimension specified by attributes[axis] shoule be 1 or the
same with x's, others should be 1. 


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
