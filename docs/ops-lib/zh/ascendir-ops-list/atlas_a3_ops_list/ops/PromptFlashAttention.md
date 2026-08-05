# PromptFlashAttention

```c
REG_OP(PromptFlashAttention)
    .INPUT(query, TensorType({DT_FLOAT16, DT_BF16, DT_INT8}))
    .INPUT(key, TensorType({DT_FLOAT16, DT_BF16, DT_INT8}))
    .INPUT(value, TensorType({DT_FLOAT16, DT_BF16, DT_INT8}))
    .OPTIONAL_INPUT(pse_shift, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(atten_mask, TensorType({DT_FLOAT16, DT_BOOL, DT_INT8, DT_UINT8}))
    .OPTIONAL_INPUT(actual_seq_lengths, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(actual_seq_lengths_kv, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(deq_scale1, TensorType({DT_UINT64, DT_FLOAT32}))
    .OPTIONAL_INPUT(quant_scale1, TensorType({DT_FLOAT32}))
    .OPTIONAL_INPUT(deq_scale2, TensorType({DT_UINT64, DT_FLOAT32}))
    .OPTIONAL_INPUT(quant_scale2, TensorType({DT_FLOAT32, DT_BF16}))
    .OPTIONAL_INPUT(quant_offset2, TensorType({DT_FLOAT32, DT_BF16}))
    .OUTPUT(attention_out, TensorType({DT_FLOAT16, DT_BF16, DT_INT8}))
    .REQUIRED_ATTR(num_heads, Int)
    .ATTR(scale_value, Float, 1.0)
    .ATTR(pre_tokens, Int, 214748647)
    .ATTR(next_tokens, Int, 0)
    .ATTR(input_layout, String, "BSH")
    .ATTR(num_key_value_heads, Int, 0)
    .ATTR(sparse_mode, Int, 0)
    .ATTR(inner_precise, Int, 1)
    .OP_END_FACTORY_REG(PromptFlashAttention)
```

## Brief

Function PromptFlashAttention.

## Inputs

- query: A matrix Tensor. The type support float16, bf16, int8.
- key: A matrix Tensor. The type support float16, bf16, int8.
- value: A matrix Tensor. The type support float16, bf16, int8.
- pse_shift: A matrix Tensor. The type support float16, bf16.
- atten_mask: A matrix Tensor. The type support float16, bool, int8, uint8.
- actual_seq_lengths: A Tensor. The type support int64.
- actual_seq_lengths_kv: A Tensor. The type support int64.
- deq_scale1: A Tensor. The type support uint64, float32.
- quant_scale1: A Tensor. The type support float32.
- deq_scale2: A Tensor. The type support uint64, float32.
- quant_scale2: A Tensor. The type support float32, bf16.
- quant_offset2: A Tensor. The type support float32, bf16.

## Outputs

- attention_out: A matrix Tensor. The type support float16, bf16, int8.

## Attributes

- num_heads: An int. The number of the heads.
- scale_value: A float. The scale value. Default: 1.0.
- pre_tokens: An int. Previous tokens. Default: 214748647.
- next_tokens: An int. Next tokens. Default: 0.
- input_layout: A string. Specifies the layout of `query`, the value must be one of ["BSH", "BNSD", "BSND", "BNSD_BSND"]. Default: "BSH".
- num_key_value_heads: Key value num heads. Default: 0.
- sparse_mode: Sparse mode. Default: 0.
- inner_precise: An int. 0, float16 high precision. 1, high performance. Default: 1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 query: bfloat16,float16,int8
- input1 key: bfloat16,float16,int8
- input2 value: bfloat16,float16,int8
- input3 pse_shift: bfloat16,float16
- input4 atten_mask: bool,float16,int8,uint8
- input5 actual_seq_lengths: int64
- input6 actual_seq_lengths_kv: int64
- input7 deq_scale1: float32,uint64
- input8 quant_scale1: float32
- input9 deq_scale2: float32,uint64
- input10 quant_scale2: bfloat16,float32
- input11 quant_offset2: bfloat16,float32
- output0 attention_out: bfloat16,float16,int8

## Attention Constraints

- Ensure CANN and PyTorch package version compatibility when using this interface with PyTorch.
- Handle empty input: If 'query' is empty, return directly. If 'query' is non-empty and 'key', 'value' are empty tensors (S2=0), fill 'attention_out' with zeros of the corresponding shape.
If 'attention_out' is an empty tensor, AscendCLNN will process it.
- The 'sparseMode' parameter currently only supports values 0, 1, 2, 3, and 4; other values will cause an error.
- Output is INT8. 'quantOffset2' must be a non-empty pointer and tensor. 'sparseMode', 'preTokens', and 'nextTokens' must meet certain conditions.
If some rows of the matrix do not participate in calculations, resulting in computational errors, this scenario will be blocked
(solution: if you want this scenario not to be blocked, post-quantization operations should be performed outside the PFA interface, not enabled within).
For `sparseMode = 0`, if `attenMask` is a non-empty pointer, the condition for interception is `actualSeqLengths - actualSeqLengthsKV - preTokens > 0` or `nextTokens < 0` per batch.
For `sparseMode = 1` or `2`, no interception conditions are met.
For `sparseMode = 3`, the condition for interception is `actualSeqLengthsKV - actualSeqLengths < 0` per batch.
For `sparseMode = 4`, the condition for interception is `preTokens < 0` or `nextTokens + actualSeqLengthsKV - actualSeqLengths < 0` per batch.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
