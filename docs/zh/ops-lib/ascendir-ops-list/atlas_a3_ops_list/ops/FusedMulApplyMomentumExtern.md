# FusedMulApplyMomentumExtern

```c
REG_OP(FusedMulApplyMomentumExtern)
    .INPUT(var, TensorType(DT_FLOAT))
    .INPUT(accum, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(x1, TensorType::NumberType())
    .INPUT(momentum, TensorType::NumberType())
    .INPUT(x2, TensorType::NumberType())
    .INPUT(var_copy, TensorType(DT_FLOAT16))
    .OUTPUT(var, TensorType(DT_FLOAT))
    .OUTPUT(var_copy, TensorType(DT_FLOAT16))
    .OUTPUT(accum, TensorType::NumberType())
    .ATTR(use_nesterov, Bool, false)
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(FusedMulApplyMomentumExtern)
```

## Brief

Fused Mul + ApplyMomentum training op (CANN graph-mode).
 grad = x1 * x2; accum' = accum * momentum + grad;
 var_delta = accum' * lr (standard) or grad*lr + accum'*momentum*lr (Nesterov);
 var' = var - var_delta; var_copy' = var_copy - Cast(var_delta) (independent low-precision copy).

## Inputs

- var: master weight, FP32, in-place updated.
- accum: momentum buffer.
- lr: learning rate scalar.
- x1: gradient component g1.
- momentum: momentum coefficient scalar.
- x2: LossScale reciprocal g2 scalar.
- var_copy: low-precision weight copy (FP16/BF16), in-place updated.

## Outputs

- var: updated master weight var' (in-place, reuses input var).
- var_copy: updated low-precision copy var_copy' (in-place, reuses input var_copy).
- accum: updated momentum buffer accum' (in-place, reuses input accum).

## Attributes

- use_nesterov: bool, default false. Standard/Nesterov var_delta.
- use_locking: bool, default false. Reserved (no numerical effect).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float32
- input1 accum: float16,float32
- input2 lr: float16,float32
- input3 x1: float16,float32
- input4 momentum: float16,float32
- input5 x2: float16,float32
- input6 var_copy: float16
- output0 var: float32
- output1 var_copy: float16
- output2 accum: float16,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
