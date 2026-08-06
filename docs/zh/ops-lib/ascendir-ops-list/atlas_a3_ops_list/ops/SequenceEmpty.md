# SequenceEmpty

```c
REG_OP(SequenceEmpty)
    .OUTPUT(handle, TensorType({DT_RESOURCE}))
    .ATTR(dtype, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(SequenceEmpty)
```

## Brief

construct an empty tensor sequence, with given data type. 

## Outputs

- handle: empty sequence.

## Attributes

- dtype: the data type of the tensors in the output sequence,
the default value is float. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 handle: resource


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
