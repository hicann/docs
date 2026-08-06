# AdvanceStep

```c
REG_OP(AdvanceStep)
    .INPUT(input_tokens, TensorType({DT_INT64}))
    .INPUT(sampled_token_ids, TensorType({DT_INT64}))
    .INPUT(input_positions, TensorType({DT_INT64}))
    .INPUT(seq_lens, TensorType({DT_INT64}))
    .INPUT(slot_mapping, TensorType({DT_INT64}))
    .INPUT(block_tables, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(spec_token, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(accepted_num, TensorType({DT_INT64}))
    .OUTPUT(input_tokens, TensorType({DT_INT64}))
    .OUTPUT(input_positions, TensorType({DT_INT64}))
    .OUTPUT(seq_lens, TensorType({DT_INT64}))
    .OUTPUT(slot_mapping, TensorType({DT_INT64}))
    .REQUIRED_ATTR(num_seqs, Int)
    .REQUIRED_ATTR(num_queries, Int)
    .REQUIRED_ATTR(block_size, Int)
    .OP_END_FACTORY_REG(AdvanceStep)
```

## Brief

The main function of the advcance_step operator is to advance the inference step in vLLM, that is,
update the model status and generate new inputTokens, inputPostions, seqLen, and slotMapping in each generation step.
Improves the efficiency of vLLM inference. 

## Inputs

Six inputs, including:
- input_tokens: A 1-D input tensor. When spec_token and accepted_num are None, length equal to num_seqs. When
spec_token and accepted_num are NOT None, length equal to num_seqs * (spec_num + 1). Must be int64 type. Must be int64
type. Format is ND.
- sampled_token_ids: A 2-D input tensor. When spec_token and accepted_num are None, the first dim equal to
num_queries and the second dim equal to one. When spec_token and accepted_num are NOT None, the first dim equal to
num_seqs and the second dim equal to spec_num+1. Must be int64 type.
Must be int64 type. Format is ND.
- input_positions: A 1-D input tensor. When spec_token and accepted_num are None, length equal to num_seqs. When
spec_token and accepted_num are NOT None, length equal to num_seqs * (spec_num + 1). Must be int64 type. Format is ND.
- seq_lens: A 1-D input tensor. When spec_token and accepted_num are None, length equal to num_seqs. When spec_token
and accepted_num are NOT None, length equal to num_seqs * (spec_num + 1). Must be int64 type. Must be int64 type. Format
is ND.
- slot_mapping: A 1-D input tensor. When spec_token and accepted_num are None, length equal to num_seqs. When
spec_token and accepted_num are NOT None, length equal to num_seqs * (spec_num + 1). Must be int64 type. Must be int64
type. Format is ND.
- block_tables: When spec_token and accepted_num are None, A 1-D input tensor, and length equal to num_seqs. When
spec_token and accepted_num are NOT None, A 2-D input tensor, the first dim equal to num_seqs and the second dim equal
to spec_num+1. Must be int64 type. Format is ND.
- spec_token: A 2-D optional input tensor, which the first dim equal to num_seqs and the second dim equal to
spec_num. Must be int64 type. Format is ND.
- accepted_num: A 1-D optional input tensor, and length equal to num_seqs. Must be int64 type. Format is ND.

## Outputs

- input_tokens: A 1-D output tensor. The input tensor input_tokens will self-updating and save as itself.
Must be int64 type. Format is ND.
- input_positions: A 1-D output tensor. The input tensor input_positions will self-updating and save as itself.
Must be int64 type. Format is ND.
- seq_lens: A 1-D output tensor. The input tensor seq_lens will self-updating and save as itself.
Must be int64 type. Format is ND.
- slot_mapping: A 1-D output tensor. The input tensor slot_mapping will self-updating and save as itself.
Must be int64 type. Format is ND. 

## Attributes

- num_seqs: A required Int, which equal to the length of input_tokens, input_positions, seq_lens,
slot_mapping and block_tables. The value of it must bigger than 0.
- num_queries: A required Int, which equal to the length of sampled_token_ids's first dim.
The value of it must bigger than 0.
- block_size: A required Int, which means the basic block length of each block. The value of it must bigger than 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_tokens: int64
- input1 sampled_token_ids: int64
- input2 input_positions: int64
- input3 seq_lens: int64
- input4 slot_mapping: int64
- input5 block_tables: int64
- input6 spec_token: int64
- input7 accepted_num: int64


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
