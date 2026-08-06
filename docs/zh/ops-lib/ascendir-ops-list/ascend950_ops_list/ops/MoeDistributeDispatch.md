# MoeDistributeDispatch

```c
REG_OP(MoeDistributeDispatch)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16}))
    .INPUT(expert_ids, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(scales, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(x_active_mask, TensorType({DT_BOOL}))
    .OPTIONAL_INPUT(expert_scales, TensorType({DT_FLOAT}))
    .OUTPUT(expand_x, TensorType({DT_BF16, DT_INT8, DT_FLOAT16}))
    .OUTPUT(dynamic_scales, TensorType({DT_FLOAT}))
    .OUTPUT(expand_idx, TensorType({DT_INT32}))
    .OUTPUT(expert_token_nums, TensorType({DT_INT64}))
    .OUTPUT(ep_recv_count, TensorType({DT_INT32}))
    .OUTPUT(tp_recv_count, TensorType({DT_INT32}))
    .OUTPUT(expand_scales, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(group_ep, String)
    .REQUIRED_ATTR(ep_world_size, Int)
    .REQUIRED_ATTR(ep_rank_id, Int)
    .REQUIRED_ATTR(moe_expert_num, Int)
    .ATTR(group_tp, String, "")
    .ATTR(tp_world_size, Int, 0)
    .ATTR(tp_rank_id, Int, 0)
    .ATTR(expert_shard_type, Int, 0)
    .ATTR(shared_expert_num, Int, 1)
    .ATTR(shared_expert_rank_num, Int, 0)
    .ATTR(quant_mode, Int, 0)
    .ATTR(global_bs, Int, 0)
    .ATTR(expert_token_nums_type, Int, 1)
    .OP_END_FACTORY_REG(MoeDistributeDispatch)
```

## Brief

MoeDistributeDispatch operator interface implementation.

## Inputs

Five inputs, including:
- x: A tensor. Support dtype: float16,bfloat16, dimension must be 2. Shape supports (BS, H), support format: ND.
- expertIds: A tensor. Support dtype: int32, indicates top k experts of each token, dimension must be 2. Shape supports (BS, K), support format: ND.
- scales: An optional tensor. Support dtype: float32, dimension must be 2, support format: ND.
- x_active_mask: An optional tensor. Support dtype: bool, support format: ND.
- expert_scales: An optional tensor. Support dtype: float32. Shape supports (BS, K), support format: ND.

## Outputs

Seven outputs, including:
- expand_x: A tensor. Result of each expert after dispatching. Support dtype: float16,bfloat16,int8. Shape supports (A, H), support format: ND.
- dynamic_scales: If quant is enabled, scale value of each token. A tensor. Support dtype: float32. Shape supports (A, ), support format: ND.
- expand_idx: A tensor. Support dtype: int32. Shape supports (BS*K, ), support format: ND.
- expert_token_nums: A tensor. Tokens nums of expand_x. Support dtype: int64, support format: ND.
- ep_recv_count: A tensor. Received token nums after dispatching. Support dtype: int32, support format: ND.
- tp_recv_count: A tensor. Received token nums after allgather. Support dtype: int32, support format: ND.
- expand_scales: A tensor. Scales of each token to sum for combine. Support dtype: float32. Shape supports (A, ), support format: ND.

## Attributes

- group_ep: Required. Input ep comm group name, ep means experts parallelism, dtype: String.
- ep_world_size: Required. Input ep comm world size, dtype: int64.
- ep_rank_id: Required. Input ep comm rank Id, dtype: int64.
- moe_expert_num: Required. Input moe expert num, dtype: int64.
- group_tp: Input tp comm group name, tp means tensor parallelism, dtype: String.
- tp_world_size: Input tp comm world size, dtype: int64.
- tp_rank_id: Input tp comm rank Id, dtype: int64.
- expert_shard_type: Input moe shard type, dtype: int64.
- shared_expert_num: Input shared expert num, dtype: int64.
- shared_expert_rank_num: Input shared expert rank num, dtype: int64.
- quant_mode: Input quant mode. The options are 0 (non-quantization), 1 (static quantization), and 2 (dynamic quantization). dtype: int64.
- global_bs: Input global batch size, dtype: int64.
- expert_token_nums_type: Input expert token nums type, dtype: int64.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- input1 expert_ids: int32
- input2 scales: float32
- input3 x_active_mask: bool
- input4 expert_scales: float32
- output0 expand_x: bfloat16,float16,int8
- output1 dynamic_scales: float32
- output2 expand_idx: int32
- output3 expert_token_nums: int64
- output4 ep_recv_count: int32
- output5 tp_recv_count: int32
- output6 expand_scales: float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
