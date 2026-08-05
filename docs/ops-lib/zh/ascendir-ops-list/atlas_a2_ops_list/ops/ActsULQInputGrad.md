# ActsULQInputGrad

```c
REG_OP(ActsULQInputGrad)
    .INPUT(y_grad, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(clamp_min_mask, TensorType({DT_BOOL, DT_FLOAT16, DT_FLOAT}))
    .INPUT(clamp_max_mask, TensorType({DT_BOOL, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(x_grad, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OP_END_FACTORY_REG(ActsULQInputGrad)
```

## Brief

Returns y_grad * clamp_min_mask * clamp_max_mask (elementwise STE clamp gradient gate).

## Inputs

Three inputs, including:
- y_grad: An ND Tensor. Must be one of the following types: float16, float32.
- clamp_min_mask: An ND Tensor. Must be one of the following types: bool, float16, float32.
- clamp_max_mask: An ND Tensor. Must be one of the following types: bool, float16, float32.

## Outputs

x_grad: An ND Tensor. Must be one of the following types: float16, float32 (same as y_grad).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y_grad: float16,float32
- input1 clamp_min_mask: bool,float16,float32
- input2 clamp_max_mask: bool,float16,float32
- output0 x_grad: float16,float32

## Third-party framework compatibility

Compatible with the MindSpore ULQ backward operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
