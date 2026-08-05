# INInferV2

```c
REG_OP(INInferV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(gamma, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(beta, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(mean, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(variance, TensorType({DT_FLOAT}))
    .ATTR(epsilon, Float, 0.00001)
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(batch_mean, TensorType({DT_FLOAT}))
    .OUTPUT(batch_variance, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(INInferV2)
```

## Brief

Performs instance normalization for inference .

## Inputs

Five inputs, including:
- x: A Tensor of type float16 or float32.
- gamma: A optional Tensor of type float32, for the scaling gamma, with shape [N, C1, 1, 1, C0].
- beta: A optional Tensor of type float32, for the scaling beta, with the same shape of gamma.
- mean: A optional Tensor of type float32, for the mean, with the same shape of gamma.
- variance: A optional Tensor of type float32, for the variance, with the same shape of gamma.

## Outputs

- y: A Tensor of type float16 or float32 for the normalized "x".
- batch_mean: A Tensor of type float32 for the result mean.
- batch_variance: A Tensor of type float32 for the result variance .

## Attributes

epsilon: An optional float32, specifying the small value added to variance to avoid dividing by zero.
Defaults to "0.00001" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 gamma: float32
- input2 beta: float32
- input3 mean: float32
- input4 variance: float32
- output0 y: float16,float32
- output1 batch_mean: float32
- output2 batch_variance: float32

## Attention Constraints

For Atlas 200/300/500 Inference Product, the result accuracy fails to reach 0.001 due to the square root instruction.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
