# QuantizeAddLayerNorm

```c
REG_OP(QuantizeAddLayerNorm)
    .INPUT(x1, ge::TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(x2, ge::TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(gamma, ge::TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(beta, ge::TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(bias, ge::TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(scales, ge::TensorType({DT_FLOAT, DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(zero_points, ge::TensorType({DT_FLOAT, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, ge::TensorType({DT_INT8, DT_INT8, DT_INT8}))
    .OUTPUT(x, ge::TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(dtype, Int)
    .ATTR(axis, Int, -1)
    .ATTR(epsilon, Float, 1e-5f)
    .ATTR(additional_output, Bool, false)
    .OP_END_FACTORY_REG(QuantizeAddLayerNorm)
```

## Brief

QuantizeAddLayerNorm operator interface implementation.

## Inputs

- x1: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- x2: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- gamma: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- beta: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- bias: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].
- scales: A Tensor. Support dtype: [float32, bfloat16], support format: [ND].
- zero_points: A optional Tensor. Support dtype: [float32, bfloat16], support format: [ND].

## Outputs

- y: A Tensor. Support dtype: [int8], support format: [ND].
- x: A Tensor. Support dtype: [float32, float16, bfloat16], support format: [ND].

## Attributes

- dtype: A required attribute, the type is int. No defaults value.
- axis: A optional attribute, the type is int. Defaults to -1.
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
- input5 scales: bfloat16,float32
- input6 zero_points: bfloat16,float32
- output0 y: int8
- output1 x: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
