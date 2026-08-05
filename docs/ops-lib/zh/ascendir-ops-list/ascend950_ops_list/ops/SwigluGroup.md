# SwigluGroup

```c
REG_OP(SwigluGroup)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(weight, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(group_index, TensorType({DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .ATTR(clamp_limit, Float, -1.0f)
    .OP_END_FACTORY_REG(SwigluGroup)
```

## Brief

Performs SwiGLU activation.

## Inputs

- x: Required tensor of type float16, bfloat16 or float32. The last dimension is split into two
equal parts for SwiGLU and must be divisible by 2.
- weight: Optional float32 tensor. Per-token weight multiplied into the SwiGLU result.
- group_index: Optional int64 tensor. Count-mode group token numbers.

## Outputs

- y: SwiGLU result tensor with the same dtype as x and last dimension halved.

## Attributes

- clamp_limit: Optional float. Defaults to -1.0, which disables clamp. If set to a positive value,
clamps SwiGLU inputs before activation.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 weight: float32
- input2 group_index: int64
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe, ONNX, TensorFlow, or PyTorch.


---

[Back to Operator Specifications (Ascend950)](../README.md)
