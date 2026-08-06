# SwinTransformerLnQkvQuant

```c
REG_OP(SwinTransformerLnQkvQuant)
    .INPUT(x, TensorType({DT_FLOAT16}))
    .INPUT(gamma, TensorType({DT_FLOAT16}))
    .INPUT(beta, TensorType({DT_FLOAT16}))
    .INPUT(weight, TensorType({DT_FLOAT16}))
    .INPUT(bias, TensorType({DT_FLOAT16}))
    .INPUT(quant_scale, TensorType({DT_FLOAT16}))
    .INPUT(quant_offset, TensorType({DT_FLOAT16}))
    .INPUT(dequant_scale, TensorType({DT_UINT64}))
    .OUTPUT(query_output, TensorType({DT_FLOAT16}))
    .OUTPUT(key_output, TensorType({DT_FLOAT16}))
    .OUTPUT(value_output, TensorType({DT_FLOAT16}))
    .REQUIRED_ATTR(head_num, Int)
    .REQUIRED_ATTR(seq_length, Int)
    .REQUIRED_ATTR(epsilon, Float)
    .REQUIRED_ATTR(ori_height, Int)
    .REQUIRED_ATTR(ori_weight, Int)
    .REQUIRED_ATTR(h_win_szie, Int)
    .REQUIRED_ATTR(w_win_size, Int)
    .REQUIRED_ATTR(weight_transpose, Bool)
    .OP_END_FACTORY_REG(SwinTransformerLnQkvQuant)
```

## Inputs

Eight inputs, including:
- x: A Tensor. Must be one of the following types: float16.
- gamma: A Tensor. Must be one of the following types: float16.
- beta: A Tensor. Must be one of the following types: float16.
- weight: A Tensor. Must be one of the following types: int8.
- bias: A Tensor. Must be one of the following types: float16.
- quant_scale: A Tensor. Must be one of the following types: float16.
- quant_offset: A Tensor. Must be one of the following types: float16.
- dequant_scale: A Tensor. Must be one of the following types: uint64.

## Outputs

Three outputs, including:
- query_output: A Tensor. Must be one of the following types: float16.
- key_output: A Tensor. Must be one of the following types: float16.
- value_output: A Tensor. Must be one of the following types: float16.

## Attributes

- head_num: A required attribute, the type is int. Defaults to 1.
- seq_length: A required attribute, the type is int. Defaults to 32.
- epsilon: A required attribute, the type is float. Defaults to 0.000001.
- ori_height: A required attribute, the type is int. Defaults to 7
- ori_weight: A required attribute, the type is int. Defaults to 7.
- h_win_szie: A required attribute, the type is int. Defaults to 7.
- w_win_size: A required attribute, the type is int. Defaults to 7.
- weight_transpose: A required attribute, the type is bool. Defaults to true.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- input1 gamma: float16
- input2 beta: float16
- input3 weight: int8
- input4 bias: int32
- input5 quant_scale: float16
- input6 quant_offset: float16
- input7 dequant_scale: uint64
- output0 query_output: float16
- output1 key_output: float16
- output2 value_output: float16


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
