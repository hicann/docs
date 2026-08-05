# SoftsignGrad

```c
REG_OP(SoftsignGrad)
    .INPUT(gradients, TensorType({FloatingDataType, DT_BF16}))
    .INPUT(features, TensorType({FloatingDataType, DT_BF16}))
    .OUTPUT(output, TensorType({FloatingDataType, DT_BF16}))
    .OP_END_FACTORY_REG(SoftsignGrad)
```

## Brief

Computes softsignGrad: gradients / (1 + abs(features)) ** 2 .

## Inputs

Two inputs, including:
- gradients: A Tensor.Must be one of the following types: bfloat16, float16, float32.
- features: A Tensor of the same type and shape as "gradients".

## Outputs

output:A Tensor. Has the same type as "gradients".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 gradients: float16,float32
- input1 features: float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator SoftsignGrad.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
