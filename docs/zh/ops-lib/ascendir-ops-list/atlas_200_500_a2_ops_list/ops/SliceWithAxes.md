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

Extracts a slice from a tensor.
      This operation extracts a slice of size "size" from a tensor "x"
      starting at the location specified by "offsets".

## Inputs

- x: A Tensor. Must be one of the following types:
bfloat16, float16, float32, double, int64, int32, uint8, uint16, uint32, uint64, int8,
int16, complex64, complex128, qint8, quint8, qint16, quint16, qint32. Format is ND.
- offsets: A Tensor of type int32 or int64. The starting location for the slice.
Format is ND.
- size: A Tensor of type int32 or int64. The tensor size for the slice.
Must be one of the following types: int32, int64. Format is ND. 

## Outputs

y: A Tensor. Has the same type as "x". The slice extracted from the tensor.
Format is ND. 

## Attributes

- axes: A listint attr. The axes for the slice.

## Third-party framework compatibility

Compatible with the TensorFlow operator Slice.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
