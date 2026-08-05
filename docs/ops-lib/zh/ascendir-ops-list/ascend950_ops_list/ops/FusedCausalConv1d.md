# FusedCausalConv1d

```c
REG_OP(FusedCausalConv1d)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16}))
    .INPUT(weight, TensorType({DT_BF16, DT_FLOAT16}))
    .INPUT(conv_states, TensorType({DT_BF16, DT_FLOAT16}))
    .OPTIONAL_INPUT(query_start_loc, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(cache_indices, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(initial_state_mode, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(bias, TensorType({DT_BF16, DT_FLOAT16}))
    .OPTIONAL_INPUT(num_accepted_tokens, TensorType({DT_INT32}))
    .ATTR(activation_mode, Int, 0)
    .ATTR(pad_slot_id, Int, -1)
    .ATTR(run_mode, Int, 0)
    .ATTR(residual_connection, Int, 0)
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16}))
    .OUTPUT(conv_states, TensorType({DT_BF16, DT_FLOAT16}))
    .OP_END_FACTORY_REG(FusedCausalConv1d)
```

## Brief

Applies causal 1D convolution on token sequences and updates the state cache. 

## Inputs

- x: Input sequence tensor. shape [cu_seq_len, dim] or [batch, seqlen, dim]. Supports float16, bfloat16.
- weight: Convolution kernel of shape [K, dim], K fixed to 3. Same type as x.
- conv_states: Cache state tensor storing K-1 historical tokens per sequence, updated in-place. Same type as x.
- query_start_loc: Optional. Start offset of each sequence in x. shape [batch+1]. int32.
- cache_indices: Optional. Index mapping each sequence to its cache slot in conv_states. shape [batch]. int32.
- initial_state_mode: Optional. Flag indicating whether each sequence uses cached data: 0=zero-padding, 1=use cache, 2=use cache but zero out the first K-1 outputs. shape [batch]. int32.
- bias: Optional. Convolution bias of shape [dim]. Same type as x.
- num_accepted_tokens: Optional. Number of accepted tokens per sequence in speculative decoding. shape [batch]. int32.

## Outputs

- y: Output sequence tensor. Same shape and type as x.
- conv_states: Updated cache state tensor. Same shape and type as input conv_states.

## Attributes

- activation_mode: An optional int. Activation function type: 0 (None), 1 (silu), 2 (swish). Default: 0.
- pad_slot_id: An optional int. Slot ID used to skip padding batches. Default: -1.
- run_mode: An optional int. Execution mode: 0 (prefill), 1 (decode). Default: 0.
- residual_connection: An optional int. Whether to use residual connection: 0 (no), 1 (yes). Default: 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- input1 weight: bfloat16,float16
- input2 conv_states: bfloat16,float16
- input3 query_start_loc: int32
- input4 cache_indices: int32
- input5 initial_state_mode: int32
- input6 bias: bfloat16,float16
- input7 num_accepted_tokens: int32
- output0 conv_states: bfloat16,float16
- output1 y: bfloat16,float16


---

[Back to Operator Specifications (Ascend950)](../README.md)
