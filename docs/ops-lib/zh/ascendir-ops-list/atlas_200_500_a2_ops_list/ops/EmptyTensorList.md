# EmptyTensorList

```c
REG_OP(EmptyTensorList)
    .INPUT(element_shape, TensorType({DT_INT32,DT_INT64}))
    .INPUT(max_num_elements, TensorType({DT_INT32}))
    .OUTPUT(handle, TensorType({DT_VARIANT}))
    .ATTR(element_dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(EmptyTensorList)
```

## Brief

Creates and returns an empty tensor list. 

## Inputs

- element_shape: A shape compatible with that of elements in the list.
- max_num_elements: The maximum number of elements.

## Outputs

handle: An empty tensor list . 

## Attributes

element_dtype: The type of elements in the list. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 element_shape: int32,int64
- input1 max_num_elements: int32
- output0 handle: variant

## Third-party framework compatibility.

Compatible with tensorflow EmptyTensorList operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
