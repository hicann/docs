# FIFOQueue

```c
REG_OP(FIFOQueue)
    .OUTPUT(handle, TensorType({DT_RESOURCE}))
    .REQUIRED_ATTR(component_types, ListType)
    .ATTR(shapes, ListListInt, {})
    .ATTR(capacity, Int, -1)
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .OP_END_FACTORY_REG(FIFOQueue)
```

## Brief

A queue that produces elements in first-in first-out order. 

## Outputs

handle:A Tensor of type mutable resource. The handle to a queue. 

## Attributes

- component_types: A list of DType objects. The length of component_types
must equal the number of tensors in each queue element.
- shapes:An optional attribute. A list of fully-defined TensorShape objects with the
same length as dtypes, or None.
- capacity:An optional int. The upper bound on the number of elements that may
be stored in this queue. default vaule is -1.
- container: An optional string. Defaults to "". If non-empty, this queue
is placed in the given container. Otherwise, a default container is used.
- shared_name: An optional string. Defaults to "". If non-empty, this queue will be shared under
the given name across multiple sessions. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 handle: resource

## Third-party framework compatibility

Compatible with tensorflow FIFOQueue operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
