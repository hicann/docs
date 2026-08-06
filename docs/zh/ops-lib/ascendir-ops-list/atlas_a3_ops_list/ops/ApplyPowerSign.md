# ApplyPowerSign

```c
REG_OP(ApplyPowerSign)
    .INPUT(var, TensorType::NumberType())
    .INPUT(m, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(logbase, TensorType::NumberType())
    .INPUT(sign_decay, TensorType::NumberType())
    .INPUT(beta, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ApplyPowerSign)
```

## Brief

Updates "var" according to the AddSign update.
 t-1 mean previous period.
 m_t <- beta1 * m_{t-1} + (1 - beta1) * grad
 update <- exp(logbase * sign_decay * sign(grad) * sign(m_t)) * grad
 var <- var - lr * update

## Inputs

- var: A mutable tensor. Should be from a Variable().
- m: A mutable tensor. Has the same type as "var".
    Should be from a Variable().
- lr: A scalar. Has the same type as "var".
- logbase: A scalar. Has the same type as "var".
- sign_decay: A scalar. Has the same type as "var".
- beta: A scalar. Has the same type as "var".
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
- input0 var: float32
- input1 m: float32
- input2 lr: float32
- input3 logbase: float32
- input4 sign_decay: float32
- input5 beta: float32
- input6 grad: float32
- output0 var: float32

## Attention Constraints

 the input tensors must have the same shape.

## Third-party framework compatibility

Compatible with the TensorFlow operator ApplyPowerSign.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
