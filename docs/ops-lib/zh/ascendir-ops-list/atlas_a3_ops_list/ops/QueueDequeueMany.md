# QueueDequeueMany

```c
REG_OP(QueueDequeueMany)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .INPUT(n, TensorType({DT_INT32}))
    .DYNAMIC_OUTPUT(components, TensorType({DT_FLOAT, DT_FLOAT16, \
        DT_INT8, DT_INT16, DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, \
        DT_UINT32, DT_UINT64, DT_BOOL, DT_DOUBLE, DT_RESOURCE, \
        DT_STRING, DT_COMPLEX64, DT_COMPLEX128, DT_QINT16, DT_QUINT16, \
        DT_QINT8, DT_QUINT8, DT_QINT32}))
    .ATTR(timeout_ms, Int, -1)
    .REQUIRED_ATTR(component_types, ListType)
    .OP_END_FACTORY_REG(QueueDequeueMany)
```

## Brief

Dequeues n tuples of one or more tensors from the given queue. 

## Inputs

The input handle must have the resource type. Inputs include:
- handle:A Tensor of type mutable resource. The handle to a queue.
- n: A Tensor of type int32. The number of tuples to dequeue.

## Outputs

components:A list of Tensor objects of type component_types. Must be one of the following types: float32, float16, int8,
int16, uint16, uint8, int32, int64, uint32, uint64, bool, double, resource, string, complex64, complex128, qint16, quint16, qint8, quint8, qint32. It's a dynamic output. 

## Attributes

- timeout_ms: An optional int. Defaults to -1. If the queue has fewer than
n elements, this operation will block for up to timeout_ms milliseconds.
Note: This option is not supported yet.
- component_types: A list of DTypes that has length >= 1. The type of each
component in a tuple. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- input1 n: int32

## Third-party framework compatibility

Compatible with tensorflow QueueDequeueMany operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
