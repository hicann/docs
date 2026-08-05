# DummySeedGenerator

```c
REG_OP(DummySeedGenerator)
    .OUTPUT(handle, TensorType({ DT_RESOURCE }))
    .OP_END_FACTORY_REG(DummySeedGenerator)
```

## Brief

Create a placeholder handle to rewrite and pass
to use during the graph compilation phase. 

## Outputs

handle:Output random number . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 handle: resource


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
