# CTCLossV2Grad

```c
REG_OP(CTCLossV2Grad)
    .INPUT(grad_out, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT,DT_DOUBLE}))
    .INPUT(log_probs, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(targets, TensorType({DT_INT32, DT_INT64}))
    .INPUT(input_lengths, TensorType({DT_INT32, DT_INT64}))
    .INPUT(target_lengths, TensorType({DT_INT32, DT_INT64}))
    .INPUT(neg_log_likelihood, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(log_alpha, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(grad, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE}))
    .ATTR(blank, Int, 0)
    .ATTR(reduction, String, "mean")
    .ATTR(zero_infinity, Bool, false)
    .OP_END_FACTORY_REG(CTCLossV2Grad)
```

## Brief

The Connectionist Temporal Classification loss grad.

## Inputs

- grad_out: A tensor. Has the same dtype as log_probs. Gradient renewal coefficient. Tensor of size (N), where N = batch size.
- log_probs: A tensor. Must be one of the following types: float16, bfloat16, float32, double. Tensor of size (T, N, C), where T =input length, N =batch size,
and C = number of classes (including blank).
It represent the logarithmized probabilities of the outputs.
- targets: A tensor. Must be one of the following types: int32, int64. Tensor of size (N, S) or sum(target_lengths), where S = max target length.
It represent the target sequences.
- input_lengths: A tensor. Must be one of the following types: int32, int64. Tuple or tensor of size (N). It represent the lengths of the inputs.
- target_lengths: A tensor. Must be one of the following types: int32, int64. Tuple or tensor of size (N). It represent lengths of the targets.
- neg_log_likelihood: A tensor. Has the same dtype as log_probs, tuple or tensor of size (N).
A loss value which is differentiable with respect to each input node.
- log_alpha: A tensor. Has the same dtype as log_probs, tensor of size (N, T, X), where X = 2 * max(target_lengths) + 1.
The probability of possible trace of input to target.

## Outputs

- grad: A tensor. Has the same dtype as log_probs. Tensor of size (T, N, C), The grad of Connectionist Temporal Classification loss.

## Attributes

- blank: An optional Int. Blank label. Default 0.
- reduction: An optional String. Specifies the reduction to apply to the output: 'none' | 'mean' | 'sum'. Default: 'mean'.
- zero_infinity: An optional Bool. Whether to zero infinite losses and the associated gradients. Default: false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad_out: bfloat16,float16,float32
- input1 log_probs: bfloat16,float16,float32
- input2 targets: int32,int64
- input3 input_lengths: int32,int64
- input4 target_lengths: int32,int64
- input5 neg_log_likelihood: bfloat16,float16,float32
- input6 log_alpha: bfloat16,float16,float32
- output0 grad: bfloat16,float16,float32
### AI CPU
- input0 grad_out: double,float32
- input1 log_probs: double,float32
- input2 targets: int32,int64
- input3 input_lengths: int32,int64
- input4 target_lengths: int32,int64
- input5 neg_log_likelihood: double,float32
- input6 log_alpha: double,float32
- output0 grad: double,float32

## Attention Constraints

The limit of Label’s length is 1K.

## Third-party framework compatibility

Compatible with Pytorch CTCLoss operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
