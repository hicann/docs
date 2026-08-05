# HardShrinkGrad

```c
REG_OP(HardShrinkGrad)
  .INPUT(gradients, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
  .INPUT(features, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
  .OUTPUT(backprops, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
  .ATTR(lambd, Float, 0.5)
  .OP_END_FACTORY_REG(HardShrinkGrad)
```

## Brief

Calculate the hard shrink grad function.
Computes the gradient for the HardShrink: if x > lambda or x < -lambda, x,otherwise 0

## Inputs

Two inputs, including:
- gradients: A tensor. Must be one of the following types:
    float16, float32, bfloat16. 
- features: A tensor. Must be one of the following types:
    float16, float32, bfloat16. 

## Outputs

backprops: A tensor with the same type and shape as 'features'. 

## Attributes

lambd: An optional float.Defaults to 0.5. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 gradients: bfloat16,float16,float32
- input1 features: bfloat16,float16,float32
- output0 backprops: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator Hardshrink_backward. 


---

[Back to Operator Specifications (Ascend950)](../README.md)
