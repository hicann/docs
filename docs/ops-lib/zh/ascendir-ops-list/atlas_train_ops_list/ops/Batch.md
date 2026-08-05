# Batch

```c
REG_OP(Batch)
  .DYNAMIC_INPUT(x_tensors, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, \
      DT_INT16, DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, DT_DOUBLE}))
  .DYNAMIC_OUTPUT(y_tensors, TensorType({DT_INT8, DT_UINT8, DT_INT16, \
      DT_UINT16, DT_INT32, DT_INT64, DT_FLOAT, DT_FLOAT16, DT_DOUBLE, DT_BOOL}))
  .OUTPUT(y_index, TensorType({ DT_INT64 }))
  .OUTPUT(y_id, TensorType({ DT_INT64 }))
  .REQUIRED_ATTR(num_batch_threads, Int)
  .REQUIRED_ATTR(max_batch_size, Int)
  .ATTR(max_enqueued_batches, Int, 10)
  .REQUIRED_ATTR(batch_timeout_micros, Int)
  .ATTR(allowed_batch_sizes, ListInt, {})
  .REQUIRED_ATTR(grad_timeout_micros, Int)
  .ATTR(container, String, "")
  .ATTR(shared_name, String, "")
  .ATTR(batching_queue, String, "")
  .OP_END_FACTORY_REG(Batch)
```

## Brief

Creates batches of tensors in "x_tensors" .   

## Inputs

Input "x_tensors" is a list or a dictionary of tensors.
x_tensors: The list or dictionary of tensors to enqueue.
It's a dynamic input. Must be one of the following types:
float16, float32, int8, int16, uint16, uint8, int32, int64, bool, double.  

## Outputs

- y_index: A Tensor. The index of a BatchTensor. Must be in row-major order.
- y_id: A Tensor. The ID of a BatchTensor. Must be in row-major order.
- y_tensors: A list or dictionary of tensors with
the same types as "x_tensors" .  It's a dynamic output.  

## Attributes

- num_batch_threads: An optional int. The number of threads enqueuing "x_tensors".
The batching will be nondeterministic if "num_batch_threads" > 1.
- max_batch_size: An optional int. The maximum batch size pulled from the queue.
- max_enqueued_batches: An optional int. Defaults to 10. The maximum number of batches pulled from the queue.
- batch_timeout_micros: The batch processing timeout, in microseconds.
- allowed_batch_sizes: An optional int list. The allowed batch size pulled from the queue.
- grad_timeout_micros: The gradient batch processing timeout,
in microseconds.
- container: An optional string. Defaults to "". If non-empty, this queue is placed in the given container.
Otherwise, a default container is used.
- shared_name: An optional string. Defaults to "". If set, this queue will be shared under the given name
across multiple sessions.
- batching_queue: An optional string. Defaults to "". The queue resource container.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output1 y_index: int64
- output2 y_id: int64

## Attention Constraints

Batch runs on the Ascend AI CPU, which delivers poor performance.   

## Third-party framework compatibility

Compatible with the TensorFlow operator Batch.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
