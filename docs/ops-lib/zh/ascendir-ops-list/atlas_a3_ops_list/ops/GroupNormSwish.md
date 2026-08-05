# GroupNormSwish

```c
REG_OP(GroupNormSwish)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .INPUT(gamma, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .INPUT(beta, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(mean, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(rstd, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .REQUIRED_ATTR(num_groups, Int)
    .ATTR(data_format, String, "NCHW")
    .ATTR(eps, Float, 0.00001f)
    .ATTR(activate_swish, Bool, true)
    .ATTR(swish_scale, Float, 1.0)
    .OP_END_FACTORY_REG(GroupNormSwish)
```

## Brief

Performs group normalization and swish. 

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
- rstd: A Tensor of type bfloat16/float16/float32.
Must be 1D. Specifies the rstd of "x". 

## Attributes

- num_groups: An required int32/int64, specifying the number of group.
- eps: An optional float32, specifying the small value added to the
denominator for numerical stability. Defaults to "0.00001".
- data_format: An optional String, Defaults to NCHW.
- activate_swish: An optional bool.  Defaults to "true".
- swish_scale: An optional float.  Defaults to "1".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 gamma: bfloat16,float16,float32
- input2 beta: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
- output1 mean: bfloat16,float16,float32
- output2 rstd: bfloat16,float16,float32

## Third-party framework compatibility

- Compatible with the PyTorch operator GroupNorm and Swish.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
