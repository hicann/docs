# CTCLossV2

```c
REG_OP(CTCLossV2)
    .INPUT(log_probs, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(targets, TensorType({DT_INT32, DT_INT64}))
    .INPUT(input_lengths, TensorType({DT_INT32, DT_INT64}))
    .INPUT(target_lengths, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(neg_log_likelihood, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(log_alpha, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE}))
    .ATTR(blank, Int, 0)
    .ATTR(reduction, String, "mean")
    .ATTR(zero_infinity, Bool, false)
    .OP_END_FACTORY_REG(CTCLossV2)
```

## Brief

The Connectionist Temporal Classification loss.

## Inputs

- log_probs: A tensor. Must be one of the following types: float16, bfloat16, float32, double. Tensor of size (T, N, C), where T =input length, N =batch size,
and C = number of classes (including blank).
It represent the logarithmized probabilities of the outputs.
- targets: A tensor. Must be one of the following types: int32, int64. Tensor of size (N, S) or sum(target_lengths), where S = max target length.
It represent the target sequences. The value range is [0, C-1], where C represents the last dimension in log_probs.
- input_lengths: A tensor. Must be one of the following types: int32, int64. Tuple or tensor of size (N). It represent the lengths of the inputs.
- target_lengths: A tensor. Must be one of the following types: int32, int64. Tuple or tensor of size (N). It represent lengths of the targets.

## Outputs

- neg_log_likelihood: A tensor. Has the same dtype as log_probs, tuple or tensor of size (N). A loss value which is differentiable with respect to each input node.
- log_alpha: A tensor. Has the same dtype as log_probs, tensor of size (N, T, X), where X = 2 * max(target_lengths) + 1.
The probability of possible trace of input to target.

## Attributes

- blank: An optional Int. Blank label. Default 0.
- reduction: An optional String. Specifies the reduction to apply to the output: 'none' | 'mean' | 'sum'. Default: 'mean'.
- zero_infinity: An optional Bool. Whether to zero infinite losses and the associated gradients. Default: false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 log_probs: double,float32
- input1 targets: int32,int64
- input2 input_lengths: int32,int64
- input3 target_lengths: int32,int64
- output0 neg_log_likelihood: double,float32
- output1 log_alpha: double,float32

## Attention Constraints

The limit of Label’s length is 1K.

## Third-party framework compatibility

Compatible with Pytorch CTCLoss operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
