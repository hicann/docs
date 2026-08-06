# InstanceNorm

```c
REG_OP(InstanceNorm)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(gamma, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(beta, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(mean, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(variance, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(data_format, String, "NDHWC")
    .ATTR(epsilon, Float, 1e-6f)
    .OP_END_FACTORY_REG(InstanceNorm)
```

## Brief

InstanceNorm operator interface implementation.

## Inputs

Three inputs, including:
- x: A 4D or 5D Tensor. Support dtype: [float32, float16],
 support format: [NCHW, NHWC, NDHWC, NCDHW].
- gamma: A 4D or 5D Tensor. Support dtype: [float32, float16],
 support format: [NCHW, NHWC, NDHWC, NCDHW] and DHW=1.
- beta: A 4D or 5D Tensor. Support dtype: [float32, float16],
 support format: [NCHW, NHWC, NDHWC, NCDHW] and DHW=1.

## Outputs

Three outputs, including:
- y: A 4D or 5D Tensor. Support dtype: [float32, float16],
 support format: [NCHW, NHWC, NDHWC, NCDHW]. Has the same type as "x".
- mean: A 4D or 5D Tensor. Support dtype: [float32, float16],
 support format: [NCHW, NHWC, NDHWC, NCDHW] and DHW=1. Has the same type as "x".
- variance: A 4D or 5D Tensor. Support dtype: [float32, float16],
 support format: [NCHW, NHWC, NDHWC, NCDHW] and DHW=1. Has the same type as "x".

## Attributes

- data_format: An optional attribute. The type is string. Default to "NDHWC".
- epsilon: An optional attribute. The type is float. Default to 1e-6.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 gamma: float16,float32
- input2 beta: float16,float32
- output0 y: float16,float32
- output1 mean: float16,float32
- output2 variance: float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
