# TensorArray

```c
REG_OP(TensorArray)
    .INPUT(size, TensorType({DT_INT32}))
    .OUTPUT(handle, TensorType({DT_RESOURCE}))
    .OUTPUT(flow, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(dtype, Type)
    .ATTR(element_shape, ListInt, ge::UNKNOWN_RANK)
    .ATTR(dynamic_size, Bool, false)
    .ATTR(clear_after_read, Bool, true)
    .ATTR(identical_element_shapes, Bool, false)
    .ATTR(tensor_array_name, String, "")
    .OP_END_FACTORY_REG(TensorArray)
```

## Brief

Class wrapping dynamic-sized, per-time-step, write-once Tensor arrays. 

## Inputs

The input size must be type int32. Inputs include:
- size: int32 scalar Tensor: the size of the TensorArray. Required if
handle is not provided. 

## Outputs

- handle: The handle to the TensorArray.
- flow: A scalar used to control gradient flow.

## Attributes

- dtype: The data type of this TensorArray.
- element_shape: An optional attribute. The TensorShape of elements in this TensorArray.
- dynamic_size: An optional bool. A boolean that determines whether writes to the
TensorArray are allowed to grow the size. Default is false.
- clear_after_read: An optional bool. Default is true. If true, clear
TensorArray values
after reading them. This disables read-many semantics, but allows early
release of memory.
- identical_element_shapes: An optional bool. Default is false. If true, then all elements
in the TensorArray will be expected to have have identical shapes.
- tensor_array_name: An optional string, the name of the TensorArray. Default is "".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 size: int32
- output0 handle: resource
- output1 flow: float32

## Third-party framework compatibility

Compatible with tensorflow TensorArray operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
