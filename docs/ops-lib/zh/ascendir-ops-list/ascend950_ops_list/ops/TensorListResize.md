# TensorListResize

```c
REG_OP(TensorListResize)
    .INPUT(input_handle, TensorType({DT_VARIANT}))
    .INPUT(size, TensorType({DT_INT32}))
    .OUTPUT(output_handle, TensorType({DT_VARIANT}))
    .OP_END_FACTORY_REG(TensorListResize)
```

## Brief

Resizes the list. 

## Inputs

- input_handle: The input tensor list.
- size: size of the output list.

## Outputs

output_handle: The output tensor list. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_handle: variant
- input1 size: int32
- output0 output_handle: variant

## Third-party framework compatibility.

Compatible with tensorflow TensorListResize operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
