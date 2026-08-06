# AbsGrad

```c
REG_OP(AbsGrad)
    .INPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(dy, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(z, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(AbsGrad)
```

## Brief

Computes gradients for absolute operation.

## Inputs

- y: A tensor of type float16 or float32 or bfloat16. Support broadcasting operations.
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

Compatible with the TensorFlow operator AbsGrad.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
