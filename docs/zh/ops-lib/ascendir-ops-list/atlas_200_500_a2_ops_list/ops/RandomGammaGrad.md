# RandomGammaGrad

```c
REG_OP(RandomGammaGrad)
    .INPUT(alpha, TensorType({DT_FLOAT, DT_DOUBLE}))
    .INPUT(sample, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(RandomGammaGrad)
```

## Brief

Computes the derivative of a Gamma random sample w.r.t. alpha. 

## Inputs

Inputs include:
- alpha: A Tensor. Must be one of the following types: float32, double.
- sample: A Tensor. Must have the same type as alpha.

## Outputs

y: A Tensor. Has the same type as alpha. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 alpha: double,float32
- input1 sample: double,float32
- output0 y: double,float32

## Attention Constraints

The implementation for RandomGammaGrad on Ascend uses AICPU, with bad performance.

## Third-party framework compatibility

- compatible with tensorflow RandomGammaGrad operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
