# TensorListElementShape

```c
REG_OP(TensorListElementShape)
    .INPUT(input_handle, TensorType({DT_VARIANT}))
    .OUTPUT(element_shape, TensorType({DT_INT32,DT_INT64}))
    .ATTR(shape_type, Type, DT_INT32)
    .OP_END_FACTORY_REG(TensorListElementShape)
```

## Brief

The shape of elements in the input tensor list. 

## Inputs

input_handle: The input list. 

## Outputs

element_shape:A shape compatible with that of elements in the list. 

## Attributes

shape_type: An optional attribute. The type of shape in the list. Defaults to DT_INT32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_handle: variant
- output0 element_shape: int32,int64

## Third-party framework compatibility.

Compatible with tensorflow TensorListElementShape operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
