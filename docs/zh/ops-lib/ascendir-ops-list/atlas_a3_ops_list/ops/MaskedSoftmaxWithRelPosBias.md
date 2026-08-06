# MaskedSoftmaxWithRelPosBias

```c
REG_OP(MaskedSoftmaxWithRelPosBias)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BFLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(atten_mask, TensorType({DT_FLOAT16, DT_BFLOAT16, DT_FLOAT}))
    .INPUT(relative_pos_bias, TensorType({DT_FLOAT16, DT_BFLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BFLOAT16, DT_FLOAT}))
    .ATTR(scale_value, Float, 1.0)
    .ATTR(inner_precision_mode, Int, 0)
    .OP_END_FACTORY_REG(MaskedSoftmaxWithRelPosBias)
```

## Brief

swin_transformer model specific structure.Operator only supports swin_transformer.

## Inputs

Three inputs, including:
- x: An ND Tensor. Must be one of the following types: float16, float, bfloat16,
the shape should be (B*W, N, S1, S2) or (B, W, N, S1, S2).
- atten_mask: An ND Tensor. Must be one of the following types: float16, float, bfloat16,
the shape should be (W, S1, S2) or (W, 1, S1, S2) or (1, W, 1, S1, S2)
- relative_pos_bias: An ND Tensor. Must be one of the following types: float16, float, bfloat16.
the shape sholud be (N, S1, S2) or (1, N, S1, S2) or (1, 1, N, S1, S2)

## Outputs

One output, including:
- y: An ND Tensor. Must be one of the following types: float16, float, bfloat16,
the shape should be same with x.

## Attributes

- scale_value: A optional attribute, the type is float. Defaults to 1.0.
- inner_precision_mode: A optional attribute, the type is int. Defaults to 0, reserved field.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 atten_mask: bfloat16,float16,float32
- input2 relative_pos_bias: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
