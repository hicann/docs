# LogSigmoidGrad

```c
REG_OP(LogSigmoidGrad)
    .INPUT(grads, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(features, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(backprops, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(LogSigmoidGrad)
```

## Brief

Calculate the gradient of log simoid.

## Inputs

Two inputs, including:
- grads: A tensor, gradient of previous layer. Must be one of the following types:
      float16, float32, bfloat16. 
- features: A tensor with the same type as 'grads', input of log sigmoid.

## Outputs

One output, including:
- backprops: A tensor with the same type and shape as 'grads'.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: float16,float32
- input1 features: float16,float32
- output0 backprops: float16,float32

## Attention Constraints

LogSigmoidGrad supports broadcasting.

## Third-party framework compatibility

Compatible with the Pytorch operator LogSigmoidBackward. 


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
