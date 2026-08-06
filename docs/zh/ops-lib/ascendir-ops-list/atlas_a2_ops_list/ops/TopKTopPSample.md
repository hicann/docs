# TopKTopPSample

```c
REG_OP(TopKTopPSample)
    .INPUT(logits, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(top_k, TensorType({DT_INT32}))
    .INPUT(top_p, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(q, TensorType({DT_FLOAT}))
    .OUTPUT(logits_select_idx, TensorType({DT_INT64}))
    .OUTPUT(logits_top_kp_select, TensorType({DT_FLOAT}))
    .ATTR(eps, Float, 1E-8)
    .ATTR(is_need_logits, Bool, false)
    .ATTR(top_k_guess, Int, 32)
    .OP_END_FACTORY_REG(TopKTopPSample)
```

## Brief

Perform topk-topp-sample sampling calculations based on input word frequency logits, top-k/top-p sampling
parameters, and random sampling weight distribution q. Output the maximum word frequency logits_select_idx for each
batch, along with the word frequency distribution logits_top_kp_select after topk-topp sampling.

## Inputs

Four inputs, including:
- logits: A Required tensor in [batch, voc_size] on default. Acts as the input word frequencies to be sampled. The
frequency index is fixed as the last dimension. Currently supports 2 dimensions. Supports non-contiguous tensors, and
must be a non-null pointer.
  The supported types are:float16, bfloat16, format supports ND.
- top_k: A Required tensor in [batch, ] on default. Acts as the sampled k-value for each batch. The supported types
are: int32, Supports non-contiguous tensors, and must be a non-null pointer.
- top_p: A Required tensor in [batch, ] on default. Acts as the p-value sampled for each batch. The supported types
are: float16, bfloat16, Supports non-contiguous tensors, and must be a non-null pointer.
- q: An optional tensor in [batch, voc_size], Defaults to "None". A Required tensor in [batch, ] on default. Acts as
the sampled k-value for each batch. The supported types are: float32, Supports non-contiguous tensors.

## Outputs

- logits_select_idx: A 2D tensor which is the sequence of numbers, format supports ND, and must be a non-null
pointer.
   The supported types are: int64. 
- logits_top_kp_select: An optional 2D tensor. Acts as the logits remaining in the logits file after undergoing the
topK-topP calculation process. When `is_need_logits=False`, it is disabled and outputs a null pointer; when
`is_need_logits=True`, it is enabled and outputs a dimension that must be [batch, voc_size]. The supported types are:
float32.

## Attributes

- eps: An optional attribute of type float. Prevent division by zero in softmax and weight sampling; default value
1e-8.
- is_need_logits：An optional attribute of type bool. Control the output condition of logits_top_kp_select,
defaulting to False for empty return. When set to True, a Tensor sized of [batch, voc_size] contains only remaining
logits at their origin position in the input logits, will be returned as the logits_top_kp_select.
- top_k_guess: An optional attribute of type int32. Indicates the size of candidate logits for each batch when
attempting top-P partial traversal sampling. Must be a positive integer, defaulting to 32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 logits: bfloat16,float16
- input1 top_k: int32
- input2 top_p: bfloat16,float16
- input3 q: float32
- output0 logits_select_idx: int64
- output1 logits_top_kp_select: float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Range or PyTorch operator Range/Arange.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
