# MaskedSelect

```c
REG_OP(MaskedSelect)
    .INPUT(x, TensorType::BasicType())
    .INPUT(mask, TensorType({DT_BOOL}))
    .OUTPUT(y, TensorType::BasicType())
    .OP_END_FACTORY_REG(MaskedSelect)
```

## Brief

Choose the value of X with value according to mask.

## Inputs

two inputs, including:
- x: A tensor of type BasicType.
- mask: A tensor of type bool, true for selecting related number of x out, false for no selecting.

## Outputs

y: A tensor with the same type as x. 

## Attention Constraints

- The input tensors of x and mask must meet the broadcast relationship.
- The dimnum of y must be 1.

## Third-party framework compatibility

Compatible with the Numpy operator select.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
