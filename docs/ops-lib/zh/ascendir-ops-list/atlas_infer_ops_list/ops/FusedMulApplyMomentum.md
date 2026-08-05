# FusedMulApplyMomentum

```c
REG_OP(FusedMulApplyMomentum)
    .INPUT(var, TensorType::NumberType())
    .INPUT(accum, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(x1, TensorType::NumberType())
    .INPUT(momentum, TensorType::NumberType())
    .INPUT(x2, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .OUTPUT(accum, TensorType::NumberType())
    .ATTR(use_nesterov, Bool, false)
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(FusedMulApplyMomentum)
```

## Brief

Fused Mul + ApplyMomentum training op (CANN graph-mode).
 grad = x1 * x2; accum' = accum * momentum + grad;
 var_delta = accum' * lr (standard) or grad*lr + accum'*momentum*lr (Nesterov);
 var' = var - var_delta.

## Inputs

- var: weight tensor, in-place updated.
- accum: momentum buffer, in-place updated.
- lr: learning rate scalar.
- x1: gradient component g1.
- momentum: momentum coefficient scalar.
- x2: LossScale reciprocal g2 scalar.

## Outputs

- var: updated weight var' (in-place, reuses input var).
- accum: updated momentum buffer accum' (in-place, reuses input accum).

## Attributes

- use_nesterov: bool, default false. Standard/Nesterov var_delta.
- use_locking: bool, default false. Reserved (no numerical effect).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float16,float32
- input1 accum: float16,float32
- input2 lr: float16,float32
- input3 x1: float16,float32
- input4 momentum: float16,float32
- input5 x2: float16,float32
- output0 var: float16,float32
- output1 accum: float16,float32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
