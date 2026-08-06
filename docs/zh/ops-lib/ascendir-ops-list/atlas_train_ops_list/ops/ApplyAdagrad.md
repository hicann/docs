# ApplyAdagrad

```c
REG_OP(ApplyAdagrad)
    .INPUT(var, TensorType::NumberType())
    .INPUT(accum, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(update_slots, Bool, true)
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ApplyAdagrad)
```

## Brief

Updates "var" according to the adagrad scheme.
  accum += grad * grad
  var -= lr * grad * (1 / sqrt(accum))

## Inputs

- var: A mutable tensor. Should be from a Variable(). Support float16, bfloat16 and float32.
- accum: A mutable tensor. Has the same type as "var".
    Should be from a Variable().
- lr: A scalar. Has the same type as "var".
- grad: A tensor for the gradient. Has the same type as "var".

## Outputs

var: A mutable tensor. Has the same type as input "var".

## Attributes

- update_slots: An optional bool. Defaults to "True". If "True", the accum tensor will be updated.
- use_locking: An optional bool. Defaults to "False".
    If "True", updating of the "var", "ms", and "mom" tensors is protected
    by a lock; otherwise the behavior is undefined, but may exhibit less
    contention.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float32
- input1 accum: float32
- input2 lr: float32
- input3 grad: float32
- output0 var: float32

## Attention Constraints

- The input and output tensors must have the same shape.

## Third-party framework compatibility

Compatible with the TensorFlow operator ApplyAdagrad.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
