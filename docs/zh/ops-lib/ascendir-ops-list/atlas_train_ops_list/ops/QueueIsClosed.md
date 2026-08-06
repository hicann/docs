# QueueIsClosed

```c
REG_OP(QueueIsClosed)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .OUTPUT(is_closed, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(QueueIsClosed)
```

## Brief

This operation returns true if the queue is closed and false if
the queue is open. 

## Inputs

The input handle must have the resource type. Inputs include:
handle:A Tensor of type resource. The handle to a queue. 

## Outputs

is_closed:A Tensor of type bool. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- output0 is_closed: bool

## Third-party framework compatibility

Compatible with tensorflow QueueIsClosed operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
