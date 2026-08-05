# SequenceAt

```c
REG_OP(SequenceAt)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .INPUT(index, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_INT8, DT_INT16, \
        DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BOOL, DT_COMPLEX64, \
        DT_COMPLEX128}))
    .OP_END_FACTORY_REG(SequenceAt)
```

## Brief

ouputs a tensor copy from the tensor at 'position' in input_sequence. 

## Inputs

- handle: the handle of sequence.
- index: position of the tensor in the sequence. negative value means
counting position from back, accepted range in [-n, n - 1],
where n is the number of tensors in sequence,
it must be a scalar(tensor of empty shape), it is scalar. 

## Outputs

- y: output tensor at the specified position in the input sequence.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- input1 index: int32,int64
- output0 y: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
