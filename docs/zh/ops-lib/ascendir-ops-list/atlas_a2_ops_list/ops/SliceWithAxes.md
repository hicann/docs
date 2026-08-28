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

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 offsets: int32,int64
- input2 size: int32,int64
- output0 y: bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator Slice.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
