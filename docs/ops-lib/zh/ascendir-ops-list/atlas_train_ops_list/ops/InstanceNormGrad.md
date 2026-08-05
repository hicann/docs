# InstanceNormGrad

```c
REG_OP(InstanceNormGrad)
    .INPUT(dy, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(variance, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(mean, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(gamma, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(pd_x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(pd_gamma, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(pd_beta, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(InstanceNormGrad)
```

## Brief

InstanceNormGrad operator interface implementation.

## Inputs

Five inputs, including:
- dy: Represents the input gradient tensor. Support dtype: float16, float32. Suppor shape 4D or 5D.
Support format: [NCHW, NHWC, NDHWC, NCDHW]. Has the same dtype, format and shape as "x".
- x: Represents the input tensor. Support dtype: float16, float32. Suppor shape 4D or 5D.
Support format: [NCHW, NHWC, NDHWC, NCDHW].
- variance: Represents the variance tensor. Support dtype: float16, float32. Suppor shape 4D or 5D.
Support format: [NCHW, NHWC, NDHWC, NCDHW] and DHW=1. Has the same dtype and format as "x".
The shapes of "variance" and "mean" are consistent, and the N and C axes are consistent with those of "x", and the other dimensions are 1.
- mean: Represents the mean tensor. Support dtype: float16, float32. Suppor shape 4D or 5D.
Support format: [NCHW, NHWC, NDHWC, NCDHW] and DHW=1. Has the same dtype and format as "x".
The shapes of "variance" and "mean" are consistent, and the N and C axes are consistent with those of "x", and the other dimensions are 1.
- gamma: Represents the optional weight parameter. Support dtype: float16, float32. Suppor shape 4D or 5D.
Support format: [NCHW, NHWC, NDHWC, NCDHW].  Has the same dtype as "x".
The C axis of "gamma" is consistent with that of "x", and the other dimensions are 1. 

## Outputs

Three outputs, including:
- pd_x: Represents the gradient tensor of the input tensor. Support dtype: float16, float32. Suppor shape 4D or 5D.
Support format: [NCHW, NHWC, NDHWC, NCDHW].  Has the same dtype, format and shape as "x".
- pd_gamma: Represents the gradient tensor of the weight parameter. Support dtype: float16, float32. Suppor shape 4D or 5D.
Support format: [NCHW, NHWC, NDHWC, NCDHW]. Has the same dtype and format as "x". Has the same shape as "gamma".
- pd_beta: Represents the gradient tensor of the bias parameter. Support dtype: float16, float32. Suppor shape 4D or 5D.
Support format: [NCHW, NHWC, NDHWC, NCDHW]. Has the same dtype and format as "x". Has the same shape as "gamma".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: float16,float32
- input1 x: float16,float32
- input2 variance: float16,float32
- input3 mean: float16,float32
- input4 gamma: float16,float32
- output0 pd_x: float16,float32
- output1 pd_gamma: float16,float32
- output2 pd_beta: float16,float32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
