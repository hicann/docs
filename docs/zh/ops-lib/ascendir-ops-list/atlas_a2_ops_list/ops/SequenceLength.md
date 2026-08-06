# SequenceLength

```c
REG_OP(SequenceLength)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .OUTPUT(length, TensorType({DT_INT64}))
    .OP_END_FACTORY_REG(SequenceLength)
```

## Brief

produces a scalar(tensor of empty shape) containing the number
of tensors in input_sequence. 

## Inputs

- handle: the handle of sequence.

## Outputs

- length: length of input sequence, it must be a scalar (tensor of empty shape)

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- output0 length: int64


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
