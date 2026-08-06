# TensorListReserve

```c
REG_OP(TensorListReserve)
    .INPUT(element_shape, TensorType({DT_INT32,DT_INT64}))
    .INPUT(num_elements, TensorType({DT_INT32}))
    .OUTPUT(handle, TensorType({DT_VARIANT}))
    .ATTR(element_dtype, Type, DT_INT32)
    .ATTR(shape_type, Type, DT_INT32)
    .OP_END_FACTORY_REG(TensorListReserve)
```

## Brief

List of the given size with empty elements. 

## Inputs

- element_shape: A shape compatible with that of elements in the list.
- num_elements: The number of elements to reserve.

## Outputs

handle: An output tensor list . 

## Attributes

- element_dtype: An optional attribute. The type of elements in the list. Defaults to DT_INT32.
- shape_type: An optional attribute. The type of shape in the list. Defaults to DT_INT32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 element_shape: int32,int64
- input1 num_elements: int32
- output0 handle: variant

## Third-party framework compatibility.

Compatible with tensorflow TensorListReserve operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
