# EndOfSequence

```c
REG_OP(EndOfSequence)
    .INPUT(x, TensorType({DT_UINT8}))
    .OUTPUT(y, TensorType({DT_UINT8}))
    .OP_END_FACTORY_REG(EndOfSequence)
```

## Brief

End of sequence. 

## Inputs

x: A Tensor of type uint8. 

## Outputs

y: A Tensor. Has the same type as "x".


---

[Back to Operator Specifications (Ascend950)](../README.md)
