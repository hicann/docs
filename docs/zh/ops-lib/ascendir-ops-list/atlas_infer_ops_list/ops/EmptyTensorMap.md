# EmptyTensorMap

```c
REG_OP(EmptyTensorMap)
    .OUTPUT(handle, TensorType({DT_VARIANT}))
    .OP_END_FACTORY_REG(EmptyTensorMap)
```

## Brief

Creates and returns an empty tensor map. 

## Outputs

handle: An empty tensor map. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 handle: variant

## Third-party framework compatibility.

Compatible with tensorflow EmptyTensorMap operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
