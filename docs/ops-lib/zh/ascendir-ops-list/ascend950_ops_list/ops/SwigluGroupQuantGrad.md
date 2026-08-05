# SwigluGroupQuantGrad

```c
REG_OP(SwigluGroupQuantGrad)
    .INPUT(grad_y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(weight, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(y_origin, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(group_index, TensorType({DT_INT64}))
    .OUTPUT(grad_x, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(grad_weight, TensorType({DT_FLOAT}))
    .ATTR(clamp_limit, Float, -1.0f)
    .OP_END_FACTORY_REG(SwigluGroupQuantGrad)
```

## Brief

SwiGLU Group Dynamic Quant Backward operator.

## Inputs

- grad_y: Gradient input tensor. Must be one of the following types: float32,float16,bfloat16, has format ND.
- x: Forward pass input tensor. Must be one of the following types: float32,float16,bfloat16, has format ND.
- weight: Optional tensor. topk weight tensor. Type is float32, has format ND.
- y_origin: Optional tensor. Forward pass output before quantization.
Must be one of the following types: float32,float16,bfloat16, has format ND.
- group_index: Optional tensor. Group index tensor for dynamic quantization. Type is int64, has format ND.

## Outputs

- grad_x: Gradient of x tensor. Same type as input x, has format ND.
- grad_weight: Optional output. Gradient of weight tensor. Type is float32, has format ND.

## Attributes

- clamp_limit: Optional float. Clamp value for gradient mask, default is -1.0 (no clamp).
    If set to a positive value, clamps SwiGLU inputs before activation. Must be -1.0 or > 0.

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
