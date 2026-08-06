# RnnGenMask

```c
REG_OP(RnnGenMask)
    .INPUT(seq_length, TensorType({DT_INT32}))
    .OUTPUT(seq_mask, TensorType({DT_FLOAT16}))
    .REQUIRED_ATTR(num_step, Int)
    .REQUIRED_ATTR(hidden_size, Int)
    .OP_END_FACTORY_REG(RnnGenMask)
```

## Brief

rnn_gen_mask

## Inputs

seq_length: A ND Tensor of type int32. Record the current length of each batch.

## Attributes

- num_step: A required int.
- hidden_size: A required int.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 seq_length: int32
- output0 seq_mask: float16

## Ouputs

y: A mutable Tensor of type float16, with the shape of [num_step, batch_size, hidden_size]. 


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
