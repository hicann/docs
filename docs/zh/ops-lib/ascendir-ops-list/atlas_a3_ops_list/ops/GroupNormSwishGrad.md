# GroupNormSwishGrad

```c
REG_OP(GroupNormSwishGrad)
    .INPUT(dy, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(mean, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(rstd, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(beta, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(dx, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(dgamma, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(dbeta, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(num_groups, Int)
    .ATTR(data_format, String, "NCHW")
    .ATTR(swish_scale, Float, 1.0)
    .ATTR(dgamma_is_require, Bool, true)
    .ATTR(dbeta_is_require, Bool, true)
    .OP_END_FACTORY_REG(GroupNormSwishGrad)
```

## Brief

Performs the backward operation of group normalization and swish.

## Inputs

Six input, including:
- dy: A Tensor. Group grad. Datatype support float32, float16, bfloat16. Format support ND.
- mean: A Tensor. Mean of each group. Datatype support float32, float16, bfloat16. Format support ND.
- rstd: A Tensor. Reciprocal standard deviation of each group. Datatype support float32, float16, bfloat16. Format support ND.
- x: A Tensor. Specifies the offset. Datatype support float32, float16, bfloat16. Format support ND. Same shape as mean.
- gamma: A Tensor. Specifies the scaling factor. Datatype support float32, float16, bfloat16. Format support ND. Same shape as dy.
- beta: A Tensor. Specifies the intercept. Datatype support float32, float16, bfloat16. Format support ND. Same shape as gamma.

## Outputs

Three output, including:
- dx: A Tensor. x factor grad. Datatype is the same as the input Datatype. Format support ND.
- dgamma: A Tensor. scale factor grad. Datatype is the same as the input Datatype. Format support ND.
- dbeta: A Tensor. offset factor grad. Datatype is the same as the input Datatype. Format support ND.

## Attributes

- num_groups: Int. Number specifying the number of group.
- data_format: An optional String, Defaults to NCHW.
- swish_scale: An optional float. Defaults to "1.0".
- dgamma_is_require: An optional bool, controls whether to return weight.grad. Defaults to true.
- dbeta_is_require: An optional bool, controls whether to return beta.grad. Defaults to true.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: bfloat16,float16,float32
- input1 mean: bfloat16,float16,float32
- input2 rstd: bfloat16,float16,float32
- input3 x: bfloat16,float16,float32
- input4 gamma: bfloat16,float16,float32
- input5 beta: bfloat16,float16,float32
- output0 dx: bfloat16,float16,float32
- output1 dgamma: bfloat16,float16,float32
- output2 dbeta: bfloat16,float16,float32

## Third-party framework compatibility

- Compatible with the backward of PyTorch operator GroupNorm and Swish.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
