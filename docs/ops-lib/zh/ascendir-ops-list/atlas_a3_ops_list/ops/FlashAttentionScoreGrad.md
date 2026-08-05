# FlashAttentionScoreGrad

```c
REG_OP(FlashAttentionScoreGrad)
    .INPUT(query, TensorType({DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .INPUT(key, TensorType({DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .INPUT(value, TensorType({DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .INPUT(dy, TensorType({DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OPTIONAL_INPUT(pse_shift, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OPTIONAL_INPUT(drop_mask, TensorType({DT_UINT8}))
    .OPTIONAL_INPUT(padding_mask, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OPTIONAL_INPUT(atten_mask, TensorType({DT_BOOL, DT_UINT8}))
    .OPTIONAL_INPUT(softmax_max, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(softmax_sum, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(softmax_in, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OPTIONAL_INPUT(attention_in, TensorType({DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OPTIONAL_INPUT(prefix, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(actual_seq_qlen, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(actual_seq_kvlen, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(q_start_idx, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(kv_start_idx, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(d_scale_q, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(d_scale_k, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(d_scale_v, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(d_scale_dy, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(d_scale_o, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(query_rope, TensorType({DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OPTIONAL_INPUT(key_rope, TensorType({DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OPTIONAL_INPUT(sink, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(ds_scale, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(p_scale, TensorType({DT_FLOAT32}))
    .OUTPUT(dq, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OUTPUT(dk, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OUTPUT(dv, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OUTPUT(dpse, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OUTPUT(dq_rope, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OUTPUT(dk_rope, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OUTPUT(dsink, TensorType({DT_FLOAT32}))
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
    .ATTR(softmax_in_layout, String, "")
    .OP_END_FACTORY_REG(FlashAttentionScoreGrad)
```

## Brief

Backwards calculation of FlashAttentionScore.

## Inputs

Seventeen inputs, including:
- query: A matrix Tensor. The type support float16, bf16, float32.
- key: A matrix Tensor. The type support float16, bf16, float32.
- value: A matrix Tensor. The type support float16, bf16, float32.
- dy: A matrix Tensor. The type support float16, bf16, float32.
- pse_shift: A scalar. An optional input parameter. The type support float16, bf16, float32.
- drop_mask: A matrix Tensor. An optional input parameter. The type support uint8.
- padding_mask: A matrix Tensor. An optional input parameter. The type support float16, bf16, float32.
- atten_mask: A matrix Tensor. An optional input parameter. The type support uint8, bool.
- softmax_max: A matrix Tensor. An optional input parameter. The type support float32.
- softmax_sum: A matrix Tensor. An optional input parameter. The type support float32.
- softmax_in: A matrix Tensor. An optional input parameter. The type support float16, bf16, float32.
- attention_in: A matrix Tensor. An optional input parameter. The type support float16, bf16, float32.
- prefix: A matrix Tensor. An optional input parameter. The type support int64.
- actual_seq_qlen: A matrix Tensor. An optional input parameter. The type support int64.
If used, layout need to be setted TND. ex. If the q seqlen is [2,2,2,2,2], this parameter need be setted [2,4,6,8,10].
- actual_seq_kvlen: A matrix Tensor. An optional input parameter. The type support int64. If used,
layout need to be setted TND. ex. If the kv seqlen is [2,2,2,2,2], this parameter need be setted [2,4,6,8,10].
- q_start_idx: A matrix Tensor. An optional input parameter. The type support int64.
- kv_start_idx: A matrix Tensor. An optional input parameter. The type support int64.
- d_scale_q: A matrix Tensor. An optional input parameter. The type support float32.
- d_scale_k: A matrix Tensor. An optional input parameter. The type support float32.
- d_scale_v: A matrix Tensor. An optional input parameter. The type support float32.
- d_scale_dy: A matrix Tensor. An optional input parameter. The type support float32.
- d_scale_o: A matrix Tensor. An optional input parameter. The type support float32.
- query_rope: A matrix Tensor. An optional input parameter. The type support float16, bf16, float32.
- key_rope: A matrix Tensor. An optional input parameter. The type support float16, bf16, float32.
- sink: A matrix Tensor. An optional input parameter. The type support float32.

## Outputs

- dq: A matrix Tensor. The type support float16, bf16, float32.
- dk: A matrix Tensor. The type support float16, bf16, float32.
- dv: A matrix Tensor. The type support float16, bf16, float32.
- dpse: A matrix Tensor. The type support float16, bf16, float32.
- dqRope: A matrix Tensor. The type support float16, bf16, float32.
- dkRope: A matrix Tensor. The type support float16, bf16, float32.
- dsink: A matrix Tensor. The type support float32.

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
- softmax_in_layout: A string. Optional attribute.  Default: "", the value must be one of ["", "same_as_input"].

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 query: bfloat16,float16,float32
- input1 key: bfloat16,float16,float32
- input2 value: bfloat16,float16,float32
- input3 dy: bfloat16,float16,float32
- input4 pse_shift: bfloat16,float16,float32
- input5 drop_mask: uint8
- input6 padding_mask: bfloat16,float16,float32
- input7 atten_mask: bool,uint8
- input8 softmax_max: float32
- input9 softmax_sum: float32
- input10 softmax_in: bfloat16,float16,float32
- input11 attention_in: bfloat16,float16,float32
- input12 prefix: int64
- input13 actual_seq_qlen: int64
- input14 actual_seq_kvlen: int64
- input15 q_start_idx: int64
- input16 kv_start_idx: int64
- input17 d_scale_q: float32
- input18 d_scale_k: float32
- input19 d_scale_v: float32
- input20 d_scale_dy: float32
- input21 d_scale_o: float32
- input22 query_rope: bfloat16,float16,float32
- input23 key_rope: bfloat16,float16,float32
- input24 sink: float32
- input25 ds_scale: float32
- input26 p_scale: float32
- output0 dq: bfloat16,float16,float32
- output1 dk: bfloat16,float16,float32
- output2 dv: bfloat16,float16,float32
- output3 dpse: bfloat16,float16,float32
- output4 dq_rope: bfloat16,float16,float32
- output5 dk_rope: bfloat16,float16,float32
- output6 dsink: float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
