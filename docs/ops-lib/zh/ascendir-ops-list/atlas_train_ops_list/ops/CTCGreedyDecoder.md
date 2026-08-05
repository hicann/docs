# CTCGreedyDecoder

```c
REG_OP(CTCGreedyDecoder)
    .INPUT(inputs, TensorType({DT_FLOAT, DT_DOUBLE}))
    .INPUT(sequence_length, TensorType({DT_INT32}))
    .ATTR(merge_repeated, Bool, false)
    .OUTPUT(decoded_indices, TensorType({DT_INT64}))
    .OUTPUT(decoded_values, TensorType({DT_INT64}))
    .OUTPUT(decoded_shape, TensorType({DT_INT64}))
    .OUTPUT(log_probability, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(CTCGreedyDecoder)
```

## Brief

Performs greedy decoding on the logits given in inputs. 

## Inputs

- inputs: 3-D, shape: `(max_time x batch_size x num_classes)`, the logits.
- sequence_length: A vector containing sequence lengths, size `(batch_size)`.

## Outputs

- decoded_indices: Indices matrix, size `(total_decoded_outputs x 2)`,
of a `SparseTensor<int64, 2>`.  The rows store: [batch, time].
- decoded_values: Values vector, size: `(total_decoded_outputs)`,
of a `SparseTensor<int64, 2>`.  The vector stores the decoded classes.
- decoded_shape: Shape vector, size `(2)`, of the decoded SparseTensor.
Values are: `[batch_size, max_decoded_length]`.
- log_probability: Matrix, size `(batch_size x 1)`, containing sequence
log-probabilities. 

## Attributes

merge_repeated: If True, merge repeated classes in output. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input1 sequence_length: int32
- output0 decoded_indices: int64
- output1 decoded_values: int64
- output2 decoded_shape: int64
- output3 log_probability: double,float32

## Third-party framework compatibility

Compatible with TensorFlow CTCGreedyDecoder operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
