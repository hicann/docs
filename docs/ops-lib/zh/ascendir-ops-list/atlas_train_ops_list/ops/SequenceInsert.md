# SequenceInsert

```c
REG_OP(SequenceInsert)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .INPUT(value, TensorType({DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_INT8, \
        DT_INT16, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BOOL, DT_COMPLEX64, \
        DT_COMPLEX128}))
    .OPTIONAL_INPUT(index, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(handle_y, TensorType({DT_RESOURCE}))
    .OP_END_FACTORY_REG(SequenceInsert)
```

## Brief

ouputs a tensor sequence that insert tensor into sequence at 'position',
tensor must have the same data type as input_sequence. 

## Inputs

- handle: the handle of sequence.
- value: tensor to be inserted into the input sequence.
- index: position of the tensor in the sequence. negative value means
counting position from back, accepted range in [-n, n - 1],
where n is the number of tensors in sequence,
it must be a scalar(tensor of empty shape), Must be one of the following types:
uint8, uint16, uint32, uint64, int8, int16, int32, int64, float16, float, double, bool,
complex64, complex128, it is scalar. 

## Outputs

- handle_y: output sequence that contains the inserted tensor
at the given positon. Type is resource.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- input1 value: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 handle_y: resource


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
