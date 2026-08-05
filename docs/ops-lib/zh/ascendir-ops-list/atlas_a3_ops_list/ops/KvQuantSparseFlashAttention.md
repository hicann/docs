# KvQuantSparseFlashAttention

```c
REG_OP(KvQuantSparseFlashAttention)
    .INPUT(query, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(key, TensorType({DT_INT8, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .INPUT(value, TensorType({DT_INT8, DT_FLOAT8_E4M3FN, DT_HIFLOAT8}))
    .INPUT(sparse_indices, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(key_dequant_scale, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(value_dequant_scale, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(block_table, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(actual_seq_lengths_query, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(actual_seq_lengths_kv, TensorType({DT_INT32}))
    .OUTPUT(attention_out, TensorType({DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(scale_value, Float)
    .REQUIRED_ATTR(key_quant_mode, Int)
    .REQUIRED_ATTR(value_quant_mode, Int)
    .ATTR(sparse_block_size, Int, 1)
    .ATTR(layout_query, String, "BSND")
    .ATTR(layout_kv, String, "BSND")
    .ATTR(sparse_mode, Int, 3)
    .ATTR(pre_tokens, Int, 9223372036854775807)
    .ATTR(next_tokens, Int, 9223372036854775807)
    .ATTR(attention_mode, Int, 0)
    .ATTR(quant_scale_repo_mode, Int, 1)
    .ATTR(tile_size, Int, 128)
    .ATTR(rope_head_dim, Int, 64)
    .OP_END_FACTORY_REG(KvQuantSparseFlashAttention)
```

## Brief

Function KvQuantSparseFlashAttention.

## Inputs

- query: A matrix tensor. The type support float16, bfloat16.
Query for attention structure.
- key: A matrix tensor. The type support int8, fp8_e4m3fn, hifloat8.
Key for attention structure.
- value: A matrix tensor. The type support int8, fp8_e4m3fn, hifloat8.
Value for attention structure.
- sparse_indices: A matrix tensor. The type support int32.
The indices of sparse kv cache.
- key_dequant_scale: A matrix tensor. The type support float32.
The dequantization factor of key.
- value_dequant_scale: A matrix tensor. The type support float32.
The dequantization factor of value.
- block_table: A matrix tensor. The type support int32.
The block mapping table used in KV storage of PageAttention.
- actual_seq_lengths_query: A matrix tensor. The type support int32.
Efective sequence length of query in different batches.
- actual_seq_lengths_kv: A matrix tensor. The type support int32.
Effective sequence length of key/value in different batches.

## Outputs

- attention_out: A matrix tensor. The type support float16, bfloat16.
The output of attention structure.

## Attributes

- scale_value: A float. The scale value.
- key_quant_mode: An int. Antiquantization mode of key.
- 0: per-channel
- 1: per-token+per-head
- 2: per-tile
- value_quant_mode: An int. Antiquantization mode of value. The mode number is the same as key_quant_mode.
- sparse_block_size: An int. The block size in the sparse phase. Default: 1.
- layout_query: A string. Specifies the layout of `query`, the value must be one of ["BSND", "TND"]. Default: "BSND".
- layout_kv: A string. Specifies the layout of `key/value`, the value must be one of ["BSND", "TND", "PA_BSND"]. Default: "BSND".
- sparse_mode: Sparse mode. Default: 3.
- 0: default mask
- 3: rightDownCausal make
- 4: band mask
- pre_tokens: An int. Previous tokens. Default: 9223372036854775807.
- next_tokens: An int. Next tokens. Default: 9223372036854775807.
- attention_mode: An int. Attention mode, 0: GQA/MHA; 1: MLA-naive; 2: MLA-absorb. Default: 0.
- quant_scale_repo_mode: An int. Quant scale repo mode, 0: separate; 1: combine. Default: 1.
- tile_size: An int. Tile size. Default: 128.
- rope_head_dim: An int. Rope head dim. Default: 64.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 query: bfloat16,float16
- input1 key: int8
- input2 value: int8
- input3 sparse_indices: int32
- input4 key_dequant_scale: float32
- input5 value_dequant_scale: float32
- input6 block_table: int32
- input7 actual_seq_lengths_query: int32
- input8 actual_seq_lengths_kv: int32
- output0 attention_out: bfloat16,float16


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
