# UnbatchGrad

```c
REG_OP(UnbatchGrad)
  .INPUT(x_input, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, \
      DT_INT32, DT_INT64, DT_BOOL, DT_FLOAT, DT_DOUBLE, DT_FLOAT16, \
      DT_COMPLEX64, DT_COMPLEX128}))
  .INPUT(index, TensorType({DT_INT64}))
  .INPUT(grad, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, \
      DT_INT32, DT_INT64, DT_BOOL, DT_FLOAT, DT_DOUBLE, DT_FLOAT16, \
      DT_COMPLEX64, DT_COMPLEX128}))
  .INPUT(id, TensorType({DT_INT64}))
  .OUTPUT(y_grad, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, \
      DT_INT32, DT_INT64, DT_BOOL, DT_FLOAT, DT_DOUBLE, DT_FLOAT16, \
      DT_COMPLEX64, DT_COMPLEX128}))
  .ATTR(container, String, "")
  .ATTR(shared_name, String, "")
  .OP_END_FACTORY_REG(UnbatchGrad)
```

## Brief

Acts like Batch but using the given "batch_index" index of batching
things as they become available .   

## Inputs

Input "x_input" is a list or a dictionary of tensors.
- x_input: The input to the Unbatch operation.
- index: The batch_index given to the Unbatch operation.
- id: The "id" scalar emitted by Batch.
- grad: The downstream gradient .

## Outputs

y_grad: The return value, either an empty tensor or the batched gradient .   

## Attributes

- container: An optional string. If non-empty, this queue is placed in the given container.
Otherwise, a default container is used. Defaults to "".
- shared_name: An optional string. If set, this queue will be shared under the given name
across multiple sessions. Defaults to "".   

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x_input: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 index: int64
- input2 grad: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input3 id: int64
- output0 y_grad: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Attention Constraints

UnbatchGrad runs on the Ascend AI CPU, which delivers poor performance.   

## Third-party framework compatibility

Compatible with the TensorFlow operator UnbatchGrad.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
