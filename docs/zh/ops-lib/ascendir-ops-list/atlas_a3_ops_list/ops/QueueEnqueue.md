# QueueEnqueue

```c
REG_OP(QueueEnqueue)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .DYNAMIC_INPUT(components, TensorType({DT_FLOAT, DT_FLOAT16, \
        DT_INT8, DT_INT16, DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, \
        DT_UINT32, DT_UINT64, DT_BOOL, DT_DOUBLE, DT_RESOURCE, \
        DT_STRING, DT_COMPLEX64, DT_COMPLEX128, DT_QINT16, DT_QUINT16, \
        DT_QINT8, DT_QUINT8, DT_QINT32}))
    .ATTR(timeout_ms, Int, -1)
    .OP_END_FACTORY_REG(QueueEnqueue)
```

## Brief

Enqueues a tuple of one or more tensors in the given queue. 

## Inputs

The input handle must have the resource type. Inputs include:
- handle:A Tensor of type mutable resource. The handle to a queue.
- components: A list of Tensor objects. One or more tensors from which
the enqueued tensors should be taken. Must be one of the following types:
float32, float16, int8, int16, uint16, uint8, int32, int64, uint32, uint64,
bool, double, resource, string, complex64, complex128, qint16, quint16, qint8,
quint8, qint32. It's a dynamic input. 

## Attributes

timeout_ms: An optional int. Defaults to -1. If the queue is full, this
operation will block for up to timeout_ms milliseconds. Note: This option
is not supported yet. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource

## Third-party framework compatibility

Compatible with tensorflow QueueEnqueue operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
