# QuantLightningIndexer

```c
REG_OP(QuantLightningIndexer)
    .INPUT(query, TensorType({DT_INT8, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .INPUT(key, TensorType({DT_INT8, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .INPUT(weights, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(query_dequant_scale, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(key_dequant_scale, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(actual_seq_lengths_query, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(actual_seq_lengths_key, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(block_table, TensorType({DT_INT32}))
    .OUTPUT(sparse_indices, TensorType({DT_INT32}))
    .REQUIRED_ATTR(query_quant_mode, Int)
    .REQUIRED_ATTR(key_quant_mode, Int)
    .ATTR(layout_query, String, "BSND")
    .ATTR(layout_key, String, "BSND")
    .ATTR(sparse_count, Int, 2048)
    .ATTR(sparse_mode, Int, 3)
    .ATTR(pre_tokens, Int, 9223372036854775807)
    .ATTR(next_tokens, Int, 9223372036854775807)
    .ATTR(key_stride0, Int, -1)
    .ATTR(key_dequant_scale_stride0, Int, -1)
    .OP_END_FACTORY_REG(QuantLightningIndexer)
```

## Brief

Function QuantLightningIndexer.

## Inputs

- query: A matrix tensor. The type support int8, fp8_e4m3fn, hifloat8.
Query for attention structure.
- key: A matrix tensor. The type support int8, fp8_e4m3fn, hifloat8.
Key for attention structure.
- weights: A matrix tensor. The type support float16, bfloat16.
Weights for attention structure.
- query_dequant_scale:  A matrix tensor. The type support float16, float32.
The dequantization factor of query.
- key_dequant_scale:  A matrix tensor. The type support float16, float32.
The dequantization factor of key.
- actual_seq_lengths_query: A matrix tensor. The type support int32.
Efective sequence length of query in different batches.
- actual_seq_lengths_key: A matrix tensor. The type support int32.
Effective sequence length of key in different batches.
- block_table: A matrix tensor. The type support int32.
The block mapping table used in KV storage of PageAttention.

## Outputs

- sparse_indices: A matrix tensor. The type support int32.
The indices of sparse kv cache.

## Attributes

- query_quant_mode: An int. Antiquantization mode of query.
- 0: per-token+per-head
- key_quant_mode: An int. Antiquantization mode of key. The mode number is the same as key_quant_mode.
- layout_query: A string. Specifies the layout of `query`, the value must be one of ["BSND", "TND"]. Default: "BSND".
- layout_key: A string. Specifies the layout of `key`, the value must be one of ["BSND", "TND", "PA_BSND"]. Default: "BSND".
- sparse_count: An int. The sparse count. Default: 2048.
- sparse_mode: Sparse mode. Default: 3.
- 0: default mask
- 3: rightDownCausal make
- 4: band mask
- pre_tokens: An int. Previous tokens. Default: 9223372036854775807.
- next_tokens: An int. Next tokens. Default: 9223372036854775807.
- key_stride0: An int. Key stride 0. Default: -1.
- key_dequant_scale_stride0: An int. Key dequant scale stride 0. Default: -1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 query: int8
- input1 key: int8
- input2 weights: float16
- input3 query_dequant_scale: float16
- input4 key_dequant_scale: float16
- input5 actual_seq_lengths_query: int32
- input6 actual_seq_lengths_key: int32
- input7 block_table: int32
- output0 sparse_indices: int32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
