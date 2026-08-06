# NonZeroWithValue

```c
REG_OP(NonZeroWithValue)
    .INPUT(x, TensorType({DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT8, DT_UINT8, DT_INT16, \
           DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64, DT_BOOL}))
    .OUTPUT(value, TensorType({DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT8, DT_UINT8, DT_INT16, \
            DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64, DT_BOOL}))
    .OUTPUT(index, TensorType({DT_INT32}))
    .OUTPUT(count, TensorType({DT_INT32}))
    .ATTR(transpose, Bool, false)
    .ATTR(dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(NonZeroWithValue)
```

## Brief

Returns a tensor containing the indices of all non-zero elements of
input.

## Inputs

x: A Tensor. Must be one of the following types: float16, float32, int32,
int64, double, int8, uint8, int16, uint16, uint32, uint64, bool.
Supported format "ND". 

## Outputs

- value: A Tensor. Has the same type as "x" .
- index: A Tensor. The type is INT32, means index for input.
- count: A Scalar. The type is INT32, means count for non_zero ele in input.

## Attributes

- transpose: The output tensor will be transposed if true. Defaults to False.
- dtype: Must be one of the following types: int32. Defaults to `int32`.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float32
- output0 value: float32
- output1 index: int32
- output2 count: int32

## Third-party framework compatibility

Compatible with the PyTorch operator NonZeroWithValue.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
