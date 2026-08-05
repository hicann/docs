# PriorityQueue

```c
REG_OP(PriorityQueue)
    .OUTPUT(handle, TensorType({DT_RESOURCE}))
    .ATTR(component_types, ListType, {})
    .ATTR(shapes, ListListInt, {})
    .ATTR(capacity, Int, -1)
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .OP_END_FACTORY_REG(PriorityQueue)
```

## Brief

A queue that produces elements sorted by the first component value. 

## Outputs

handle: A Tensor of type DT_RESOURCE. 

## Attributes

- component_types: An optional list of tf.DTypes. Defaults to {}.
The type of each component in a value.
- shapes: A list of shapes for each component of a queue element.
The length of this attr must be either 0 or the same as the length of
"component_types". If the length of this attr is 0, the shapes of queue
elements are not constrained, and only one element may be dequeued at a time.
- container: An optional string. Defaults to "". If non-empty, this queue
is placed in the given container. Otherwise, a default container is used.
- capacity:An integer. Defaults to "-1". The upper bound on the number of elements that may be stored in this queue.
- shared_name: An optional string. Defaults to "". If non-empty, this
queue will be shared under the given name across multiple sessions. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 handle: resource

## Attention Constraints

PriorityQueue runs on the Ascend AI CPU, which delivers poor performance.

## Third-party framework compatibility

Compatible with the TensorFlow operator PriorityQueue.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
