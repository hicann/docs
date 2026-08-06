# TensorArrayClose

```c
REG_OP(TensorArrayClose)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .OP_END_FACTORY_REG(TensorArrayClose)
```

## Brief

Delete the TensorArray from its resource container. 

## Inputs

The input handle must be type resource. Inputs include:
handle: A Tensor of type resource. The handle to a TensorArray
(output of TensorArray or TensorArrayGrad). 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource

## Third-party framework compatibility

Compatible with tensorflow TensorArrayClose operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
