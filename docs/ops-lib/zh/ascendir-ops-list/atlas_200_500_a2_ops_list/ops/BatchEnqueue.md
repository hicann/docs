# BatchEnqueue

```c
REG_OP(BatchEnqueue)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE, \
        DT_INT8, DT_INT32, DT_INT64, DT_UINT8, DT_UINT32, DT_UINT64}))
    .OPTIONAL_INPUT(queue_id, TensorType({DT_UINT32}))
    .OUTPUT(enqueue_count, TensorType({DT_INT32}))
    .ATTR(batch_size, Int, 8)
    .ATTR(queue_name, String, "")
    .ATTR(queue_depth, Int, 100)
    .ATTR(pad_mode, String, "REPLICATE")
    .OP_END_FACTORY_REG(BatchEnqueue)
```

## Brief

batch input x acording to attr batch_size and enqueue.

## Inputs

- x: A Tensor need to batch of type float16/float32/float64/int8/int32/int64/uint8/uint32/uint64.
- queue_id:A Tensor of type uint32, queue id.

## Outputs

enqueue_count: A Tensor of type int32, enqueue tensor number.

## Attributes

- batch_size: An optional int. Batch size. Defaults to 8.
- queue_name: An optional string. Queue name. Defaults to "".
- queue_depth: An optional int. Queue depth. Defaults to 100.
- pad_mode: An optional string from: '"REPLICATE", "ZERO"'. Defaults to
"REPLICATE". Pad mode.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 queue_id: uint32
- output0 enqueue_count: int32


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
