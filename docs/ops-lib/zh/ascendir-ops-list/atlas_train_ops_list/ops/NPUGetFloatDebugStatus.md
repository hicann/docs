# NPUGetFloatDebugStatus

```c
REG_OP(NPUGetFloatDebugStatus)
    .OUTPUT(data, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(NPUGetFloatDebugStatus)
```

## Brief

Get the value of global workspace. 

## Outputs

data: A Tensor of type int32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- output0 data: int32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
