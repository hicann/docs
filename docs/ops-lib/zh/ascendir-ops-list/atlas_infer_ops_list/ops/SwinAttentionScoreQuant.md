# SwinAttentionScoreQuant

```c
REG_OP(SwinAttentionScoreQuant)
    .INPUT(query, TensorType({DT_INT8}))
    .INPUT(key, TensorType({DT_INT8}))
    .INPUT(value, TensorType({DT_INT8}))
    .INPUT(scale_quant, TensorType({DT_FLOAT16}))
    .INPUT(scale_dequant1, TensorType({DT_UINT64}))
    .INPUT(scale_dequant2, TensorType({DT_UINT64}))
    .OPTIONAL_INPUT(bias_quant, TensorType({DT_FLOAT16}))
    .OPTIONAL_INPUT(bias_dequant1, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(bias_dequant2, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(padding_mask1, TensorType({DT_FLOAT16}))
    .OPTIONAL_INPUT(padding_mask2, TensorType({DT_FLOAT16}))
    .OUTPUT(attention_score, TensorType({DT_FLOAT16}))
    .ATTR(query_transpose, Bool, false)
    .ATTR(key_transpose, Bool, false)
    .ATTR(value_transpose, Bool, false)
    .ATTR(softmax_axes, Int, -1)
    .OP_END_FACTORY_REG(SwinAttentionScoreQuant)
```

## Brief

The quant fusion operator of SwinAttentionScoreQuant.

## Inputs

- query: A matrix Tensor. The type support int8.
- key: A matrix Tensor. The type support int8.
- value: A matrix Tensor. The type support int8.
- scale_quant: A Tensor. The type support fp16.
- scale_dequant1: A Tensor. The type support uint64.
- scale_dequant2: A Tensor. The type support uint64.
- bias_quant: A Tensor. The type support fp16.
- bias_dequant1: A Tensor. The type support int32.
- bias_dequant2: A Tensor. The type support int32.
- padding_mask1: A matrix Tensor. The type support fp16.
- padding_mask2: A matrix Tensor. The type support fp16.
- attention_score: A matrix Tensor. The type support fp16.

## Outputs

- attention_score: A matrix Tensor. The type support fp16.

## Attributes

- query_transpose: A bool. Whether query is transposed. Default: false.
- key_transpose: A bool. Whether key is transposed. Default: false.
- value_transpose: A bool. Whether value is transposed. Default: false.
- softmax_axes: An int. Which axes to calculate softmax. Default: -1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 query: int8
- input1 key: int8
- input2 value: int8
- input3 scale_quant: float16
- input4 scale_dequant1: uint64
- input5 scale_dequant2: uint64
- input6 bias_quant: float16
- input7 bias_dequant1: int32
- input8 bias_dequant2: int32
- input9 padding_mask1: float16
- input10 padding_mask2: float16
- output0 attention_score: float16


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
