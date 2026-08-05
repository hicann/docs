# SqueezeV3

```c
REG_OP(SqueezeV3)
    .INPUT(x, TensorType::ALL())
    .OPTIONAL_INPUT(axes, TensorType({DT_INT64}))
    .OUTPUT(y, TensorType::ALL())
    .OP_END_FACTORY_REG(SqueezeV3)
```

## Brief

Removes dimensions of size 1 from the shape of a tensor according to axes. 

## Inputs

x: A tensor. All data types are supported. 
axes: An optional list of int64. Defaults to []. If not specified, squeezes all
dimensions of size 1. If specified, only squeezes the dimensions listed. It is
an error to squeeze a dimension that is not 1. 

## Outputs

y: Reshape tensor with same data as input. The same type as input x. 

## Third-party framework compatibility

Compatible with the onnx operator Squeeze in V13. 


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
