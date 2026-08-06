# FFN

```c
REG_OP(FFN)
    .INPUT(x, TensorType({DT_INT8, DT_FLOAT16, DT_BF16}))
    .INPUT(weight1, TensorType({DT_INT8, DT_FLOAT16, DT_BF16, DT_INT4}))
    .INPUT(weight2, TensorType({DT_INT8, DT_FLOAT16, DT_BF16, DT_INT4}))
    .OPTIONAL_INPUT(expert_tokens, TensorType({DT_INT64}))
    .OPTIONAL_INPUT(bias1, TensorType({DT_INT32, DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(bias2, TensorType({DT_INT32, DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(scale, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(offset, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(deq_scale1, TensorType({DT_UINT64, DT_BF16, DT_INT64, DT_FLOAT}))
    .OPTIONAL_INPUT(deq_scale2, TensorType({DT_UINT64, DT_BF16, DT_INT64, DT_FLOAT}))
    .OPTIONAL_INPUT(antiquant_scale1, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(antiquant_scale2, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(antiquant_offset1, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(antiquant_offset2, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(activation, String)
    .ATTR(inner_precise, Int, 0)
    .ATTR(output_dtype, Int, -1)
    .ATTR(tokens_index_flag, Bool, false)
    .OP_END_FACTORY_REG(FFN)
```

## Brief

Fusion op for FFN. This op supports to compute MoeFFN(Mixture-of-Experts) or FFN.

## Inputs

fourteen inputs, including:
- x: A matrix Tensor. The type support int8, float16, bfloat16.
Format support ND, FRACTAL_NZ. Shape supports at least 2 dimensions (M,K1), and at most 8 dimensions.
- weight1: A matrix Tensor for weight of the first matmul. The type support int4, int8, float16, bfloat16.
Format support ND, FRACTAL_NZ. When having experts/having no expert, shape should be (E, K1, N1)/(K1, N1).
- weight2: A matrix Tensor for weight of the second matmul. The type support int4, int8, float16, bfloat16.
Format support ND, FRACTAL_NZ. When having experts/having no expert, shape should be (E, K2, N2)/(K2, N2).
- expert_tokens: A matrix Tensor. Indicating num of tokens in each of experts. If having experts, expert_tokens should be passed; if having no experts, expert_tokens should not be passed.
The type support int64. Format support ND. If not null, shape should be (E) and should satisfy E <= 256.
- bias1: A matrix Tensor for bias of the first matmul. The type support int32, float16, float32. Format support ND.
When having experts/having no expert, shape should be (E, N1)/(N1).
- bias2: A matrix Tensor for bias of the secend matmul. The type support int32, float16, float32. Format support ND.
When having experts/having no expert, shape should be (E, N2)/(N2).
- scale: A matrix Tensor. Indicating scaling factor of quantization parameter.
The type support float32. Format support ND. In per-tensor quantization cases, when having experts/having no expert, shape should be (E)/(1).
In per-channel quantization cases, when having experts/having no expert, shape should be (E, N1)/(N1).
- offset: A matrix Tensor. Indicating the offset of the quantization parameter.
The type support float32. Format support ND. When having experts/having no expert, shape should be (E)/(1).
- deq_scale1: A matrix Tensor. Indicating scaling factor of dequantization parameter for the first matmul.
The type support uint64, int64, float32, bfloat16. Format support ND. When having experts/having no expert, shape should be (E, N1)/(N1).
- deq_scale2: A matrix Tensor. Indicating scaling factor of dequantization parameter for the second matmul.
The type support uint64, int64, float32, bfloat16. Format support ND. When having experts/having no expert, shape should be (E, N2)/(N2).
- antiquant_scale1: A matrix Tensor. Indicating the scaling factor of the fake-quantization parameter for the first matmul.
The type support float16, bfloat16. Format support ND. In per-channel fake-quantization cases, when having experts/having no expert, shape should be (E, N1)/(N1).
In per-in-group fake-quantization cases, when having experts/having no expert, shape should be (E, G1, N1)/(G1, N1).
- antiquant_scale2: A matrix Tensor. Indicating the scaling factor of the fake-quantization parameter for the second matmul.
The type support float16, bfloat16. Format support ND. In per-channel fake-quantization cases, when having experts/having no expert, shape should be (E, N1)/(N1).
In per-in-group fake-quantization cases, when having experts/having no expert, shape should be (E, G2, N2)/(G2, N2).
- antiquant_offset1: A matrix Tensor. Indicating the offset of the fake-quantization parameter for the first matmul.
The type support float16, bfloat16. Format support ND. In per-channel fake-quantization cases, when having experts/having no expert, shape should be (E, N2)/(N2).
In per-in-group fake-quantization cases, when having experts/having no expert, shape should be (E, G1, N1)/(G1, N1).
- antiquant_offset2: A matrix Tensor. Indicating the offset of the fake-quantization parameter for the second matmul.
The type support float16, bfloat16. Format support ND. In per-channel fake-quantization cases, when having experts/having no expert, shape should be (E, N2)/(N2).
In per-in-group fake-quantization cases, when having experts/having no expert, shape should be (E, G2, N2)/(G2, N2).

## Outputs

