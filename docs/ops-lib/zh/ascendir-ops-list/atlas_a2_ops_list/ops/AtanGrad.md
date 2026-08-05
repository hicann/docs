# AtanGrad

```c
REG_OP(AtanGrad)
  .INPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
  .INPUT(dy, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
  .OUTPUT(z, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
  .OP_END_FACTORY_REG(AtanGrad)
```

## Brief

Computes gradients for Atan operation. Support broadcasting operations.

## Inputs

- y: A tensor of type float16 or bfloat16 or float32.
- dy: A tensor of the same dtype as "y"

## Outputs

z: A tensor. Has the same dtype as "y".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y: bfloat16,float16,float32
- input1 dy: bfloat16,float16,float32
- output0 z: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator AtanGrad.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
