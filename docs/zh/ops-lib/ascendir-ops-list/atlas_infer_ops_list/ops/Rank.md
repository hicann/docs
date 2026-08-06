# Rank

```c
REG_OP(Rank)
    .INPUT(x, TensorType::ALL())
    .OUTPUT(y, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(Rank)
```

## Brief

Returns an integer representing the rank of input tensor. The rank of a tensor is the number of indices required to uniquely select each element of the tensor, that is, the dimension size of the tensor. 

## Inputs

x: A Tensor of type float32, float16, int8, int16, uint16, uint8, int32, int64, uint32, uint64, bool, double, string. 

## Outputs

y: A tensor. The rank of input tensor. Type is int32. 

## Third-party framework compatibility

Compatible with the TensorFlow operator Rank.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
