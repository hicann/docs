# QueueClose

```c
REG_OP(QueueClose)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .ATTR(cancel_pending_enqueues, Bool, false)
    .OP_END_FACTORY_REG(QueueClose)
```

## Brief

Closes the given queue. 

## Inputs

Including:
handle: A Tensor of type DT_RESOURCE. The handle to a queue. 

## Attributes

cancel_pending_enqueues: An optional bool. Defaults to "False".
If true, all pending enqueue requests that are blocked on
the given queue will be canceled. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource

## Attention Constraints

QueueClose runs on the Ascend AI CPU, which delivers poor performance.

## Third-party framework compatibility

Compatible with the TensorFlow operator QueueClose.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
