# IncreFlashAttention

```c
REG_OP(IncreFlashAttention)
    .INPUT(query, TensorType({DT_FLOAT16, DT_BF16, DT_INT8}))
    .DYNAMIC_INPUT(key, TensorType({DT_FLOAT16, DT_BF16, DT_INT8}))
    .DYNAMIC_INPUT(value, TensorType({DT_FLOAT16, DT_BF16, DT_INT8}))
    .OPTIONAL_INPUT(pse_shift, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(atten_mask, TensorType({DT_BOOL, DT_INT8, DT_UINT8}))
    .OPTIONAL_INPUT(actual_seq_lengths, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(dequant_scale1, TensorType({DT_UINT64, DT_FLOAT}))
    .OPTIONAL_INPUT(quant_scale1, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(dequant_scale2, TensorType({DT_UINT64, DT_FLOAT}))
    .OPTIONAL_INPUT(quant_scale2, TensorType({DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(quant_offset2, TensorType({DT_FLOAT, DT_BF16}))
    .OPTIONAL_INPUT(antiquant_scale, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(antiquant_offset, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(block_table, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(kv_padding_size, TensorType({DT_INT64}))
    .OUTPUT(attention_out, TensorType({DT_FLOAT16, DT_BF16, DT_INT8}))
    .REQUIRED_ATTR(num_heads, Int)
    .ATTR(scale_value, Float, 1.0)
    .ATTR(input_layout, String, "BSH")
    .ATTR(num_key_value_heads, Int, 1)
    .ATTR(block_size, Int, 0)
    .ATTR(inner_precise, Int, 1)
    .OP_END_FACTORY_REG(IncreFlashAttention)
```

## Brief

Implement incremental inference based on full inference.

## Inputs

- query: A matrix Tensor. The type support float16, bf16, int8.
- key: It's a dynamic input. A matrix Tensor. The type support float16, bf16, int8.
- value: It's a dynamic input. A matrix Tensor. The type support float16, bf16, int8.
- pse_shift: A matrix Tensor. Position coding inside the attention structure. The type support float16, bf16.
- atten_mask: A matrix Tensor. Mask the result of multiplying query by key to indicate whether to calculate the correlation between tokens.
The type support bool, int8, uint8.
- actual_seq_lengths: A matrix Tensor. Indicates the valid sequence length of the key/value in different batches.
The type support int64.
- dequant_scale1: A matrix Tensor. Dequantization factor after multiplying query by key.
The type support uint64, float32.
- quant_scale1: A matrix Tensor. Indicates the quantization factor before multiplying query by key.
The type support float32.
- dequant_scale2: A matrix Tensor. Dequantization factor after multiplying the result of softmax by value.
The type support uint64, float32.
- quant_scale2: A matrix Tensor. Quantization factor of the output. The type support float32, bf16.
- quant_offset2: A matrix Tensor. Indicates the quantization offset of the output. The type support float32, bf16.
- antiquant_scale: A matrix Tensor. Indicates the antiquant factor. The type support float16, bf16.
- antiquant_offset: A matrix Tensor. Indicates the antiquant offset. The type support float16, bf16.
- block_table: A matrix Tensor. Indicates the block mapping table used by KV storage in PageAttention.
The type support int32.
- kv_padding_size: A matrix Tensor. Indicates whether the data of each batch in the key/value is
right-aligned and the number of right-aligned data.The type support int64.

## Outputs

attention_out: A matrix Tensor. The type support float16, bf16, int8. 

## Attributes

- num_heads: A required int. The number of the heads.
- scale_value: An optional float. The scale value. Default: 1.0.
- input_layout: An optional string. Specifies the layout of query, the value must be one of ["BSH", "BNSD", "BSND"]. Default: "BSH".
- num_key_value_heads: An optional int. Key value num heads. Default: 1.
- block_size: An optional int. Max length in pageattention's kv block. Default: 0.
- inner_precise: An optional int. When innerPrecise is 0, the high-precision mode is used.
When innerPrecise is 1, the high-performance mode is used. Default: 1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 query: bfloat16,float16
- input1 key: bfloat16,float16,int8
- input2 value: bfloat16,float16,int8
- input3 pse_shift: bfloat16,float16
- input4 atten_mask: bool,int8,uint8
- input5 actual_seq_lengths: int64
- input6 dequant_scale1: float32,uint64
- input7 quant_scale1: float32
- input8 dequant_scale2: float32,uint64
- input9 quant_scale2: bfloat16,float32
- input10 quant_offset2: bfloat16,float32
- input11 antiquant_scale: bfloat16,float16
- input12 antiquant_offset: bfloat16,float16
- input13 block_table: int32
- input14 kv_padding_size: int64
- output0 attention_out: bfloat16,float16,int8

## Attention Constraints

- Constraints for empty Input:
- Direct return if query is empty.
- If query exists, key and value are empty: output a zero-filled tensor of corresponding shape.
- AscendCLNN framework handles if attention_out is an empty tensor.
- No processing for parameters marked as can pass nullptr if they are null pointers.
- Key and value tensor shapes must match; batch in non-continuous scenarios can only be 1.
- Constraints for int8 quantization:
- Specific parameter existence and data format requirements based on input/output data formats.
- Both input and output int8: need deqScale1, quantScale1, deqScale2, quantScale2.
- Input int8, output float16: need deqScale1, quantScale1, deqScale2; error if quantOffset2 or quantScale2 not nullptr.
- Input float16/bf16, output int8: only quantScale2 needs to exist.
- Constraints for antiquant:
- Support per-tensor/per-channel formats and float32/bf16 data types.
- Types and shape of quantScale2 and quantOffset2 need to be consistent.
- Specific recommendations for quantScale2 shape based on input data type and output layout.
- Support per-channel, per-tensor, and per-token modes, and symmetric/asymmetric quantization.
- Per-channel mode: shape supports (2, N, 1, D), (2, N, D), (2, H); data type matches query; antiquantMode set to 0.
- Per-tensor mode: shape (2), data type matches query; antiquantMode set to 0.
- Per-token mode: shape (2, B, S), data type float32; antiquantMode set to 1.
- Symmetric quantization: antiquantOffset can be empty; if empty, symmetric quantization is performed.
- Asymmetric quantization: both antiquantScale and antiquantOffset need to exist.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
