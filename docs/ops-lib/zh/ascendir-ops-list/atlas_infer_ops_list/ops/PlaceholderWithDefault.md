# PlaceholderWithDefault

```c
REG_OP(PlaceholderWithDefault)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .REQUIRED_ATTR(shape, ListInt)
    .OP_END_FACTORY_REG(PlaceholderWithDefault)
```

## Brief

Inserts a placeholder with default value for a tensor. 

## Inputs

x: A tensor. 

## Outputs

y: The created placeholder tensor. 

## Attributes

shape: tensor shape. 

## Third-party framework compatibility

Compatible with the TensorFlow operator PlaceholderWithDefault.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
