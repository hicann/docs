# MoeDistributeCombineV2

```c
REG_OP(MoeDistributeCombineV2)
    .INPUT(expand_x, TensorType({DT_BF16, DT_FLOAT16, DT_INT32}))
    .INPUT(expert_ids, TensorType({DT_INT32}))
    .INPUT(assist_info_for_combine, TensorType({DT_INT32}))
    .INPUT(ep_send_counts, TensorType({DT_INT32}))
    .INPUT(expert_scales, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(tp_send_counts, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(x_active_mask, TensorType({DT_BOOL}))
    .OPTIONAL_INPUT(activation_scale, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(weight_scale, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(group_list, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(expand_scales, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(shared_expert_x, TensorType({DT_BF16, DT_FLOAT16, DT_INT32}))
    .OPTIONAL_INPUT(elastic_info, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(ori_x, TensorType({DT_BF16, DT_FLOAT16, DT_INT32}))
    .OPTIONAL_INPUT(const_expert_alpha_1, TensorType({DT_BF16, DT_FLOAT16, DT_INT32}))
    .OPTIONAL_INPUT(const_expert_alpha_2, TensorType({DT_BF16, DT_FLOAT16, DT_INT32}))
    .OPTIONAL_INPUT(const_expert_v, TensorType({DT_BF16, DT_FLOAT16, DT_INT32}))
    .OPTIONAL_INPUT(performance_info, TensorType({DT_INT64}))
    .OUTPUT(x, TensorType({DT_BF16, DT_FLOAT16}))
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
    .ATTR(global_bs, Int, 0)
    .ATTR(out_dtype, Int, 0)
    .ATTR(comm_quant_mode, Int, 0)
    .ATTR(group_list_type, Int, 0)
    .ATTR(comm_alg, String, "")
    .ATTR(zero_expert_num, Int, 0)
    .ATTR(copy_expert_num, Int, 0)
    .ATTR(const_expert_num, Int, 0)
    .OP_END_FACTORY_REG(MoeDistributeCombineV2)
```

## Brief

MoeDistributeCombineV2 operator interface implementation.

## Inputs

Ten inputs, including:
- expand_x: A tensor. Support dtype: float16, bfloat16, int32, dimension must be 2, Support Shape: (A * world_size, H), support format: ND.
- expert_ids: A tensor. Support dtype: int32, dimension must be 2, Support Shape: (BS, K), support format: ND.
- assist_info_for_combine: A tensor. Support dtype: int32, dimension must be 1, Support Shape: (A * 128), support format: ND.
- ep_send_counts: A tensor. Support dtype: int32, Support Shape: (expert_nums + 2 * globalBs * K * server_num, ), support format: ND.
- expert_scales: A tensor. Support dtype: float32, Support Shape: (BS, K), support format: ND.
- tp_send_counts: A tensor. Support dtype: int32, support format: ND.
- x_active_mask: An optional tensor. Support dtype: bool, support format: ND.
- activation_scale: An optional tensor. Support dtype: float32, support format: ND.
- weight_scale: An optional tensor. Support dtype: float32, support format: ND.
- group_list: An optional tensor. Support dtype: int64, support format: ND.
- expand_scales: A tensor. Support dtype: float32, Support Shape: (A, ), support format: ND.
- shared_expert_x: A tensor. Support dtype: float16, bfloat16, int32, support format: ND.
- performance_info: A tensor. Support dtype: int64, support format: ND.

## Outputs

One outputs, including:
- x: A tensor. Result of combine. Support dtype: float16,bfloat16,  Support Shape: (BS, H), support format: ND.

## Attributes

- group_ep: Input ep comm group name, ep means experts parallelism, dtype: String.
- ep_world_size: Input ep comm world size, dtype: Int64.
- ep_rank_id: Input ep comm rank Id, dtype: Int64.
- moe_expert_num: Input moe expert num, dtype: Int64.
- group_tp: Input tp comm group name, tp means tensor parallelism, dtype: String.
- tp_world_size: Input tp comm world size, dtype: Int64.
- tp_rank_id: Input tp comm rank Id, dtype: Int64.
- expert_shard_type: Input moe shard type, dtype: Int64.
- shared_expert_num: Input shared expert num, dtype: Int64.
- shared_expert_rank_num: Input shared expert rank num, dtype: Int64.
- global_bs: Input global batch size, dtype: Int64.
- out_dtype: Dtype of output, 0 for bfloat16, 1 for float16, dtype: Int64.
- comm_quant_mode: communication quantization mode, 1 for enable, 0 for disable, dtype: Int64.
- group_list_type: type of input group_list, dtype: Int64.
- comm_alg: Input comm alg type, dtype: String.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 expand_x: bfloat16,float16,int32
- input1 expert_ids: int32
- input2 assist_info_for_combine: int32
- input3 ep_send_counts: int32
- input4 expert_scales: float32
- input5 tp_send_counts: int32
- input6 x_active_mask: bool
- input7 activation_scale: float32
- input8 weight_scale: float32
- input9 group_list: int64
- input10 expand_scales: float32
- input11 shared_expert_x: bfloat16,float16,int32
- input12 elastic_info: int32
- input13 ori_x: bfloat16,float16,int32
- input14 const_expert_alpha_1: bfloat16,float16,int32
- input15 const_expert_alpha_2: bfloat16,float16,int32
- input16 const_expert_v: bfloat16,float16,int32
- input17 performance_info: int64
- output0 x: bfloat16,float16


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
