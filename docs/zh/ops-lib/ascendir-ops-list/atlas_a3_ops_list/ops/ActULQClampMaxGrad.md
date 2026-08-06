# ActULQClampMaxGrad

```c
REG_OP(ActULQClampMaxGrad)
    .INPUT(y_grad, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(clamp_max_mask, TensorType({DT_BOOL, DT_FLOAT16, DT_FLOAT}))
    .INPUT(x_clamped_loss, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(clamp_max_grad, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OP_END_FACTORY_REG(ActULQClampMaxGrad)
```

## Brief

QAT ULQ clamp-max backward gradient.
  clamp_max_grad = sum_over_all_axes( y_grad * (x_clamped_loss + |clamp_max_mask|) ).

## Inputs

Three inputs (identical shape, no broadcast):
- y_grad: upstream gradient. Must be one of the following types: float16, float32.
- clamp_max_mask: clamp-max mask (values in {0, 1}). Must be one of: bool, float16, float32.
- x_clamped_loss: clamp loss term. Must be one of: float16, float32.

## Outputs

clamp_max_grad: 0-D scalar gradient for the learnable clamp-max bound. dtype follows y_grad.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y_grad: float16,float32
- input1 clamp_max_mask: bool,float16,float32
- input2 x_clamped_loss: float16,float32
- output0 clamp_max_grad: float16,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
