# RopeQuantKvcache

```c
REG_OP(RopeQuantKvcache)
    .INPUT(qkv, TensorType({DT_FLOAT16}))
    .INPUT(cos, TensorType({DT_FLOAT16}))
    .INPUT(sin, TensorType({DT_FLOAT16}))
    .INPUT(quant_scale, TensorType({DT_FLOAT32}))
    .INPUT(quant_offset, TensorType({DT_INT32}))
    .INPUT(k_cache, TensorType({DT_INT8}))
    .INPUT(v_cache, TensorType({DT_INT8}))
    .INPUT(indice, TensorType({DT_INT32}))
    .OUTPUT(q, TensorType({DT_FLOAT16}))
    .OUTPUT(k, TensorType({DT_FLOAT16}))
    .OUTPUT(v, TensorType({DT_FLOAT16}))
    .OUTPUT(k_cache, TensorType({DT_INT8}))
    .OUTPUT(v_cache, TensorType({DT_INT8}))
    .ATTR(size_splits, ListInt, {})
    .ATTR(layout, String, "BSND")
    .ATTR(kv_output, Bool, false)
    .OP_END_FACTORY_REG(RopeQuantKvcache)
```

## Brief

Fusion ops for splitvd rope quantize scatter.

## Inputs

eight inputs, including:
- qkv: A 3D Tensor of type float16 with shape (B, S, H), H is (Nq+Nkv+Nkv)*D, format support ND
- cos: A 4D Tensor of type float16 with shape (B, S, 1, D), shape must same with k, format support ND
- sin: A 4D Tensor of type float16 with shape (B, S, 1, D), shape must same with k, format support ND
- quant_scale: A 1D Tensor of type float with shape (D), shape D must same with k, format support ND
- k_cache: A 4D Tensor of type int8 with shape (B, S, Nkv, D), shape B/N/D must same with k,
S must large than k, format support ND
- v_cache: A 4D Tensor of type int8 with shape (B, S, Nkv, D), shape B/N/D must same with v,
S must large than k, format support ND
- indice: A 1D Tensor of type int32 with shape (B), shape must same with qkv, format support ND

## Outputs

- q: A 4D Tensor of type float16 with shape (B, S, Nq, D), split from qkv, format support ND
- k: A 4D Tensor of type float16 with shape (B, S, Nkv, D), split from qkv, N must same with v, format support ND
- v: A 4D Tensor of type float16 with shape (B, S, Nkv, D), split from qkv, N must same with k, format support ND
- k_cache: A 4D Tensor of type int8 with shape (B, S, Nkv, D), shape B/N/D must same with k, S must large than k,
format support ND
- v_cache: A 4D Tensor of type int8 with shape (B, S, Nkv, D), shape B/N/D must same with v, S must large than v,
format support ND
It is a custom operator.

## Attributes

- size_splits: list to split qkv input tensor to q/k/v, default is null.
- layout: qkv input tensor layout, like BSND/BNSD, default is BSND.
- kv_output: control origin k/v output or not, default is false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 qkv: float16
- input1 cos: float16
- input2 sin: float16
- input3 quant_scale: float32
- input4 quant_offset: int32
- input5 k_cache: int8
- input6 v_cache: int8
- input7 indice: int32
- output0 q: float16
- output1 k: float16
- output2 v: float16
- output3 k_cache: int8
- output4 v_cache: int8


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
