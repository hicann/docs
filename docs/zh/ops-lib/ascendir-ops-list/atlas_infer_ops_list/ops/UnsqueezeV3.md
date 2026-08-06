# UnsqueezeV3

```c
REG_OP(UnsqueezeV3)
    .INPUT(x, TensorType::ALL())
    .INPUT(axes, TensorType({DT_INT64}))
    .OUTPUT(y, TensorType::ALL())
    .OP_END_FACTORY_REG(UnsqueezeV3)
```

## Brief

Inserts a dimension of 1 into a tensor's shape. Only the tensor shape
is changed, but the data is not changed. 

## Inputs

x: A tensor. All data types are supported. 
axes: A list of int64, which indicates the dimensions to be inserted. 

## Outputs

y: Reshape tensor with same data as input. The same type as input x. 

## Third-party framework compatibility

Compatible with the Onnx operator Unsqueeze in V3. 


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
