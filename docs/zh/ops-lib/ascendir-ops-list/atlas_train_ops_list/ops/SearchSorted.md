# SearchSorted

```c
REG_OP(SearchSorted)
    .INPUT(sorted_sequence, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT16, DT_INT8,
                                DT_UINT8, DT_INT32, DT_INT64}))
    .INPUT(values, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT16, DT_INT8,
                                DT_UINT8, DT_INT32, DT_INT64}))
    .OPTIONAL_INPUT(sorter, TensorType({DT_INT64}))
    .OUTPUT(out, TensorType(DT_INT32, DT_INT64))
    .ATTR(dtype, Type, DT_INT64)
    .ATTR(right, Bool, false)
    .OP_END_FACTORY_REG(SearchSorted)
```

## Brief

insert the values into the sorted sequence and return the index. 

## Inputs

- sorted_sequence: A Tensor of {DT_FLOAT16,DT_FLOAT,DT_INT16,DT_INT8,DT_UINT8,DT_INT32,DT_INT64},
the values of the last dim are sorted by ascending order.
- values: the inserted Tensor. Must have the same type as input. only the last dim can be different from
the sorted_sequence.
- sorter:  if provided, a tensor matching the shape of the unsorted sorted_sequence containing a sequence of indices
that sort it in the ascending order on the innermost dimension  

## Outputs

- out: output tensor of the op, which is the same shape as input "values". Dtype is int32 or int64.

## Attributes

- dtype: An optional type. Default value is DT_INT64, only supports DT_INT64/DT_INT32.
- right: An optional bool. Default value is false, false means the inserted position aligns to the left side when
the sequence contains same value and the position candidates are not unique, while true means aligning to
the right side when in such situation. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 sorted_sequence: float16,float32,int8,int16,int32,int64,uint8
- input1 values: float16,float32,int8,int16,int32,int64,uint8
- output0 out: int32,int64

## Third-party framework compatibility

Compatible with pytorch1.8.1 searchsorted operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
