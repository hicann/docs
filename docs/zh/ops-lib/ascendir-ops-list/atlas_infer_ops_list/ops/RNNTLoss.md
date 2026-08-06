# RNNTLoss

```c
REG_OP(RNNTLoss)
    .INPUT(acts, TensorType({DT_FLOAT}))
    .INPUT(labels, TensorType({DT_INT32}))
    .INPUT(input_lengths, TensorType({DT_INT32}))
    .INPUT(label_lengths, TensorType({DT_INT32}))
    .ATTR(blank_label, Int, 0)
    .OUTPUT(costs, TensorType({DT_FLOAT}))
    .OUTPUT(grads, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(RNNTLoss)
```

## Brief

Calculates the RNNT Loss (log probability) for each batch entry.
Also calculates the gradient.

## Inputs

- acts: 4-D, shape: `(batch x seqLength x labelLength x outputDim)`, the logits.
- labels: 2-D Tensor containing all the targets of the batch with zero padded.
- input_lengths: Tensor of size (batch) containing size of each output sequence.
- label_lengths: Tensor of (batch) containing label length of each example.

## Outputs

- costs: 1-D Tensor, the cost of each example in the batch.
- grads: A Tensor. Has the same type as acts.

## Attributes

blank_label: An optional attribute. Defaults to 0.

## Third-party framework compatibility

Compatible with TensorFlow RNNTLoss operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
