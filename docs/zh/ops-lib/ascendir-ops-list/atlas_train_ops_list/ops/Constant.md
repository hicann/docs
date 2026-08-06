# Constant

```c
REG_OP(Constant)
    .OUTPUT(y, TensorType::ALL())
    .ATTR(value, Tensor, Tensor())
    .OP_END_FACTORY_REG(Constant)
```

## Brief

Creates a constant tensor for training. 

## Outputs

y: The constant tensor. 

## Attributes

value: Required. The value and type of the resulting tensor, and no restrictions on type. 

## Third-party framework compatibility

Compatible with the TensorFlow operator Const.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