y: A matrix Tensor. The type support float16, bfloat16.
Format support ND, FRACTAL_NZ. Num of dimension should be same as x.
The following are the supported data formats and data types (for Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component):
| Tensor    | x       | weight1/weight2 | bias1/bias2 | scale/offset | deq_scale1/deq_scale2 | antiquant_scale1/antiquant_scale2  | antiquant_offset1/antiquant_offset2 | y       |
| :-------: | :-----: | :-------------: | :---------: | :----------: | :-------------------: | :--------------------------------: | :---------------------------------: | :-----: |
| Format1   | ND      | ND              | ND          | ND           | ND                    | ND                                 | ND                                  | ND      |
| Data Type | float16 | float16         | float16     | -            | -                     | -                                  | -                                   | float16 |
|           | bfloat16| bfloat16        | float32     | -            | -                     | -                                  | -                                   | bfloat16|
|           | int8    | int8            | int32       | float32      | uint64                | -                                  | -                                   | float16 |
|           | int8    | int8            | int32       | float32      | bfloat16              | -                                  | -                                   | bfloat16|
|           | int8    | int8            | int32       | float32      | int64                 | -                                  | -                                   | float16 |
|           | int8    | int8            | int32       | float32      | float32               | -                                  | -                                   | float16 |
|           | float16 | int8            | float16     | -            | -                     | float16                            | float16                             | float16 |
|           | bfloat16| int8            | float32     | -            | -                     | bfloat16                           | bfloat16                            | bfloat16|
|           | float16 | int4            | float16     | -            | -                     | float16                            | float16                             | float16 |
|           | bfloat16| int4            | float32     | -            | -                     | bfloat16                           | bfloat16                            | bfloat16|
The following are the supported data formats and data types (for Atlas Inference Series Product):
| Tensor    | x          | weight1/weight2 | bias1/bias2 | scale/offset | deq_scale1/deq_scale2 | antiquant_scale1/antiquant_scale2  | antiquant_offset1/antiquant_offset2 | y          |
| :-------: | :--------: | :-------------: | :---------: | :----------: | :-------------------: | :--------------------------------: | :---------------------------------: | :--------: |
| Format1   | FRACTAL_NZ | FRACTAL_NZ      | ND          | ND           | ND                    | ND                                 | ND                                  | FRACTAL_NZ |
| Data Type | float16    | float16         | float16     | -            | -                     | -                                  | -                                   | float16    |

## Attributes

- activation: A string. The type of activation. Support fastgelu, gelu, relu, silu, geglu, swiglu and reglu.
- inner_precise: An int. 0, fp16 high precision. 1, high performance. Default value: 0
- output_dtype: An int. -1, output data type is float16. 0, output data type is float16. 1, output data type is bfloat16. Default -1.
- tokens_index_flag: A bool. false, values in expert_tokens are values. true, values in expert_tokens are indices. Default value: false

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,int8
- input1 weight1: bfloat16,float16,int4,int8
- input2 weight2: bfloat16,float16,int4,int8
- input3 expert_tokens: int64
- input4 bias1: float16,float32,int32
- input5 bias2: float16,float32,int32
- input6 scale: float32
- input7 offset: float32
- input8 deq_scale1: bfloat16,float32,int64,uint64
- input9 deq_scale2: bfloat16,float32,int64,uint64
- input10 antiquant_scale1: bfloat16,float16
- input11 antiquant_scale2: bfloat16,float16
- input12 antiquant_offset1: bfloat16,float16
- input13 antiquant_offset2: bfloat16,float16
- output0 y: bfloat16,float16

## Attention Constraints

- Atlas Inference Series Product only support non-quantization high performance no-expert cases; x and y must have two dimensions; activation only supports gelu/fastgelu/relu/silu.
- If expert_tokens is passed, when tokens_index_flag is true, it must be a non-negative monotone non-decreasing array; when tokens_index_flag is false, it must be a non-negative array.
- If expert_tokens is passed, when tokens_index_flag is false, sum of expert_tokens should be equal to the first dim M of x; when tokens_index_flag is true, the last value in expert_tokens should be equal to the first dim M of x.
- If activation is geglu/swiglu/reglu, only supporting float16 (data type of required inputs are all float16) high performance no-expert cases, and should satisfy N1=2*K2.
- If activation is gelu/fastgelu/relu/silu, should satisfy N1=K2.
- All cases should satisfy K1=N2, K1<65536, K2<65536, and M should be less than 2147483547 after aligning to 32 byte.
- Non-quantization cases should not pass quantization or fake-quantization related optional inputs, quantization cases should not pass fake-quantization related optional inputs, fake-quantization cases should not pass quantization related optional inputs.
- Per-tensor quantization cases support data type template with deq_scale1/deq_scale2 float32, while per-channel quantization cases do not support this data type template.
- If data type of weight1 and weight2 is int4, the last dimension of weight1 and weight2 must be even.
- In per-in-group fake-quantization cases, group num G1 of antiquant_scale1 and antiquant_offset1 must be divisible by K1, group num G2 of antiquant_scale2 and antiquant_offset2 must be divisible by K2.
- Attr inner_precise is only valid in non-quantization cases. In non-quantization cases, if data type of required inputs are all bfloat16, inner_precise only supports 0; if data type of required inputs are all float16, inner_precise can pass 0 or 1.
- Attr output_dtype is only valid in quantization cases.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
