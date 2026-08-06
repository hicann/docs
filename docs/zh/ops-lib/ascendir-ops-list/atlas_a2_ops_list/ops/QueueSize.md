# QueueSize

```c
REG_OP(QueueSize)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .OUTPUT(size, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(QueueSize)
```

## Brief

Computes the number of elements in the given queue. 

## Inputs

The input handle must have the resource type. Inputs include:
handle:A Tensor of type mutable resource. The handle to a queue. 

## Outputs

size:A Tensor of type int32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- output0 size: int32

## Third-party framework compatibility

Compatible with tensorflow QueueSize operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
