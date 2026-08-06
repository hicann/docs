# INTrainingReduceGrad

```c
REG_OP(INTrainingReduceGrad)
    .INPUT(dy, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(variance, TensorType({DT_FLOAT}))
    .INPUT(mean, TensorType({DT_FLOAT}))
    .INPUT(res_gamma, TensorType({DT_FLOAT}))
    .INPUT(res_beta, TensorType({DT_FLOAT}))
    .INPUT(gamma, TensorType({DT_FLOAT}))
    .OUTPUT(pd_x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OP_END_FACTORY_REG(INTrainingReduceGrad)
```

## Brief

Performs the backpropagation of InstanceNorm. 

## Inputs

Seven inputs, including:
- dy: A 4D tensor of type float16 or float32, format [NCHW, NHWC].
- x: A 4D tensor of type float16 or float32, format [NCHW, NHWC].
- variance: A 4D tensor of type float32, for the variance of "x", format [NCHW, NHWC] and HW=1.
- mean: A 4D tensor of type float32, for the mean of "x", format [NCHW, NHWC] and HW=1.
- res_gamma: A 4D tensor of type float32, format [NCHW, NHWC] and HW=1.
- res_beta: A 4D tensor of type float32, format [NCHW, NHWC] and HW=1.
- gamma: A 4D tensor of type float32, format [NCHW, NHWC] and HW=1.

## Outputs

pd_x: A 4D tensor of type float16 or float32, for the offset of "x", format [NCHW, NHWC]. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: float16,float32
- input1 x: float16,float32
- input2 variance: float32
- input3 mean: float32
- input4 res_gamma: float32
- input5 res_beta: float32
- input6 gamma: float32
- output0 pd_x: float16,float32

## Attention Constraints

The preceding layer of this operator must be INTrainingUpdateGrad. 


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
