# RecurrentGatedDeltaRule

```c
REG_OP(RecurrentGatedDeltaRule)
.INPUT(query, "T1")
.INPUT(key, "T1")
.INPUT(value, "T1")
.INPUT(beta, "T1")
.INPUT(state, "T1")
.INPUT(actual_seq_lengths, "T2")
.INPUT(ssm_state_indices, "T2")
.OPTIONAL_INPUT(g, "T3")
.OPTIONAL_INPUT(gk, "T3")
.OPTIONAL_INPUT(num_accepted_tokens, "T2")
.OUTPUT(out, "T1")
.OUTPUT(state, "T1")
.ATTR(scale_value, Float, 1.0)
.DATATYPE(T1, TensorType({DT_BF16}))
.DATATYPE(T2, TensorType({DT_INT32}))
.DATATYPE(T3, TensorType({DT_FLOAT}))
.OP_END_FACTORY_REG(RecurrentGatedDeltaRule)
```

## Brief

Recurrent Gated Delta Rule operator interface implementation.

## Inputs

- query: queries of shape [T, Nk, Dk]. Support dtype: bfloat16. Support format: ND.
- key: keys of shape [T, Nk, Dk]. Support dtype: bfloat16. Support format: ND.
- value: values of shape [T, Nv, Dv]. Support dtype: bfloat16. Support format: ND.
- beta: betas of shape [T, Nv]. Support dtype: bfloat16. Support format: ND.
- state: initial states of shape [BlockNum, Nv, Dv, Dk]. Support dtype: bfloat16. Support format: ND.
- actual_seq_lengths: actual sequence length of shape [B,] used for variable-length training. Support dtype: int32. Support format: ND.
- ssm_state_indices: indices to map the input sequences to the states of shape [T,]. Support dtype: int32. Support format: ND.
- g: decays of shape [T, Nv], alpha = e^g. Support dtype: float32. Support format: ND.
- gk: key decays of shape [T, Nv, Dk], alpha = e^g. Support dtype: float32. Support format: ND.
- num_accepted_tokens: number of accepted tokens for each sequence during decoding of shape (B,). Support dtype: int32. Support format: ND.

## Attributes

scale_value: scale factor for the RetNet attention scores, usually 1/sqrt(Dk), the default value is 1.0. dtype: float32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 query: bfloat16
- input1 key: bfloat16
- input2 value: bfloat16
- input3 beta: bfloat16
- input4 state: bfloat16,float32
- input5 actual_seq_lengths: int32
- input6 ssm_state_indices: int32
- input7 g: float32
- input8 gk: float32
- input9 num_accepted_tokens: int32
- output0 out: bfloat16
- output1 state: bfloat16,float32

## Output

- out: outputs of shape [T, Nv,Dv]. Support dtype: bfloat16. Support format: ND.
- state: final states of shape [BlockNum, Nv, Dv, Dk]. Support dtype: bfloat16. Support format: ND.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
