# Reshape

```c
REG_OP(Reshape)
    .INPUT(x, TensorType::ALL())
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType::ALL())
    .ATTR(axis, Int, 0)
    .ATTR(num_axes, Int, -1)
    .OP_END_FACTORY_REG(Reshape)
```

## Brief

Reshapes a tensor. Only the tensor shape is changed, without changing the data. 

## Inputs

- x: A tensor. All data types are supported.
- shape: A tensor. Must be one of the following types: int32, int64. Defines the shape of the output tensor.

## Outputs

y: A tensor. The same type as input x. 

## Attributes

- axis: An optional int32 or int64. The first dimension to reshape. Defaults to "0".
- num_axes: An optional int32 or int64. The extent of the reshape. Defaults to "-1".

## Attention Constraints

This operator cannot be directly called by the acllopExecute API. 

## Third-party framework compatibility

- Compatible with the TensorFlow operator Reshape.
- Compatible with the Caffe operator Reshape.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
