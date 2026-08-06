# AsinhGrad

```c
REG_OP(AsinhGrad)
  .INPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
  .INPUT(dy, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
  .OUTPUT(z, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
  .OP_END_FACTORY_REG(AsinhGrad)
```

## Brief

Computes gradients for Asinh operation. Support broadcasting operations.

## Inputs

- y: A tensor. Must be one of the following types: bfloat16, float16, float32.
- dy: A tensor of the same dtype as "y", y and dy must satisfy the broadcasting relationship.

## Outputs

z: A tensor. Has the same dtype as "y"，the shape conforms to the relationship after the input undergoes broadcasting.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y: float16,float32
- input1 dy: float16,float32
- output0 z: float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator AsinhGrad.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
