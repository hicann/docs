# StopGradient

```c
REG_OP(StopGradient)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .OP_END_FACTORY_REG(StopGradient)
```

## Brief

Stops gradient computation. None is returned for the node where the gradient computation is stopped.

## Inputs

x: A tensor. 

## Outputs

y: The input tensor. 

## Third-party framework compatibility

Compatible with the TensorFlow operator StopGradient.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
