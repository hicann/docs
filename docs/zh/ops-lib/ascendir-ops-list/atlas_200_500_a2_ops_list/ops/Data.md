# Data

```c
REG_OP(Data)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType::ALL())
    .ATTR(index, Int, 0)
    .OP_END_FACTORY_REG(Data)
```

## Brief

Input data for other operators. 

## Inputs

x: A tensor. 

## Outputs

y: A tensor. 

## Attributes

index: Index of the input tensor.The data type must be int32 or int64.
Assume that net has three data nodes, one should be set 0, another should
be set 1, and the left should be set 2. 

## Third-party framework compatibility

Compatible with the Caffe operator Data.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
