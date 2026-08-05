# SliceWithAxes

```c
REG_OP(SliceWithAxes)
    .INPUT(x, TensorType::BasicType())
    .INPUT(offsets, TensorType::IndexNumberType())
    .INPUT(size, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType::BasicType())
    .REQUIRED_ATTR(axes, ListInt)
    .OP_END_FACTORY_REG(SliceWithAxes)
```

## Brief

Extracts a slice from a tensor along specified axes. 

## Inputs

- x: A tensor of BasicType.
- offsets: A 1D tensor of type int32 or int64. The start offsets for each axis.
- size: A 1D tensor of type int32 or int64. The sizes for each axis.

## Outputs

y: A tensor with the same type as x. 

## Attributes

axes: Required. List of axes along which to slice. 

## Third-party framework compatibility

Compatible with the TensorFlow operator Slice.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
