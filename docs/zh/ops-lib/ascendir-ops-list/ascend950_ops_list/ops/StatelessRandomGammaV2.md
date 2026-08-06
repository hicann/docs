# StatelessRandomGammaV2

```c
REG_OP(StatelessRandomGammaV2)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(seed, TensorType({DT_INT32, DT_INT64}))
    .INPUT(alpha, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_DOUBLE}))
    .OP_END_FACTORY_REG(StatelessRandomGammaV2)
```

## Brief

Outputs deterministic pseudorandom random numbers from a gamma distribution. 

## Inputs

- shape: The shape of the output tensor.
- seed: 2 seeds (shape [2]).
- alpha: The concentration of the gamma distribution. Shape must match the rightmost dimensions of shape.

## Outputs

y: A Tensor. Has the same type as alpha. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 shape: int32,int64
- input1 seed: int32,int64
- input2 alpha: double,float16,float32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with TensorFlow StatelessRandomGammaV2 operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
