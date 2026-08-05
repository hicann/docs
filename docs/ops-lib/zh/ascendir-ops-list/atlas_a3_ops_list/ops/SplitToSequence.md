# SplitToSequence

```c
REG_OP(SplitToSequence)
    .INPUT(x, TensorType({DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_INT8, \
        DT_INT16, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BOOL, DT_COMPLEX64, \
        DT_COMPLEX128}))
    .OPTIONAL_INPUT(split, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(handle, TensorType({DT_RESOURCE}))
    .ATTR(axis, Int, 0)
    .ATTR(keepdims, Bool, true)
    .OP_END_FACTORY_REG(SplitToSequence)
```

## Brief

split a tensor into a sequence of tensors, along the specified axis,
length of the parts can be specified using argument 'split'. 

## Inputs

- x: the tensor to split. Must be one of the following types:
uint8, uint16, uint32, uint64, int8, int16, int32, int64, float16,
float, double, bool, complex64, complex128.
- split: length of each output, it cat be either a scalar or 1-D tensor,
all value must be >= 0. if split is a scalar, then input will be split into
equally sized chunks, last chunk will be smaller if input size along the given
axis is not divisible by split, otherwise the tensor is split into size(split)
chunks, with lengths of the parts on axis specified in split. in the scenario,
the sum of entries in split must be equal to the dimision size of input tensor
on axis. Must be one of the following types: int32, int64. It's a dynamic input. 

## Outputs

- handle: one or more outputs forming a sequence of tensor after spliting.

## Attributes

- axis: An optional int, which axis to split on, a negative value means counting dimensions from
the back, accepted range is [-rank, rank - 1]. Default is 0.
- keep_dims: An optional bool, whether to keep the split dimension or not. If true, which means we keep split
dimension,if input 'split' is specified, this attribute is ignored. Default is true.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 handle: resource


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
