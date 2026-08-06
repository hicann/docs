# TensorListConcatLists

```c
REG_OP(TensorListConcatLists)
    .INPUT(input_a, TensorType({DT_VARIANT}))
    .INPUT(input_b, TensorType({DT_VARIANT}))
    .OUTPUT(output, TensorType({DT_VARIANT}))
    .ATTR(element_dtype, Type, DT_INT32)
    .OP_END_FACTORY_REG(TensorListConcatLists)
```

## Brief

Concat two tensor lists to a new tensor list. 

## Inputs

- input_a: The input tensor list A.
- input_b: The input tensor list B.

## Outputs

output: The output list. 

## Attributes

element_dtype: An optional attribute. The type of elements in the list. Defaults to DT_INT32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_a: variant
- input1 input_b: variant
- output0 output: variant

## Third-party framework compatibility.

Compatible with tensorflow TensorListConcatLists operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
