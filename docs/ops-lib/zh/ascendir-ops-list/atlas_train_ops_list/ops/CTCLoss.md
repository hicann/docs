# CTCLoss

```c
REG_OP(CTCLoss)
    .INPUT(inputs, TensorType({DT_FLOAT, DT_DOUBLE}))
    .INPUT(labels_indices, TensorType({DT_INT64}))
    .INPUT(labels_values, TensorType({DT_INT32}))
    .INPUT(sequence_length, TensorType({DT_INT32}))
    .OUTPUT(loss, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(gradient, TensorType({DT_FLOAT, DT_DOUBLE}))
    .ATTR(preprocess_collapse_repeated, Bool, false)
    .ATTR(ctc_merge_repeated, Bool, true)
    .ATTR(ignore_longer_outputs_than_inputs, Bool, false)
    .OP_END_FACTORY_REG(CTCLoss)
```

## Brief

Calculates the CTC Loss (log probability) for each batch entry.
Also calculates the gradient. 

## Inputs

- inputs: 3-D, shape: `(max_time x batch_size x num_classes)`, the logits.
- labels_indices: The indices of a `SparseTensor<int32, 2>`.
`labels_indices(i, :) == [b, t]` means `labels_values(i)` stores the id for
`(batch b, time t)`.
- labels_values: The values (labels) associated with the given batch and time.
- sequence_length: A vector containing sequence lengths (batch).

## Outputs

- loss: A vector (batch) containing log-probabilities.
- gradient: The gradient of `loss`.  3-D, shape: `(max_time x
batch_size x num_classes)`. 

## Attributes

- preprocess_collapse_repeated: Scalar, if true then repeated labels are collapsed prior to
the CTC calculation.If not specified, defaults to false
- ctc_merge_repeated: Scalar. If set to false, *during* CTC calculation
repeated non-blank labels will not be merged and are interpreted as
individual labels.  This is a simplified version of CTC.
If not specified, defaults to true. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input1 labels_indices: int64
- input2 labels_values: int32
- input3 sequence_length: int32

## Third-party framework compatibility

Compatible with TensorFlow CTCLoss operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
