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

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 offsets: int32,int64
- input2 size: int32,int64
- output0 y: bfloat16,bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator Slice.


---

[Back to Operator Specifications (Ascend950)](../README.md)
