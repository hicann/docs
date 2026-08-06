# ApplyAdaMax

```c
REG_OP(ApplyAdaMax)
    .INPUT(var, TensorType::NumberType())
    .INPUT(m, TensorType::NumberType())
    .INPUT(v, TensorType::NumberType())
    .INPUT(beta1_power, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(beta1, TensorType::NumberType())
    .INPUT(beta2, TensorType::NumberType())
    .INPUT(epsilon, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ApplyAdaMax)
```

## Brief

Updates "var" according to the AdaMax algorithm.
 t-1 mean previous period.
 m_t <- beta1 * m{t-1} + (1 - beta1) * grad
 v_t <- max(beta2 * v{t-1}, abs(grad))
 var <- var - lr / (1 - beta1^t) * m_t / (v_t + epsilon)

## Inputs

- var: A mutable tensor. Must be one of the following types: TensorType::NumberType().
    Should be from a Variable().
- m: A mutable tensor. Has the same type as "var".
    Should be from a Variable().
- v: A mutable tensor. Has the same type as "var".
    Should be from a Variable().
- beta1_power: A scalar. Has the same type as "var".
- lr: learning_rate. A scalar. Has the same type as "var".
- beta1: A scalar. Has the same type as "var".
- beta2: A scalar. Has the same type as "var".
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
- input0 var: float32
- input1 m: float32
- input2 v: float32
- input3 beta1_power: float32
- input4 lr: float32
- input5 beta1: float32
- input6 beta2: float32
- input7 epsilon: float32
- input8 grad: float32
- output0 var: float32

## Attention Constraints

 the input tensors must have the same shape.

## Third-party framework compatibility

Compatible with the TensorFlow operator ApplyAdaMax.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
