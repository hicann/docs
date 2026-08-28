# DequantSituQuant

```c
REG_OP(DequantSituQuant)
    .INPUT(x, TensorType({DT_INT8, DT_INT32, DT_BF16, DT_FLOAT16}))
    .OPTIONAL_INPUT(weight_scale, TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .OPTIONAL_INPUT(activation_scale, TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .OPTIONAL_INPUT(quant_scale, TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .OPTIONAL_INPUT(quant_offset, TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .OPTIONAL_INPUT(group_index, TensorType({DT_INT64, DT_INT64, DT_INT64, DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT8, DT_INT8, DT_INT8, DT_INT8}))
    .OUTPUT(y_scale, TensorType({DT_FLOAT, DT_FLOAT, DT_FLOAT, DT_FLOAT}))
    .ATTR(beta, Float, 4.0)
    .ATTR(linear_beta, Float, 25.0)
    .ATTR(activate_left, Bool, true)
    .ATTR(quant_type, String, "dynamic")
    .OP_END_FACTORY_REG(DequantSituQuant)
```

## Brief

Combine Dequant + Situ + Quant.

## Inputs

Seven inputs:
- x: Required tensor. INT8 for per-channel dequant path; INT32 for MoE grouped-matmul accumulator;
       BF16 for pre-dequantized path; FLOAT16 for pre-dequantized path. Shape is (N..., H) for INT8
       (dim > 1, H even) or [rows, width] for INT32/BF16/FLOAT16.
- weight_scale: Optional FP32. Per-channel or per-expert dequantization scale. Required for INT32 x.
- activation_scale: Optional FP32. Per-row dequantization scale (one value per row). Required for INT32 x.
- bias: Optional FP32. Dequantization bias, same shape as weight_scale.
- quant_scale: Optional FP32. Static quant scale or dynamic smooth scale.
- quant_offset: Optional FP32. Static quant offset.
- group_index: Optional INT64 [experts]. Per-expert consecutive routed row counts for MoE.

## Outputs

- y: INT8 tensor. Last dim is x last dim / 2.
- y_scale: FP32 tensor. Per-row dynamic quant scale (meaningless for static mode).

## Attributes

- beta: Float. The beta parameter for Situ activation. Default is 4.0.
- linear_beta: Float. The linear_beta parameter for Situ activation. When value <= 0, the linear_beta
transformation is not applied. Default is 25.0.
- activate_left: Bool. Whether gate is the left half (true) or right half (false). Default is true.
- quant_type: String. The quant type to use: 'static' or 'dynamic', default is 'dynamic'.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,int8,int32
- input1 weight_scale: float32
- input2 activation_scale: float32
- input3 bias: float32
- input4 quant_scale: float32
- input5 quant_offset: float32
- input6 group_index: int64
- output0 y: int8
- output1 y_scale: float32

## Attention Constraints

- The last dimension of x must be even.
- INT8 path: weight_scale required, activation_scale/group_index must be absent, x dim > 1.
- INT32 path: weight_scale and activation_scale required, quant_scale/quant_offset must be absent,
       x rank == 2, quant_type must be dynamic.
- BF16 path: weight_scale/activation_scale/bias/group_index must be absent, x rank == 2,
       quant_type must be dynamic.
- FLOAT16 path: weight_scale/activation_scale/bias/group_index must be absent, x rank == 2,
       quant_type must be dynamic.
- When quant_type is 'static', quant_scale must be provided.
- When quant_type is 'dynamic', quant_scale is optional (used as smoothScale).


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
