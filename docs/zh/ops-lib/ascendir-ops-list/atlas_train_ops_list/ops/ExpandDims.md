# ExpandDims

```c
REG_OP(ExpandDims)
    .INPUT(x, TensorType::ALL())
    .INPUT(axis, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType::ALL())
    .OP_END_FACTORY_REG(ExpandDims)
```

## Brief

Inserts a dimension of 1 into a tensor's shape. Only the tensor shape is changed, without changing the data. 

## Inputs

- x: A tensor.
- axis: The dimension index at which to expand.

## Outputs

y: A tensor with the same data as input, with an additional dimension inserted at the index specified by axis. 

## Third-party framework compatibility

Compatible with the TensorFlow operator ExpandDims.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
