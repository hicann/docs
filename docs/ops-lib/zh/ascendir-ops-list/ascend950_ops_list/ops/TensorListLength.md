# TensorListLength

```c
REG_OP(TensorListLength)
    .INPUT(input_handle, TensorType({DT_VARIANT}))
    .OUTPUT(length, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(TensorListLength)
```

## Brief

The number of tensors in the input tensor list. 

## Inputs

input_handle: The input list. 

## Outputs

length:The number of tensors in the list. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_handle: variant
- output0 length: int32

## Third-party framework compatibility.

Compatible with tensorflow TensorListLength operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
