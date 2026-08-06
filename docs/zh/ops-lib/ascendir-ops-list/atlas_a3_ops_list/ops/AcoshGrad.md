# AcoshGrad

```c
REG_OP(AcoshGrad)
  .INPUT(y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
  .INPUT(dy, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
  .OUTPUT(z, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
  .OP_END_FACTORY_REG(AcoshGrad)
```

## Brief

Computes gradients for Acosh operation. Support broadcasting operations.

## Inputs

- y: A ND tensor of type float16 or bfloat16 or float32. Support 1D ~ 8D.
- dy: A ND tensor with the same dtype of "y".

## Outputs

z: A ND tensor. Has the same dtype as "y".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y: bfloat16,float16,float32
- input1 dy: bfloat16,float16,float32
- output0 z: bfloat16,float16,float32

## Attention Constraints

"dy" has the same dtype as "y".

## Third-party framework compatibility

Compatible with the TensorFlow operator AcoshGrad.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
