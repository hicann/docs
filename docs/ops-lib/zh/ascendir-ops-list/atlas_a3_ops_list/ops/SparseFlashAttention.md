# SparseFlashAttention

```c
REG_OP(SparseFlashAttention)
    .INPUT(query, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(key, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(value, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(sparse_indices, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(block_table, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(actual_seq_lengths_query, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(actual_seq_lengths_kv, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(query_rope, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(key_rope, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(sinks, TensorType({DT_FP32}))
    .OUTPUT(attention_out, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(softmax_max, TensorType({DT_FP32}))
    .OUTPUT(softmax_sum, TensorType({DT_FP32}))
    .REQUIRED_ATTR(scale_value, Float)
    .ATTR(sparse_block_size, Int, 1)
    .ATTR(layout_query, String, "BSND")
    .ATTR(layout_kv, String, "BSND")
    .ATTR(sparse_mode, Int, 3)
    .ATTR(pre_tokens, Int, 9223372036854775807)
    .ATTR(next_tokens, Int, 9223372036854775807)
    .ATTR(attention_mode, Int, 0)
    .ATTR(return_softmax_lse, Bool, false)
    .OP_END_FACTORY_REG(SparseFlashAttention)
```

## Brief

Function SparseFlashAttention.

## Inputs

- query: A matrix tensor. The type support float16, bfloat16.
Query for attention structure.
- key: A matrix tensor. The type support float16, bfloat16.
Key for attention structure.
- value: A matrix tensor. The type support float16, bfloat16.
Value for attention structure.
- sparse_indices: A matrix tensor. The type support int32.
The indices of sparse kv cache.
- block_table: A matrix tensor. The type support int32.
The block mapping table used in KV storage of PageAttention.
- actual_seq_lengths_query: A matrix tensor. The type support int32.
Efective sequence length of query in different batches.
- actual_seq_lengths_kv: A matrix tensor. The type support int32.
Effective sequence length of key and value in different batches.
- query_rope: A tensor. The type support float16, bfloat16.
- key_rope: A tensor. The type support float16, bfloat16.
- sinks: A tensor. The type support float.

## Outputs

- attention_out: A matrix tensor. The type support float16, bfloat16.
- softmax_max: A matrix tensor. The type support float32.
- softmax_sum: A matrix tensor. The type support float32.

## Attributes

- scale_value: A float. A required attribute.
- sparse_block_size: An int. An optional attribute. Max value: 64. Default: 1.
- layout_query: A string. An optional attribute. Specifies the layout of `query`, the value must be one of ["BSND", "TND"]. Default: "BSND".
- layout_kv: A string. An optional attribute. Specifies the layout of `key` and 'value', the value must be one of ["BSND", "TND", "PA_BSND"]. Default: "BSND".
- sparse_mode: An int. Sparse mode. Default: 3.
- 0: default mask
- 3: rightDownCausal make
- 4: band mask
- pre_tokens: An int. Previous tokens. Default: 9223372036854775807.
- next_tokens: An int. Next tokens. Default: 9223372036854775807.
- attention_mode: An int. An optional attribute. Default: 0.
- return_softmax_lse: A bool. An optional attribute. Default: false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 query: bfloat16,float16
- input1 key: bfloat16,float16
- input2 value: bfloat16,float16
- input3 sparse_indices: int32
- input4 block_table: int32
- input5 actual_seq_lengths_query: int32
- input6 actual_seq_lengths_kv: int32
- input7 query_rope: bfloat16,float16
- input8 key_rope: bfloat16,float16
- input9 sinks: float32
- output0 attention_out: bfloat16,float16
- output1 softmax_max: float32
- output2 softmax_sum: float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
