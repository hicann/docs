# SwigluGroupGrad

```c
REG_OP(SwigluGroupGrad)
    .INPUT(grad_y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(weight, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(y_origin, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(group_index, TensorType({DT_INT64}))
    .OUTPUT(grad_x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(grad_weight, TensorType({DT_FLOAT}))
    .ATTR(clamp_limit, Float, 0)
    .OP_END_FACTORY_REG(SwigluGroupGrad)
```

## Brief

Compute the SwigluGroupGrad — gradient of ClampedSwiglu activation.

## Inputs

five inputs, including:
- grad_y: A required 2D or 3D Tensor of shape (..., H). Must be one of: bfloat16, float16, float32.
- x: A required Tensor of shape (..., 2H) and the same rank as grad_y.
    Must be one of: bfloat16, float16, float32.
- weight: An optional Tensor of shape (..., 1) with dtype float32. MoE top-k routing weight.
    It must be provided together with y_origin.
- y_origin: An optional Tensor of shape (..., H) with same dtype as grad_y. Forward output y,
    including weight multiplication when weight is present.
    It must be provided together with weight.
- group_index: An optional non-empty Tensor of shape (G,), G > 0, with dtype int64. Token/batch count per group.

## Outputs

two outputs, including:
- grad_x: A required Tensor of shape (..., 2H) with same dtype as grad_y. Gradient of x.
- grad_weight: An optional Tensor of shape (..., 1) with dtype float32. Gradient of weight.

## Attributes

one attribute:
- clamp_limit: An optional Float. Clipping threshold c; default 0 means no clamp (c=+∞).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad_y: bfloat16,float16,float32
- input1 x: bfloat16,float16,float32
- input2 weight: float32
- input3 y_origin: bfloat16,float16,float32
- input4 group_index: int64
- output0 grad_x: bfloat16,float16,float32
- output1 grad_weight: float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
