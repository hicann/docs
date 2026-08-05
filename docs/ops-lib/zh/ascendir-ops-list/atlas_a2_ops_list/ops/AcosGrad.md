# AcosGrad

```c
REG_OP(AcosGrad)
  .INPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
  .INPUT(dy, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
  .OUTPUT(z, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
  .OP_END_FACTORY_REG(AcosGrad)
```

## Brief

Computes gradients for Acos operation. Support broadcasting operations.

## Inputs

Two inputs, including:
- y: A tensor of type float16 or float32 or bfloat16.
- dy: A tensor with the same dtype of "y".

## Outputs

z: A tensor. Has the same dtype as "y".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y: bfloat16,float16,float32
- input1 dy: bfloat16,float16,float32
- output0 z: bfloat16,float16,float32

## Attention Constraints

"dy" has the same shape with "y".

## Third-party framework compatibility

Compatible with the TensorFlow operator AcosGrad.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
