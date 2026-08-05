# ApplyCenteredRMSProp

```c
REG_OP(ApplyCenteredRMSProp)
    .INPUT(var, TensorType::NumberType())
    .INPUT(mg, TensorType::NumberType())
    .INPUT(ms, TensorType::NumberType())
    .INPUT(mom, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(rho, TensorType::NumberType())
    .INPUT(momentum, TensorType::NumberType())
    .INPUT(epsilon, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ApplyCenteredRMSProp)
```

## Brief

Updates "var" according to the centered RMSProp algorithm.
 The centered RMSProp algorithm uses an estimate of the centered second moment
 (i.e., the variance) for normalization, as opposed to regular RMSProp, which
 uses the (uncentered) second moment. This often helps with training, but is
 slightly more expensive in terms of computation and memory.
 t-1 mean previous period.
 mg <- rho * mg{t-1} + (1-rho) * grad
 ms <- rho * ms{t-1} + (1-rho) * grad * grad
 mom <- momentum * mom{t-1} + lr * grad / sqrt(ms - mg * mg + epsilon)
 var <- var - mom

## Inputs

- var: A mutable tensor. Should be from a Variable().
- mg: A mutable tensor. Has the same type as "var".
    Should be from a Variable().
- ms: A mutable tensor. Has the same type as "var".
    Should be from a Variable().
- mom: A mutable tensor. Has the same type as "var".
    Should be from a Variable().
- lr: A scalar. Has the same type as "var".
- rho: A scalar. Has the same type as "var".
- momentum: A tensor. Has the same type as "var".
- epsilon: A scalar. Has the same type as "var".
- grad: A tensor for the gradient. Has the same type as "var".

## Outputs

var: A mutable tensor. Has the same type as input "var".

## Attributes

use_locking: An optional bool. Defaults to "False".
    If "True", updating of the "var", "ms", and "mom" tensors is protected
    by a lock; otherwise the behavior is undefined, but may exhibit less
    contention.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: bfloat16,float16,float32
- input1 mg: bfloat16,float16,float32
- input2 ms: bfloat16,float16,float32
- input3 mom: bfloat16,float16,float32
- input4 lr: bfloat16,float16,float32
- input5 rho: bfloat16,float16,float32
- input6 momentum: bfloat16,float16,float32
- input7 epsilon: bfloat16,float16,float32
- input8 grad: bfloat16,float16,float32
- output0 var: bfloat16,float16,float32

## Attention Constraints

- in dense implementation of this algorithm, mg, ms, and mom will
   update even if the grad is zero, but in this sparse implementation, mg, ms,
   and mom will not update in iterations during which the grad is zero.
- the input tensors must have the same shape.

## Third-party framework compatibility

Compatible with the TensorFlow operator ApplyCenteredRMSProp.


---

[Back to Operator Specifications (Ascend950)](../README.md)
