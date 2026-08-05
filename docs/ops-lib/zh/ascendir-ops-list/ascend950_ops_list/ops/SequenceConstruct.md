# SequenceConstruct

```c
REG_OP(SequenceConstruct)
    .DYNAMIC_INPUT(inputs, TensorType({DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_INT8, \
        DT_INT16, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BOOL, DT_COMPLEX64, \
        DT_COMPLEX128}))
    .OUTPUT(handle, TensorType({DT_RESOURCE}))
    .OP_END_FACTORY_REG(SequenceConstruct)
```

## Brief

constrct a tensor sequence cotaining 'input' tensors,
all tensors in 'inputs' must have the same data type. 

## Inputs

- inputs: A list of input tensor objects. Must be one of the following types:
uint8, uint16, uint32, uint64, int8, int16, int32, int64, float16, float, double,
bool, complex64, complex128. It's a dynamic input. 

## Outputs

- handle: Sequence enclosing the input tensors.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 handle: resource


---

[Back to Operator Specifications (Ascend950)](../README.md)
