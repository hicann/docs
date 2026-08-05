# Const

```c
REG_OP(Const)
    .OUTPUT(y, TensorType::ALL())
    .ATTR(value, Tensor, Tensor())
    .OP_END_FACTORY_REG(Const)
```

## Brief

Creates a constant tensor from a tensor-like object. This operator is used for inference.
Operator Const has the same definition as operator Constant. 

## Outputs

y: A constant tensor. 

## Attributes

value: Required. The value and type of the resulting tensor, and no restrictions on type. 

## Third-party framework compatibility

Compatible with the TensorFlow operator Const.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
