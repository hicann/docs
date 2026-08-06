# PaddingFIFOQueue

```c
REG_OP(PaddingFIFOQueue)
    .OUTPUT(handle, TensorType({DT_RESOURCE}))
    .REQUIRED_ATTR(component_types, ListType)
    .ATTR(shapes, ListListInt, {})
    .ATTR(capacity, Int, -1)
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .OP_END_FACTORY_REG(PaddingFIFOQueue)
```

## Brief

A queue that produces elements in first-in first-out order. 

## Outputs

handle: A Tensor of type DT_RESOURCE. 

## Attributes

- shapes: An optional list of shapes for each component of
a queue element. Defaults to {}. The length of this attr must be
either 0 or the same as the length of "component_types". Shapes of fixed
rank but variable size are allowed by setting any shape dimension to "-1".
In this case, the inputs' shape may vary along the given dimension,
and DequeueMany will pad the given dimension with zeros up to the maximum
shape of all elements in the given batch. If the length of this attr is "0",
different queue elements may have different ranks and shapes, but only one
element may be dequeued at a time.
- capacity: An optional int. Defaults to "-1". The upper bound on the number
of elements in this queue. Negative numbers mean no limit.
- container: An optional string. Defaults to "". If non-empty, this queue
is placed in the given container. Otherwise, a default container is used.
- shared_name: An optional string. Defaults to "". If non-empty, this queue
will be shared under the given name across multiple sessions.
- component_types: A list of DTypes that has length >= 1. The type of each
component in a tuple. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 handle: resource

## Attention Constraints

PaddingFIFOQueue runs on the Ascend AI CPU, which delivers poor performance.

## Third-party framework compatibility

Compatible with the TensorFlow operator PaddingFIFOQueue.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
