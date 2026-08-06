# LightningIndexer

```c
REG_OP(LightningIndexer)
    .INPUT(query, TensorType({DT_BF16, DT_FLOAT16}))
    .INPUT(key, TensorType({DT_BF16, DT_FLOAT16}))
    .INPUT(weights, TensorType({DT_BF16, DT_FLOAT16}))
    .OPTIONAL_INPUT(actual_seq_lengths_query, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(actual_seq_lengths_key, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(block_table, TensorType({DT_INT32}))
    .OUTPUT(sparse_indices, TensorType({DT_INT32}))
    .OUTPUT(sparse_values, TensorType({DT_BF16, DT_FLOAT16}))
    .ATTR(layout_query, String, "BSND")
    .ATTR(layout_key, String, "BSND")
    .ATTR(sparse_count, Int, 2048)
    .ATTR(sparse_mode, Int, 3)
    .ATTR(pre_tokens, Int, 9223372036854775807)
    .ATTR(next_tokens, Int, 9223372036854775807)
    .ATTR(return_values, Bool, false)
    .OP_END_FACTORY_REG(LightningIndexer)
```

## Brief

Function LightningIndexer.

## Inputs

- query: A matrix tensor. The type support float16, bfloat16.
Query for attention structure.
- key: A matrix tensor. The type support float16, bfloat16.
Key for attention structure.
- weights: A matrix tensor. The type support float16, bfloat16.
Weights for attention structure.
- actual_seq_lengths_query: A matrix tensor. The type support int32.
Efective sequence length of query in different batches.
- actual_seq_lengths_key: A matrix tensor. The type support int32.
Effective sequence length of key in different batches.
- block_table: A matrix tensor. The type support int32.
The block mapping table used in KV storage of PageAttention.

## Outputs

- sparse_indices: A matrix tensor. The type support int32.
The indices of sparse kv cache.
- sparse_values: A matrix tensor. The type support float16, bfloat16.
The values of sparse kv cache.

## Attributes

- layout_query: A string. Specifies the layout of `query`, the value must be one of ["BSND", "TND"]. Default: "BSND".
- layout_key: A string. Specifies the layout of `key`, the value must be one of ["BSND", "TND", "PA_BSND"]. Default: "BSND".
- sparse_count: An int. The sparse count. Default: 2048.
- sparse_mode: Sparse mode. Default: 3.
- 0: default mask
- 3: rightDownCausal make
- 4: band mask
- pre_tokens: An int. Previous tokens. Default: 9223372036854775807.
- next_tokens: An int. Next tokens. Default: 9223372036854775807.
- return_values: An bool. Need return sparse value. Default: false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 query: bfloat16,float16
- input1 key: bfloat16,float16
- input2 weights: bfloat16,float16,float32
- input3 actual_seq_lengths_query: int32
- input4 actual_seq_lengths_key: int32
- input5 block_table: int32
- output0 sparse_indices: int32
- output1 sparse_values: bfloat16,float16


---

[Back to Operator Specifications (Ascend950)](../README.md)
