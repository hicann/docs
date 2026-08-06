# DeleteSeedGenerator

```c
REG_OP(DeleteSeedGenerator)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .INPUT(deleter, TensorType({DT_VARIANT}))
    .OP_END_FACTORY_REG(DeleteSeedGenerator)
```

## Brief

DeleteSeedGenerator. 

## Inputs

- handle:   A Tensor of type resource.
- deleter: A Tensor of type variant.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- input1 deleter: variant

## Third-party framework compatibility

Compatible with TensorFlow DeleteSeedGenerator operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
