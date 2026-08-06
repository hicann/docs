# GroupNormGrad

```c
REG_OP(GroupNormGrad)
    .INPUT(dy, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(mean, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(rstd, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(dx, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(dgamma, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(dbeta, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(num_groups, Int)
    .ATTR(data_format, String, "NCHW")
    .ATTR(dx_is_require, Bool, true)
    .ATTR(dgamma_is_require, Bool, true)
    .ATTR(dbeta_is_require, Bool, true)
    .OP_END_FACTORY_REG(GroupNormGrad)
```

## Brief

backward operator for group normalization. 

## Inputs

Five input, including:
- dy: A tensor. Group grad. Datatype support float32, float16, bfloat16. Format support ND.
"dy" supports 2-8 dimensions (N, C, *), the calculation logic only cares about the first two dimensions (N and C),
and the rest can all be combined into one dimension.
- mean: A tensor. Mean of each group. Datatype support float32, float16, bfloat16. Format support ND.
Must be 2D (N, num_groups).
- rstd: A tensor. Reciprocal standard deviation of each group. Datatype support float32, float16, bfloat16. Format support ND.
Must be 2D (N, num_groups).
- x: A Tensor. Specifies the offset. Datatype support float32, float16, bfloat16. Format support ND.
"x" supports 2-8 dimensions (N, C, *), the calculation logic only cares about the first two dimensions (N and C),
and the rest can all be combined into one dimension.
- gamma: A tensor. Specifies the scaling factor. Datatype support float32, float16, bfloat16. Format support ND.
Must be 1D. The value of "gamma" needs to be consistent with the C-axis value of "x".

## Outputs

Three output, including:
- dx: A tensor. x factor grad. Datatype is the same as the input datatype. Has the same format and shape as "x".
- dgamma: A tensor. Scale factor grad. Has the same datatype, format and shape as "gamma".
- dbeta: A tensor. Offset factor grad. Has the same datatype, format and shape as "gamma".

## Attributes

- num_groups: Int. Number specifying the number of group.
- data_format: An optional string. Defaults to NCHW.
- dx_is_require: An optional bool, controls whether to return dx. Defaults to true.
- dgamma_is_require: An optional bool, controls whether to return dgamma. Defaults to true.
- dbeta_is_require: An optional bool, controls whether to return dbeta. Defaults to true.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: bfloat16,float16,float32
- input1 mean: bfloat16,float16,float32
- input2 rstd: bfloat16,float16,float32
- input3 x: bfloat16,float16,float32
- input4 gamma: bfloat16,float16,float32
- output0 dx: bfloat16,float16,float32
- output1 dgamma: bfloat16,float16,float32
- output2 dbeta: bfloat16,float16,float32

## Third-party framework compatibility

- Compatible with the backward of PyTorch operator GroupNorm.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
