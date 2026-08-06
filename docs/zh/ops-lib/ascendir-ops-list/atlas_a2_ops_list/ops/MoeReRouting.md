# MoeReRouting

```c
REG_OP(MoeReRouting)
    .INPUT(tokens, TensorType({DT_FLOAT16, DT_BF16, DT_INT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .INPUT(expert_token_num_per_rank, TensorType({DT_INT32, DT_INT64}))
    .OPTIONAL_INPUT(per_token_scales, TensorType({DT_FLOAT, DT_FLOAT8_E8M0}))
    .OUTPUT(permute_tokens, TensorType({DT_FLOAT16, DT_BF16, DT_INT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .OUTPUT(permute_per_token_scales, TensorType({DT_FLOAT, DT_FLOAT8_E8M0}))
    .OUTPUT(permute_token_idx, TensorType({DT_INT32}))
    .OUTPUT(expert_token_num, TensorType({DT_INT32, DT_INT64}))
    .ATTR(expert_token_num_type, Int, 1)
    .ATTR(idx_type, Int, 0)
    .OP_END_FACTORY_REG(MoeReRouting)
```

## Brief

Rearrange tokens from rank order to expert order

## Inputs

- tokens: A 2D tensor, represents tokens in rank-order. Type is BFloat16, Float16, DT_FLOAT8_E5M2,
DT_FLOAT8_E4M3FN or Int8. Shape supports (A, H). Format supports ND.
Notices: The value of H must be greater than 0 and less than 16384.(0 < H <16384)
- expert_token_num_per_rank: A 2D tensor, represents numbers of tokens belong to an expert on specific rank.
Type is Int32 or Int64. Shape supports (N, E). Format supports ND.
- per_token_scales: A 1D or 2D tensor, optional, represents tokens scale in rank-order. Type is Float32, DT_FLOAT8_E8M0.
Shape supports (A) or (A,S). Format supports ND. If tokens is FLOAT8, per_token_scales must be DT_FLOAT8_E8M0. 
The Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component support 1D. 
The Atlas A3 Training Series Product/Atlas A3 Inference Series Product support 1D. 
Ascend 950 support 1D or 2D. 

## Outputs

- permute_tokens: A 2D tensor, represents tokens in expert-order. Type is BFloat16, Float16 or
Int8. Shape supports (A, H). Format supports ND.
- permute_per_token_scales: A 1D or 2D tensor, represents tokens scale in expert-order. Type is Float32, DT_FLOAT8_E8M0.
Shape supports (A) or (A,S). Format supports ND.
The Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component support 1D. 
The Atlas A3 Training Series Product/Atlas A3 Inference Series Product support 1D. 
Ascend 950 support 1D or 2D. 
- permute_token_idx: A 1D tensor, represents token idx in rank-order. Type is Int32.
Shape supports (A). Format supports ND.
- expert_token_num: A 1D tensor, represents tokens nums of experts. Type is Int32 or Int64.
Shape supports (E). Format supports ND.

## Attributes

- expert_token_num_type: Optional integer, represents the cumsum or count mode. Type is Int. Default: 1. Value
supports 0-cumsum or 1-count.
- idx_type: Optional integer, represents the gather or scatter index. Type is Int. Default: 0. Value
supports 0-gather idx or 1-scatter idx.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 tokens: bfloat16,float16,int8
- input1 expert_token_num_per_rank: int32,int64
- input2 per_token_scales: float32
- output0 permute_tokens: bfloat16,float16,int8
- output1 permute_per_token_scales: float32
- output2 permute_token_idx: int32
- output3 expert_token_num: int32,int64


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
