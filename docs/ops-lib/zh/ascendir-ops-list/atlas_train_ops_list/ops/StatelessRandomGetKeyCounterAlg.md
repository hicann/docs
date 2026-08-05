# StatelessRandomGetKeyCounterAlg

```c
REG_OP(StatelessRandomGetKeyCounterAlg)
    .INPUT(seed, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(key, TensorType({DT_UINT64}))
    .OUTPUT(counter, TensorType({DT_UINT64}))
    .OUTPUT(alg, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(StatelessRandomGetKeyCounterAlg)
```

## Brief

This op picks the best counter-based RNG algorithm based on device, and
scrambles a shape-[2] seed into a key and a counter, both needed by the
counter-based algorithm. 

## Inputs

- seed: 2 seeds (shape [2]).

## Outputs

- key: Key for the counter-based RNG algorithm.
- counter: Initial counter for the counter-based RNG algorithm.
- alg: The RNG algorithm.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 seed: int32,int64
- output0 key: uint64
- output1 counter: uint64
- output2 alg: int32

## Third-party framework compatibility

Compatible with TensorFlow StatelessRandomGetKeyCounterAlg operator.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
