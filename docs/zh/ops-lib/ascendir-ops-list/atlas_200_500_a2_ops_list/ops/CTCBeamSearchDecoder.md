# CTCBeamSearchDecoder

```c
REG_OP(CTCBeamSearchDecoder)
    .INPUT(inputs, TensorType({DT_FLOAT, DT_DOUBLE}))
    .INPUT(sequence_length, TensorType({DT_INT32}))
    .REQUIRED_ATTR(beam_width, Int)
    .REQUIRED_ATTR(top_paths, Int)
    .ATTR(merge_repeated, Bool, true)
    .DYNAMIC_OUTPUT(decoded_indices, TensorType({DT_INT64}))
    .DYNAMIC_OUTPUT(decoded_values, TensorType({DT_INT64}))
    .DYNAMIC_OUTPUT(decoded_shape, TensorType({DT_INT64}))
    .OUTPUT(log_probability, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(CTCBeamSearchDecoder)
```

## Brief

Performs beam search decoding on the logits given in input. 

## Inputs

- inputs: 3-D, shape: `(max_time x batch_size x num_classes)`, the logits.
- sequence_length: A vector containing sequence lengths, size `(batch_size)`.

## Outputs

- decoded_indices: A list (length: top_paths) of indices matrices.  Matrix j,
size `(total_decoded_outputs[j] x 2)`, has indices of a
`SparseTensor<int64, 2>`.  The rows store: [batch, time].
- decoded_values: A list (length: top_paths) of values vectors.  Vector j,
size `(length total_decoded_outputs[j])`, has the values of a
`SparseTensor<int64, 2>`.  The vector stores the decoded classes for beam j.
- decoded_shape: A list (length: top_paths) of shape vector.  Vector j,
size `(2)`, stores the shape of the decoded `SparseTensor[j]`.
Its values are: `[batch_size, max_decoded_length[j]]`.
- log_probability: A matrix, shaped: `(batch_size x top_paths)`.  The
sequence log-probabilities. 

## Attributes

- merge_repeated: If True, merge repeated classes in output.
- beam_width:A scalar >= 0 (beam search beam width).
- top_paths:A scalar >= 0, <= beam_width (controls output size).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 inputs: double,float32
- input1 sequence_length: int32
- output0 log_probability: double,float32

## Third-party framework compatibility

Compatible with TensorFlow CTCBeamSearchDecoder operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
