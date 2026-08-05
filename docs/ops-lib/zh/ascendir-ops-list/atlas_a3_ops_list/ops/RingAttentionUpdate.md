# RingAttentionUpdate

```c
REG_OP(RingAttentionUpdate)
    .INPUT(prev_attn_out, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .INPUT(prev_softmax_max, TensorType({DT_FLOAT32}))
    .INPUT(prev_softmax_sum, TensorType({DT_FLOAT32}))
    .INPUT(cur_attn_out, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .INPUT(cur_softmax_max, TensorType({DT_FLOAT32}))
    .INPUT(cur_softmax_sum, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(actual_seq_qlen, TensorType({DT_INT64}))
    .OUTPUT(attn_out, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT32}))
    .OUTPUT(softmax_max, TensorType({DT_FLOAT32}))
    .OUTPUT(softmax_sum, TensorType({DT_FLOAT32}))
    .ATTR(input_layout, String, "SBH")
    .OP_END_FACTORY_REG(RingAttentionUpdate)
```

## Brief

Update multi output of RingAttention.

## Inputs

seven inputs, including:
- prev_attn_out: A matrix Tensor. The type support float16, bf16, float32.
- prev_softmax_max: A matrix Tensor. The type support float32.
- prev_softmax_sum: A matrix Tensor. The type support float32.
- cur_attn_out: A matrix Tensor. An optional input parameter. The type support float16, bf16, float32.
- cur_softmax_max: A matrix Tensor. An optional input parameter. The type support float32.
- cur_softmax_sum: A matrix Tensor. An optional input parameter. The type support float32.
- actual_seq_qlen: A matrix Tensor. An optional input parameter. The type support int64. If used,
layout need to be setted TND. ex. If the attn_out seqlen is [2,2,2,2,2], this parameter need be setted [2,4,6,8,10].

## Outputs

- attn_out: A matrix Tensor. The type support float16, bf16, float32.
- softmax_max: A matrix Tensor. The type support float32.
- softmax_sum: A matrix Tensor. The type support float32.

## Attributes

- input_layout: A string. A optional attribute. Specifies the layout of `attn_out`,
the value must be one of ["SBH"]. Default: "SBH".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 prev_attn_out: bfloat16,float16,float32
- input1 prev_softmax_max: float32
- input2 prev_softmax_sum: float32
- input3 cur_attn_out: bfloat16,float16,float32
- input4 cur_softmax_max: float32
- input5 cur_softmax_sum: float32
- input6 actual_seq_qlen: int64
- output0 attn_out: bfloat16,float16,float32
- output1 softmax_max: float32
- output2 softmax_sum: float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
