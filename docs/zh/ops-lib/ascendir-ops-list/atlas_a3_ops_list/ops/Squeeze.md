# Squeeze

```c
REG_OP(Squeeze)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .ATTR(axis, ListInt, {})
    .OP_END_FACTORY_REG(Squeeze)
```

## Brief

Removes dimensions of size 1 from the shape of a tensor. 

## Inputs

x: A tensor. All data types are supported. 

## Outputs

y: A tensor. The same type as input x. 

## Attributes

axis: An optional list of int32 or int64. Defaults to []. If not specified, squeezes all dimensions of size 1.
If specified, only squeezes the dimensions listed. It is an error to squeeze a dimension that is not 1. 

## Third-party framework compatibility

Compatible with the TensorFlow operator Squeeze.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
