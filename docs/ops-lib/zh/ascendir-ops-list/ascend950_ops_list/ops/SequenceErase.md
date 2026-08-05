# SequenceErase

```c
REG_OP(SequenceErase)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .OPTIONAL_INPUT(index, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(handle_y, TensorType({DT_RESOURCE}))
    .OP_END_FACTORY_REG(SequenceErase)
```

## Brief

ouputs a tensor sequence that remove the tensor at 'position' from input_sequence. 

## Inputs

- handle: the handle of sequence.
- index: position of the tensor in the sequence. negative value means
counting position from back, accepted range in [-n, n - 1],
where n is the number of tensors in sequence,
it must be a scalar(tensor of empty shape), Must be one of the following types: int32, int64, it is scalar. 

## Outputs

- handle_y: the handle of the sequence that has the tensor
at the specified position removed. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- output0 handle_y: resource


---

[Back to Operator Specifications (Ascend950)](../README.md)
