# PreventGradient

```c
REG_OP(PreventGradient)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .ATTR(message, String, "")
    .OP_END_FACTORY_REG(PreventGradient)
```

## Brief

Outputs its input tensor as is and triggers an error if a gradient is requested. 

## Inputs

x: A tensor. 

## Outputs

y: The input tensor. 

## Attributes

message: Will be printed in the error at the attempt to request a gradient. 

## Third-party framework compatibility

Compatible with the TensorFlow operator PreventGradient.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
