# DuaQuantizeAddLayerNorm

```c
REG_OP(DuaQuantizeAddLayerNorm)
    .INPUT(x1, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(x2, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(gamma, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(beta, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(bias, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(scales1, ge::TensorType({DT_BF16, DT_FLOAT}))
    .INPUT(scales2, ge::TensorType({DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(zero_points1, ge::TensorType({DT_INT8, DT_UINT8, DT_BF16, DT_INT32}))
    .OPTIONAL_INPUT(zero_points2, ge::TensorType({DT_INT8, DT_UINT8, DT_BF16, DT_INT32}))
    .OUTPUT(y1, ge::TensorType({DT_INT8, DT_UINT8, DT_INT32}))
    .OUTPUT(y2, ge::TensorType({DT_INT8, DT_UINT8, DT_INT32}))
    .OUTPUT(x, ge::TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .REQUIRED_ATTR(dtype, Int)
    .ATTR(axis, Int, -1)
    .ATTR(epsilon, Float, 1e-5f)
    .ATTR(additional_output, Bool, false)
    .OP_END_FACTORY_REG(DuaQuantizeAddLayerNorm)
```

## Brief

DuaQuantizeAddLayerNorm operator interface implementation.

## Inputs

- x1: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- x2: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- gamma: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- beta: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- bias: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- scales1: A Tensor. Support dtype: [float32, bfloat16], support format: [ND].
- scales2: A Tensor. Support dtype: [float32, bfloat16], support format: [ND].
- zero_points1: A optional Tensor. Support dtype: [int8, uint8, bfloat16, int32], support format: [ND].
- zero_points2: A optional Tensor. Support dtype: [int8, uint8, bfloat16, int32], support format: [ND].

## Outputs

- y1: A Tensor. Support dtype: [int8, uint8, int32], support format: [ND].
- y2: A Tensor. Support dtype: [int8, uint8, int32], support format: [ND].
- x: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].

## Attributes

- dtype: A required attribute, the type is int. No defaults value.
- axis: A optional attribute, the type is float. Defaults to -1.
- epsilon: A optional attribute, the type is float. Defaults to 1e-5.
- additional_output: A optional attribute, the type is bool. Defaults to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32
- input1 x2: bfloat16,float16,float32
- input2 gamma: bfloat16,float16,float32
- input3 beta: bfloat16,float16,float32
- input4 bias: bfloat16,float16,float32
- input5 scales1: bfloat16,float16,float32
- input6 scales2: bfloat16,float16,float32
- input7 zero_points1: bfloat16,float16,float32
- input8 zero_points2: bfloat16,float16,float32
- output0 y1: int8
- output1 y2: int8
- output2 x: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
