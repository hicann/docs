# Unbatch

```c
REG_OP(Unbatch)
  .INPUT(x_tensor, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, \
      DT_INT32, DT_INT64, DT_BOOL, DT_FLOAT, DT_DOUBLE, DT_FLOAT16, \
      DT_COMPLEX64, DT_COMPLEX128}))
  .INPUT(index, TensorType({DT_INT64}))
  .INPUT(id, TensorType({DT_INT64}))
  .OUTPUT(y_tensor, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, \
      DT_INT32, DT_INT64, DT_BOOL, DT_FLOAT, DT_DOUBLE, DT_FLOAT16, \
      DT_COMPLEX64, DT_COMPLEX128}))
  .REQUIRED_ATTR(timeout_micros, Int)
  .ATTR(container, String, "")
  .ATTR(shared_name, String, "")
  .OP_END_FACTORY_REG(Unbatch)
```

## Brief

Reverses the operation of Batch for a single output Tensor .   

## Inputs

Input "x_tensors" is a list or a dictionary of tensors.
- x_tensors: The list or dictionary of tensors to enqueue.
- index: The matching "batch_index" obtained from Batch.
- id: The "id" scalar emitted by Batch .

## Outputs

y_tensor: A list or dictionary of tensors with the same types as "x_tensors" .   

## Attributes

- timeout_micros: The unbatch processing timeout, in microseconds.
- container: An optional string. If non-empty, this queue is placed in the given container.
Otherwise, a default container is used. Defaults to "".
- shared_name: An optional string. If set, this queue will be shared under the given name
across multiple sessions. Defaults to "".   

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x_tensor: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 index: int64
- input2 id: int64
- output0 y_tensor: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Attention Constraints

Unbatch runs on the Ascend AI CPU, which delivers poor performance.   

## Third-party framework compatibility

Compatible with the TensorFlow operator Unbatch.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
