# EmbeddingBag

```c
REG_OP(EmbeddingBag)
    .INPUT(weight, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .OPTIONAL_INPUT(offsets, TensorType({DT_INT32, DT_INT64}))
    .OPTIONAL_INPUT(per_sample_weights, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(offset2bag, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(bag_size, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(max_indices, TensorType({DT_INT32, DT_INT64}))
    .ATTR(mode, String, "mean")
    .ATTR(scale_grad_by_freq, Bool, false)
    .ATTR(sparse, Bool, false)
    .ATTR(include_last_offset, Bool, false)
    .ATTR(padding_idx, Int, -1)
    .OP_END_FACTORY_REG(EmbeddingBag)
```

## Brief

Calculates the reversed outputs of the function "embedding". 

## Inputs

Four inputs, including:
- weight: A required Tensor. A mutable Tensor of word grad. Must be one of the following types: float16, float32,
bfloat16.
- indices: A required Tensor. A mutable word index Tensor. Must be one of the following types: int32, int64.
- offsets: A optional Tensor. A mutable word index Tensor. Must be one of the following types: int32, int64.
- per_sample_weights: A optional Tensor. to indicate all weights should be taken to be 1. Must be one of the
following types: float16, float32, bfloat16.
    If specified, per_sample_weights must have exactly the same shape as input
    and is treated as having the same offsets, if those are not None.
    Only supported for mode='sum'.

## Outputs

four outputs: 
y: A mutable output Tensor of new word grad has the same type as "grads". 
offset2bag:A Tensor. Must be one of the following types: int32, int64. 
bag_size:A Tensor. Must be one of the following types: int32, int64. 
max_indices:A Tensor. Must be one of the following types: int32, int64. 

## Attributes

- mode: An string attr which use "sum"``, ``"mean"`` or ``"max"``. Specifies the way to reduce the bag. Defaults to
"mean".
- padding_idx: An int attr judge which word to fill zeros. Defaults to "-1".
- scale_grad_by_freq: An optional bool. Defaults to "False".
    If "True", "grad_weight" will be scale by word_frequency.
    If "False", "grad_weight" will not be scale by word_frequency. 
- sparse: An optional bool. Defaults to "False". if True, gradient w.r.t.attr weight matrix will be a sparse tensor.
- include_last_offset: An optional bool. Defaults to "False". if True, attr offsets has one additional element,
where the last element
    is equivalent to the size of indices. This matches the CSR format. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 weight: float16,float32
- input1 indices: int32
- input2 offsets: int32
- output0 y: float16,float32
- output1 offset2bag: int32
- output2 bag_size: int32
- output3 max_indices: int32

## Third-party framework compatibility

Compatible with the Pytorch operator EmbeddingBag.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
