# AsinGrad

```c
REG_OP(AsinGrad)
  .INPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_DOUBLE,
                        DT_INT32, DT_INT64, DT_COMPLEX64, DT_COMPLEX128}))
  .INPUT(dy, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_DOUBLE,
                         DT_INT32, DT_INT64, DT_COMPLEX64, DT_COMPLEX128}))
  .OUTPUT(z, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16, DT_DOUBLE,
                         DT_INT32, DT_INT64, DT_COMPLEX64, DT_COMPLEX128}))
  .OP_END_FACTORY_REG(AsinGrad)
```

## Brief

Computes gradients for Asin operation. Support broadcasting operations.

## Inputs

Two inputs, including:
- y: An ND or 5HD tensor. support 1D ~ 8D. Must be one of the following types:
float16, bfloat16, float32, float64, int32, int64, complex64, complex128.
- dy: A tensor of the same dtype as "y".

## Outputs

z: A tensor. Has the same dtype as "y".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y: float16,float32
- input1 dy: float16,float32
- output0 z: float16,float32

## Attention Constraints

"dy" has the same dtype as "y".

## Third-party framework compatibility

Compatible with the TensorFlow operator AsinGrad.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
