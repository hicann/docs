# MultinomialAliasSetup

```c
REG_OP(MultinomialAliasSetup)
    .INPUT(probs, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(j, TensorType({DT_INT64}))
    .OUTPUT(q, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(MultinomialAliasSetup)
```

## Brief

Prepares for MultinomialAliasDraw to create a multinomial distribution. 

## Inputs

Inputs include:
- probs: A Tensor. Must be one of the following types: float, double.
1-D Tensor with shape [num_classes]. 

## Outputs

j: A Tensor. Must be one of the following types: int64.
1-D Tensor with shape [num_classes].
q: A Tensor. Must be one of the following types: float, double.
1-D Tensor with shape [num_classes]. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 j: int64
- output1 q: double,float32

## Attention Constraints

The implementation for MultinomialAliasSetup on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with torch _multinomial_alias_setup operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
