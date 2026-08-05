# Dequeue

```c
REG_OP(Dequeue)
    .OPTIONAL_INPUT(queue_id, TensorType({DT_UINT32}))
    .OUTPUT(data, TensorType::RealNumberType())
    .REQUIRED_ATTR(output_type, Type)
    .REQUIRED_ATTR(output_shape, ListInt)
    .ATTR(queue_name, String, "")
    .OP_END_FACTORY_REG(Dequeue)
```

## Brief

dequeue data acording to queue_id and queue_name.

## Inputs

- queue_id:An Tensor of type uint32, queue id.

## Outputs

data: A Tensor of type RealNumberType, dequeue tensor. Must be one of the types:double, float32, float16,
int16, int32, int64, int8, uint16, uint32, uint64, uint8, bf16. 

## Attributes

- output_type: A required type. dequeue data type.
- output_shape: A required listint. dequeue data shape.
- queue_name: An optional string. Queue name.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
