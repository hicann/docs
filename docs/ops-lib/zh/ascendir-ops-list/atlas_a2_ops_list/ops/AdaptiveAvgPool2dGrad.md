# AdaptiveAvgPool2dGrad

```c
REG_OP(AdaptiveAvgPool2dGrad)
    .INPUT(input_grad, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(output_grad, TensorType({DT_FLOAT, DT_FLOAT16}))
    .REQUIRED_ATTR(orig_input_shape, ListInt)
    .OP_END_FACTORY_REG(AdaptiveAvgPool2dGrad)
```

## Brief

Compute gradients of adaptive averagev2 pooling function.

## Inputs

- input_grad: A Tensor. Must be one of the following data types:
float16, float32.

## Outputs

- output_grad: A tensor with the same type as "input_grad".

## Attributes

- orig_input_shape: A required tuple or list of type int32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 input_grad: float16,float32
- output0 output_grad: float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator AdaptiveAvgPool2dGrad.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
