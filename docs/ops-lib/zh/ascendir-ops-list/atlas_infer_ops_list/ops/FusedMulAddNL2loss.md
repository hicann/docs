# FusedMulAddNL2loss

```c
REG_OP(FusedMulAddNL2loss)
    .INPUT(x1, TensorType::NumberType())
    .INPUT(x2, TensorType::NumberType())
    .INPUT(x3, TensorType::NumberType())
    .OUTPUT(y1, TensorType::NumberType())
    .OUTPUT(y2, TensorType::NumberType())
    .OP_END_FACTORY_REG(FusedMulAddNL2loss)
```

## Brief

Computes y1 = x1 * x3 + x2 and y2 = sum(x1^2 / 2).

## Inputs

Three inputs, including:
- x1: An ND tensor (weight). Must be one of the following types: float16, float32.
- x2: An ND tensor (weight_grad). Has the same shape and dtype as "x1".
- x3: A scalar tensor (const_input), broadcast to the shape of "x1". Has the same dtype as "x1".

## Outputs

- y1: An ND tensor. Has the same shape and dtype as "x1".
- y2: A scalar tensor, the L2 loss of "x1". Has the same dtype as "x1".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float32
- input1 x2: float32
- input2 x3: float32
- output0 y1: float32
- output1 y2: float32

## Third-party framework compatibility

Compatible with the fused Mul + AddN + L2Loss subgraph.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
