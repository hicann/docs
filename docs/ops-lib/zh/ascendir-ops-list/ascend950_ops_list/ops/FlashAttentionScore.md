# FlashAttentionScore

```c
REG_OP(FlashAttentionScore)
    .INPUT(query, TensorType({DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .INPUT(key, TensorType({DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .INPUT(value, TensorType({DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OPTIONAL_INPUT(real_shift, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OPTIONAL_INPUT(drop_mask, TensorType({DT_UINT8}))
    .OPTIONAL_INPUT(padding_mask, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OPTIONAL_INPUT(atten_mask, TensorType({DT_BOOL, DT_UINT8}))
    .OPTIONAL_INPUT(prefix, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(actual_seq_qlen, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(actual_seq_kvlen, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(q_start_idx, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(kv_start_idx, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(d_scale_q, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(d_scale_k, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(d_scale_v, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(query_rope, TensorType({DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OPTIONAL_INPUT(key_rope, TensorType({DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OPTIONAL_INPUT(sink, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(p_scale, TensorType({DT_FLOAT32}))
    .OUTPUT(softmax_max, TensorType({DT_FLOAT32}))
    .OUTPUT(softmax_sum, TensorType({DT_FLOAT32}))
    .OUTPUT(softmax_out, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OUTPUT(attention_out, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .ATTR(scale_value, Float, 1.0)
    .ATTR(keep_prob, Float, 1.0)
    .ATTR(pre_tockens, Int, 2147483647)
    .ATTR(next_tockens, Int, 2147483647)
    .REQUIRED_ATTR(head_num, Int)
    .REQUIRED_ATTR(input_layout, String)
    .ATTR(inner_precise, Int, 0)
    .ATTR(sparse_mode, Int, 0)
    .ATTR(pse_type, Int, 1)
    .ATTR(seed, Int, 0)
    .ATTR(offset, Int, 0)
    .ATTR(out_dtype, Int, 0)
    .ATTR(softmax_out_layout, String, "")
    .OP_END_FACTORY_REG(FlashAttentionScore)
```

## Brief

Fast and Memory-Efficient Exact Attention with IO-Awareness.

## Inputs

twelve inputs, including:
- query: A matrix Tensor. The type support float16, bf16, float32.
- key: A matrix Tensor. The type support float16, bf16, float32.
- value: A matrix Tensor. The type support float16, bf16, float32.
- real_shift: A matrix Tensor. An optional input parameter. The type support float16, bf16, float32.
- drop_mask: A matrix Tensor. An optional input parameter. The type support uint8.
- padding_mask: A matrix Tensor. An optional input parameter. The type support float16, bf16, float32.
- atten_mask: A matrix Tensor. An optional input parameter. The type support bool, uint8.
- prefix: A matrix Tensor. An optional input parameter. The type support int64.
- actual_seq_qlen: A matrix Tensor. An optional input parameter. The type support int64. If used,
layout need to be setted TND. ex. If the q seqlen is [2,2,2,2,2], this parameter need be setted [2,4,6,8,10].
- actual_seq_kvlen: A matrix Tensor. An optional input parameter. The type support int64. If used,
layout need to be setted TND. ex. If the kv seqlen is [2,2,2,2,2], this parameter need be setted [2,4,6,8,10].
- q_start_idx: A matrix Tensor. An optional input parameter. The type support int64.
- kv_start_idx: A matrix Tensor. An optional input parameter. The type support int64.
- d_scale_q: A matrix Tensor. An optional input parameter. The type support float32.
- d_scale_k: A matrix Tensor. An optional input parameter. The type support float32.
- d_scale_v: A matrix Tensor. An optional input parameter. The type support float32.
- queryRope: A matrix Tensor. An optional input parameter. The type support float16, bf16, float32.
- keyRope: A matrix Tensor. An optional input parameter. The type support float16, bf16, float32.
- sink: A matrix Tensor. An optional input parameter. The type support float32.

## Outputs

- softmax_max: A matrix Tensor. The type support float32.
- softmax_sum: A matrix Tensor. The type support float32.
- softmax_out: A matrix Tensor. The type support float16, bf16, float32.
- attention_out: A matrix Tensor. The type support float16, bf16, float32.

## Attributes

- scale_value: A float. The scale value. Default: 1.0.
- keep_prob: A float. The keep probability of dropout. Default: 1.0.
- pre_tockens: An int. Previous tokens.
- next_tockens: An int. Next tokens.
- head_num: An int. A required attribute. The number of the heads.
- input_layout: A string. A required attribute. Specifies the layout of `query`, the value must be one of ["BSH",
"SBH", "BNSD", "BSND", "TND"].
- inner_precise: An int. 0, 1, reserved value. 2, support invalid lines.
- sparse_mode: An int. 0, defaultMsk. 1, allMask. 2, leftUpCausal. 3, rightDownCausal. 4, band. 5, prefix.
6, prefixCompress. 7, rightDownCausalBand. 8, bandLeftUpCausal.
- pse_type: An int. Optional attribute. Users can pass in 1 if they do not specify it.
The supported configuration values ​​are 0, 1, 2, and 3.
- seed: An int. Optional attribute. Default: 0.
- offset: An int. Optional attribute.  Default: 0.
- out_dtype: An int. Optional attribute.  Default: 0.
- softmax_out_layout: A string. Optional attribute.  Default: "", the value must be one of ["", "same_as_input"].

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 query: bfloat16,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8
- input1 key: bfloat16,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8
- input2 value: bfloat16,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8
- input3 real_shift: bfloat16,float16,float32
- input4 drop_mask: uint8
- input5 padding_mask: bfloat16,float16,float32
- input6 atten_mask: bool,uint8
- input7 prefix: int64
- input8 actual_seq_qlen: int64
- input9 actual_seq_kvlen: int64
- input10 q_start_idx: int64
- input11 kv_start_idx: int64
- input12 d_scale_q: float32
- input13 d_scale_k: float32
- input14 d_scale_v: float32
- input15 query_rope: bfloat16,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8
- input16 key_rope: bfloat16,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8
- input17 sink: float32
- input18 p_scale: float32
- output0 softmax_max: float32
- output1 softmax_sum: float32
- output2 softmax_out: bfloat16,float16,float32
- output3 attention_out: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
