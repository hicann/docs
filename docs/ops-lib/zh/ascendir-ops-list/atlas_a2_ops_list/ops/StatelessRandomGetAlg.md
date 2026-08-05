# StatelessRandomGetAlg

```c
REG_OP(StatelessRandomGetAlg)
    .OUTPUT(alg, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(StatelessRandomGetAlg)
```

## Brief

Get the counter of the RNG algorithm. 

## Outputs

- alg: The RNG algorithm.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- output0 alg: int32

## Third-party framework compatibility

Compatible with TensorFlow StatelessRandomGetAlg operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
