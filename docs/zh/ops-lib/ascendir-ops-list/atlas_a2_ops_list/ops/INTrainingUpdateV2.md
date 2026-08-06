# INTrainingUpdateV2

```c
REG_OP(INTrainingUpdateV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(sum, TensorType({DT_FLOAT}))
    .INPUT(square_sum, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(gamma, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(beta, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(mean, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(variance, TensorType({DT_FLOAT}))
    .ATTR(momentum, Float, 0.1)
    .ATTR(epsilon, Float, 0.00001)
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(batch_mean, TensorType({DT_FLOAT}))
    .OUTPUT(batch_variance, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(INTrainingUpdateV2)
```

## Brief

Performs update instance normalization. 

## Inputs

Seven inputs, including:
- x: A 4D tensor of type float16 or float32, format [NCHW, NHWC].
- sum: A 4D tensor of type float32 for the output of operator INTrainingReduceV2, format [NCHW, NHWC], and HW=1.
- square_sum: A 4D tensor of type float32 for the output of operator INTrainingReduceV2, format [NCHW, NHWC], and
HW=1.
- gamma: A 4D optional tensor of type float32, for the scaling gamma, format [NCHW, NHWC], and HW=1.
- beta: A 4D optional tensor of type float32, for the scaling beta, format [NCHW, NHWC], and HW=1.
- mean: A 4D optional tensor of type float32, for the updated mean, format [NCHW, NHWC], and HW=1.
- variance: A 4D optional tensor of type float32, for the updated variance, format [NCHW, NHWC], and HW=1.

## Outputs

Three outputs
- y: A 4D tensor of type float16 or float32, for normalized "x", format [NCHW, NHWC].
- batch_mean: A 4D tensor of type float32, for the updated mean, format [NCHW, NHWC], and HW=1.
- batch_variance: A 4D tensor of type float32, for the updated variance, format [NCHW, NHWC], and HW=1.

## Attributes

- momentum: A optional float32, specifying the momentum to update mean and var. default to 0.1.
- epsilon: A optional float32, specifying the small value added to variance to avoid dividing by zero. default to
0.00001. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 sum: float32
- input2 square_sum: float32
- input3 gamma: float32
- input4 beta: float32
- input5 mean: float32
- input6 variance: float32
- output0 y: float16,float32
- output1 batch_mean: float32
- output2 batch_variance: float32

## Attention Constraints

This operator is a InstanceNorm fusion operator for updating the moving averages for training.
This operator is used in conjunction with INTrainingReduceV2.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
