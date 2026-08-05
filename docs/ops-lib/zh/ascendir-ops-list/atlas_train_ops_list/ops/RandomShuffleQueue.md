# RandomShuffleQueue

```c
REG_OP(RandomShuffleQueue)
    .OUTPUT(handle, TensorType({DT_RESOURCE}))
    .REQUIRED_ATTR(component_types, ListType)
    .ATTR(shapes, ListListInt, {})
    .ATTR(capacity, Int, -1)
    .ATTR(min_after_dequeue, Int, 0)
    .ATTR(seed, Int, 0)
    .ATTR(seed2, Int, 0)
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .OP_END_FACTORY_REG(RandomShuffleQueue)
```

## Brief

A queue implementation that dequeues elements in a random order. 

## Outputs

handle: A Tensor of type resource. The handle to a stack. 

## Attributes

- component_types:A list of fully-defined Tensortype objects with
the same length as shapes, or None.
- shapes: An optional attribute. A list of fully-defined TensorShape objects with
the same length as dtypes, or None.
- capacity: An optional int. The upper bound on the number of elements that may
be stored in this queue. Default is -1.
- min_after_dequeue: An optional int that described above. Default is 0.
- seed: An optional int. Used to create a random seed. Default is 0.
- seed2: An optional int. Used to create a random seed. Default is 0.
- container: An optional string. Defaults to "".
- shared_name: An optional string. Defaults to "".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 handle: resource

## Third-party framework compatibility

Compatible with tensorflow RandomShuffleQueue operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
