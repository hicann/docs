# DequantRopeQuantKvcache

```c
REG_OP(DequantRopeQuantKvcache)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16, DT_INT32}))
    .INPUT(cos, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(sin, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(k_cache, TensorType({DT_INT8}))
    .INPUT(v_cache, TensorType({DT_INT8}))
    .INPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .INPUT(scale_k, TensorType({DT_FLOAT32}))
    .INPUT(scale_v, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(offset_k, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(offset_v, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(weight_scale, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(activation_scale, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT32, DT_BF16, DT_FLOAT16, DT_INT32}))
    .OUTPUT(q, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(k, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(v, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(k_cache, TensorType({DT_INT8}))
    .OUTPUT(v_cache, TensorType({DT_INT8}))
    .REQUIRED_ATTR(size_splits, ListInt)
    .ATTR(quant_mode, String, "static")
    .ATTR(layout, String, "BSND")
    .ATTR(kv_output, Bool, false)
    .ATTR(cache_mode, String, "contiguous")
    .OP_END_FACTORY_REG(DequantRopeQuantKvcache)
```

## Brief

Fusion op DequantRopeQuantKvcache.

## Inputs

thirteen inputs, including:
- x: A Tensor with shape (B, S, H) or (B, H), H is (Nq+Nkv+Nkv)*D, format support ND.
The type support float16, bf16, int32.
- cos: A Tensor with shape (B, S, 1, D) or (B, D). The type support float16, bf16, format support ND.
- sin: A Tensor with shape (B, S, 1, D) or (B, D). The type support float16, bf16, format support ND.
- k_cache: A Tensor with shape (C_1, C_2, Nkv, D) indicates kcache for in-place updates.
The type support int8, format support ND.
- v_cache: A Tensor with shape (C_1, C_2, Nkv, D) indicates vcache for in-place updates.
The type support int8, format support ND.
- indices: A Tensor with shape (B) when cache_mode is contiguous with shape (B * S) when cache_mode is page.
The type support int32, format support ND.
- scale_k: A Tensor with shape (Nkv, D). The type support float32, format support ND.
- scale_v: A Tensor with shape (Nkv, D). The type support float32, format support ND.
- offset_k: A Tensor with shape (Nkv, D). An optional input parameter. The type support float32.
format support ND.
- offset_v: A Tensor with shape (Nkv, D). An optional input parameter. The type support float32.
format support ND.
- weight_scale: A Tensor with shape (D) indicates the weight scale factor of the dequantization parameter.
An optional input parameter. The type support float32.
- activation_scale: A Tensor with shape (B * S) or (B) indicates the activation scale factor of the dequantization parameter.
An optional input parameter. The type support float32.
- bias: A Tensor with shape (D). An optional input parameter. The type support float32, bf16, float16, int32.

## Outputs

- q: A Tensor with shape (B, S, Nq, D) or (B, Nq, D). The type support float16, bf16.
- k: A Tensor with shape (B, S, Nkv, D) or (B, Nkv, D). The type support float16, bf16.
- v: A Tensor with shape (B, S, Nkv, D) or (B, Nkv, D). The type support float16, bf16.
- k_cache: A Tensor with shape (C_1, C_2, Nkv, D). The type support int8, format support ND.
- v_cache: A Tensor with shape (C_1, C_2, Nkv, D). The type support int8, format support ND.

## Attributes

- size_splits: A list of int. Specifies the size of spliting qkv.
- quant_mode: A string. A optional attribute. Specifies the method of quant. Default: "static".
- layout: A string. A optional attribute. Specifies the format of input. Default: "BSND".
- kv_output: A bool. A optional attribute. Whether to output kv. Default: "false".
- cache_mode:  A string. A optional attribute. Specifies the cache mode for kcache and vcache.
   Should be "contiguous" or "page", default is "contiguous".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,int32
- input1 cos: bfloat16,float16
- input2 sin: bfloat16,float16
- input3 k_cache: int8
- input4 v_cache: int8
- input5 indices: int32
- input6 scale_k: float32
- input7 scale_v: float32
- input8 offset_k: float32
- input9 offset_v: float32
- input10 weight_scale: float32
- input11 activation_scale: float32
- input12 bias: bfloat16,float16,float32,int32
- output0 q: bfloat16,float16
- output1 k: bfloat16,float16
- output2 v: bfloat16,float16
- output3 k_cache: int8
- output4 v_cache: int8


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
