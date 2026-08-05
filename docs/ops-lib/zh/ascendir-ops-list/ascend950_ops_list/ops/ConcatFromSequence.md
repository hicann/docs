# ConcatFromSequence

```c
REG_OP(ConcatFromSequence)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .OUTPUT(y, TensorType({DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_INT8, \
        DT_INT16, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BOOL, DT_COMPLEX64, \
        DT_COMPLEX128}))
    .REQUIRED_ATTR(axis, Int)
    .ATTR(new_axis, Int, 0)
    .OP_END_FACTORY_REG(ConcatFromSequence)
```

## Brief

concatenate a sequence of tensors into a single tensor, all input tensors must
have the same shape, except for the dimension size of the axis to concatenate on. by default
new_axis is 0, the behavior is similar to numpy.concatenate. when new_axis is 1, the behavior
is similar to numpy.stack. 

## Inputs

- handle: sequence of tensors for concatenation.

## Outputs

- y: concatenated tensor. Must be one of the following types:
uint8, uint16, uint32, uint64, int8, int16, int32, int64, float16, float,
double, bool, complex64, complex128.

## Attributes

- axis: An optional int, which axis to concat on, accepted range in [-r, r - 1], where r is the rank of input
tensor, when new_axis is 1,accepted range is [-r - 1, r]
- new_axis: An optional int, insert and concatnate on a new axis or not. default 0 means do not insert new axis.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- output0 y: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64


---

[Back to Operator Specifications (Ascend950)](../README.md)
