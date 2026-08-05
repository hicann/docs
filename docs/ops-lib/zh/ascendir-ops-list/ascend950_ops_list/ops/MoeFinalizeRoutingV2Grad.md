# MoeFinalizeRoutingV2Grad

```c
REG_OP(MoeFinalizeRoutingV2Grad)
    .INPUT(grad_y, "T1")
    .INPUT(expanded_row_idx, "T2")
    .OPTIONAL_INPUT(expanded_x, "T1")
    .OPTIONAL_INPUT(scales, "T1")
    .OPTIONAL_INPUT(expert_idx, "T2")
    .OPTIONAL_INPUT(bias, "T1")
    .OUTPUT(grad_expanded_x, "T1")
    .OUTPUT(grad_scales, "T1")
    .DATATYPE(T1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .DATATYPE(T2, TensorType({DT_INT32}))
    .ATTR(drop_pad_mode, Int, 0)
    .ATTR(active_num, Int, 0)
    .ATTR(expert_num, Int, 0)
    .ATTR(expert_capacity, Int, 0)
    .OP_END_FACTORY_REG(MoeFinalizeRoutingV2Grad)
```

## Brief

Backwards calculation of MoeFinalizeRoutingV2.

## Inputs

- grad_y: A 2D Tensor, represents the gradient of output of MoeFinalizeRoutingV2. Type is BFloat16, Float16 or
Float32. Shape supports (R, H). Format supports ND.
- expanded_row_idx: A 1D Tensor, represents the token indexes of expanded_x. Type is Int32. Shape supports (R * K),
when scales is not passed in, K must be 1. If drop_pad_mode is 0, the value range is [0, R * K - 1], and there are
no duplicate indexes. When drop_pad_mode is 1, the value range is [-1, expert_num * expert_capacity - 1], and
duplicate indexes are not allowed except -1. Format supports ND.
- expanded_x: An optional 2D or 3D Tensor, represents the token sequences. Type should be the same as the type of
grad_y. When scales is passed in, it should be passed in. When drop_pad_mode is 0, it should be a 2D Tensor, and
when active_num is between (0, R * K), the shape is (active_num, H), otherwise the shape is (R * K, H). When
drop_pad_mode is 1, it should be a 3D Tensor, the shape is (expert_num, expert_capacity, H). Format supports ND.
- scales: An optional 2D Tensor, represents the scale of expanded_x. Type should be the same as the type of grad_y
except in Ascend 950 AI Processor. Shape supports (R, K). Format supports ND.
- expert_idx: An optional 2D Tensor, represents the indexes of bias. Type should be the same as the type of
expanded_row_idx. When bias is passed in, it should be passed in. Shape supports (R, K). the value range is
[0, E - 1], E >= 1, and duplicate indexes are allowed. Format supports ND.
- bias: An optional 2D Tensor, represents the bias of expanded_x. Type should be the same as the type of grad_y.
Shape supports (E, H). Format supports ND.

## Outputs

- grad_expanded_x: A 2D or 3D Tensor, represents the gradient of expanded_x. Type should be the same as the type of
grad_y. When drop_pad_mode is 0, it should be a 2D Tensor, when active_num is between (0, R * K), the shape is
(active_num, H), otherwise the shape is (R * K, H). When drop_pad_mode is 1, it should be a 3D Tensor, the shape is
(expert_num, expert_capacity, H). Format supports ND.
- grad_scales: A 2D Tensor, represents the gradient of scales. Type should be the same as the type of grad_y except
in Ascend 950 AI Processor. Shape supports (R, K). This output only makes sense when scales is passed in.
Format supports ND.

## Attributes

- drop_pad_mode: An optional integer, represents the dropless or drop/pad mode. Type is Int32. Default: 0. Value
supports 0 or 1.
- active_num: An optional integer, represents the active tokens of expanded_x. Type is Int32. Default: 0. When
drop_pad_mode is 0, it takes effect only when it is between (0, R * K). When drop_pad_mode is 1, it does not take
effect.
- expert_num: An optional integer, represents the number of expert. Type is Int32. Default: 0. When drop_pad_mode
is 0, it does not take effect. When drop_pad_mode is 1, it should be equal to E when bias is passed in, otherwise
it should be greater than 0.
- expert_capacity: An optional integer, represents the capacity of expert. Type is Int32. Default: 0. When
drop_pad_mode is 0, it does not take effect. When drop_pad_mode is 1, it should be greater than 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad_y: bfloat16,float16,float32
- input1 expanded_row_idx: int32
- input2 expanded_x: bfloat16,float16,float32
- input3 scales: bfloat16,float16,float32
- input4 expert_idx: int32
- input5 bias: bfloat16,float16,float32
- output0 grad_expanded_x: bfloat16,float16,float32
- output1 grad_scales: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
