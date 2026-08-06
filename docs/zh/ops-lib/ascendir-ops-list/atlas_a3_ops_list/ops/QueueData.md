# QueueData

```c
REG_OP(QueueData)
    .OUTPUT(y, TensorType({DT_UINT8}))
    .ATTR(index, Int, 0)
    .ATTR(queue_name, String, "")
    .ATTR(output_types, ListType, {})
    .ATTR(output_shapes, ListListInt, {{}, {}})
    .OP_END_FACTORY_REG(QueueData)
```

## Brief

Queue data for other operators. 

## Outputs

y: A DT_UINT8 tensor. 

## Attributes

- index: Index of the input tensor.The data type must be int32 or int64.
Assume that net has three data nodes, one should be set 0, another should
be set 1, and the left should be set 2.
- queue_name: An optional string that indicates the queue name. Defaults to "".
- output_types: An optional type list that indicates the data types of outputs data.
- output_shapes: An optional int list list that indicates the list shapes of outputs data.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
