# GroupNormSilu

```c
REG_OP(GroupNormSilu)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(gamma, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(beta, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(mean, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(rstd, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(num_groups, Int)
    .ATTR(eps, Float, 0.00001f)
    .ATTR(activate_silu, Bool, true)
    .OP_END_FACTORY_REG(GroupNormSilu)
```

## Brief

Performs group normalization and silu.

## Inputs

Three inputs
- x: A ND Tensor of type bfloat16/float16/float32.
- gamma: A Tensor of type bfloat16/float16/float32.
Must be 1D. Specifies the scaling factor.
- beta: A Tensor of type bfloat16/float16/float32.
Must be 1D. Specifies the offset.

## Outputs

Three outputs
- y: A ND Tensor of type bfloat16/float16/float32 for the normalized "x".
- mean: A Tensor of type bfloat16/float16/float32.
Must be 1D. Specifies the mean of "x".
Ascend 950 AI Processor: The data type must be consistent with that of gamma and beta.
- rstd: A Tensor of type bfloat16/float16/float32.
Must be 1D. Specifies the rstd of "x".
Ascend 950 AI Processor: The data type must be consistent with that of gamma and beta.

## Attributes

- num_groups: An required int32/int64, specifying the number of group.
- eps: An optional float32, specifying the small value added to the
denominator for numerical stability. Defaults to "0.00001".
- activate_silu: An optional bool.  Defaults to "true".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 gamma: float16,float32
- input2 beta: float16,float32
- output0 y: float16,float32
- output1 mean: float16,float32
- output2 rstd: float16,float32

## Third-party framework compatibility

- Compatible with the PyTorch operator GroupNorm and Silu.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
