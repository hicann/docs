# LeakyReluGrad

```c
REG_OP(LeakyReluGrad)
    .INPUT(gradients, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .INPUT(features, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .ATTR(negative_slope, Float, 0.0)
    .OUTPUT(backprops, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .OP_END_FACTORY_REG(LeakyReluGrad)
```

## Brief

Computes the output as gradients if features > 0 and negative_slope * gradients if features <= 0. 
Gradients/features support broadcasting operations. 

## Inputs

Two inputs, including:
- gradients: A tensor. Must be one of the following types: bfloat16, float16, float32, double. The backpropagated gradients to the corresponding LeakyRelu operation.
- features: A tensor. Has the same type as "gradients". The features passed as input to the corresponding LeakyRelu operation.

## Outputs

backprops: A tensor. Has the same type as "gradients". 

## Attributes

negative_slope: An optional float32. Negative Slope. Defaults to "0.0". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 gradients: bfloat16,float16,float32
- input1 features: bfloat16,float16,float32
- output0 backprops: bfloat16,float16,float32
### AI CPU
- input0 gradients: bfloat16,double,float16,float32
- input1 features: bfloat16,double,float16,float32
- output0 backprops: bfloat16,double,float16,float32

## Attention Constraints

The corresponding LeakyRelu operator needs to be called before using this operator on the network. 

## Third-party framework compatibility

- Compatible with the TensorFlow operator LeakyReluGrad.
- Compatible with the Pytorch operator leaky_relu_backward.


---

[Back to Operator Specifications (Ascend950)](../README.md)
