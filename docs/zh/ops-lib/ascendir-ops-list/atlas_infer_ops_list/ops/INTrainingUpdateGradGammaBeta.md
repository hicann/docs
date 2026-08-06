# INTrainingUpdateGradGammaBeta

```c
REG_OP(INTrainingUpdateGradGammaBeta)
    .INPUT(res_gamma, TensorType({DT_FLOAT}))
    .INPUT(res_beta, TensorType({DT_FLOAT}))
    .OUTPUT(pd_gamma, TensorType({DT_FLOAT}))
    .OUTPUT(pd_beta, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(INTrainingUpdateGradGammaBeta)
```

## Brief

Performs the backpropagation of InstanceNorm. 

## Inputs

Two inputs, including:
- res_gamma: A 4D tensor of type float32,  format [NCHW, NHWC].
- res_beta: A 4D tensor of type float32, format [NCHW, NHWC].

## Outputs

- pd_gamma: A 4D tensor of type float32, format [NCHW, NHWC].
- pd_beta: A 4D tensor of type float32, format [NCHW, NHWC].

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 res_gamma: float32
- input1 res_beta: float32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
