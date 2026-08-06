# SoftplusGrad

```c
REG_OP(SoftplusGrad)
    .INPUT(gradients, TensorType({FloatingDataType, DT_BF16}))
    .INPUT(features, TensorType({FloatingDataType, DT_BF16}))
    .OUTPUT(backprops, TensorType({FloatingDataType, DT_BF16}))
    .OP_END_FACTORY_REG(SoftplusGrad)
```

## Brief

Computes softplus gradients for a softplus operation .

## Inputs

Two inputs:
- gradients: A ND Tensor of type bfloat16, float16 or float32.
- features: A ND Tensor of type bfloat16, float16 or float32.

## Outputs

backprops: A Tensor. Has the same type and format as input "gradients" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 gradients: bfloat16,float16,float32
- input1 features: bfloat16,float16,float32
- output0 backprops: bfloat16,float16,float32
### AI CPU
- input0 gradients: double,float16,float32
- input1 features: double,float16,float32
- output0 backprops: double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator SoftplusGrad.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
