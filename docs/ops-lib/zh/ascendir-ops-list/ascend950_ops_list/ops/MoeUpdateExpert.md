# MoeUpdateExpert

```c
REG_OP(MoeUpdateExpert)
      .INPUT(expert_ids, TensorType({DT_INT32, DT_INT64}))
      .INPUT(eplb_table, TensorType({DT_INT32}))
      .OPTIONAL_INPUT(expert_scales, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
      .OPTIONAL_INPUT(pruning_threshold, TensorType({DT_FLOAT}))
      .OPTIONAL_INPUT(active_mask, TensorType({DT_BOOL}))
      .OUTPUT(balanced_expert_ids, TensorType({DT_INT32, DT_INT64}))
      .OUTPUT(balanced_active_mask, TensorType({DT_BOOL}))
      .ATTR(local_rank_id, Int, -1)
      .ATTR(world_size, Int, -1)
      .ATTR(balance_mode, Int, 0)
      .OP_END_FACTORY_REG(MoeUpdateExpert)
```

## Brief

MoeUpdateExpert operator interface implementation.

## Inputs

- expert_ids: A tensor. The topK expert index for each token. Support dtype: int32, int64. dimension must be 2, support format: ND.
- eplb_table: A tensor. Mapping table of logical rank_id to physical rank_id. Support dtype: int32. dimension must be 2, support format: ND.
- expert_scales: A tensor. Scales for top k experts for each token. Support dtype: float16, bfloat16, float32. dimension must be 2, support format: ND.
- pruning_threshold: A tensor. Threshold for expert scales. Support dtype: float32. dimension must be 1 or 2, support format: ND.
- active_mask: A tensor. Indicates if token is involved in communication. Support dtype: bool. dimension must be 1, support format: ND.

## Attributes

- local_rank_id: Required. The rank id in the current communication domain. dtype: Int64.
- world_size: Required. The num of physical rank in the current communication domain. dtype: Int64.
- balance_mode: Optional. Balanced by rank(0) or by token(1), and the current default value is 0. dtype: Int64

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 expert_ids: int32,int64
- input1 eplb_table: int32
- input2 expert_scales: bfloat16,float16,float32
- input3 pruning_threshold: float32
- input4 active_mask: bool
- output0 balanced_expert_ids: int32,int64
- output1 balanced_active_mask: bool

## Output

balance_expert_ids: A tensor. Convert the logical rank_id in expert_ids to physical rank_id using the eplb_table. Support dtype: int32, int64. Support format: ND.
balanced_active_mask: A tensor. Get balanced active mask through tailored expert scales and pruning threshold. Support dtype: bool. Support format: ND.


---

[Back to Operator Specifications (Ascend950)](../README.md)
