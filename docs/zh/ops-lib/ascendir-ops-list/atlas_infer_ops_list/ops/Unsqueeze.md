# Unsqueeze

```c
REG_OP(Unsqueeze)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .ATTR(axes, ListInt, {})
    .OP_END_FACTORY_REG(Unsqueeze)
```

## Brief

Inserts a dimension of 1 into a tensor's shape. Only the tensor shape is changed, without changing the data. 

## Inputs

x: Original tensor. All data types are supported. 

## Outputs

y: Reshape tensor with same data as input. The same type as input x. 

## Attributes

axes: List of ints indicating the dimensions to be inserted. Defaults to []. 

## Third-party framework compatibility

Compatible with the Onnx operator Unsqueeze.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
