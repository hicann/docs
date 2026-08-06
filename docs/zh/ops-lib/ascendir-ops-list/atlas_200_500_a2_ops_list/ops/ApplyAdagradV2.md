# ApplyAdagradV2

```c
REG_OP(ApplyAdagradV2)
    .INPUT(var, TensorType::NumberType())
    .INPUT(accum, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(epsilon, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(update_slots, Bool, true)
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ApplyAdagradV2)
```

## Brief

Updates "var" according to the adagradv2 scheme.
  accum += grad * grad
  var -= lr * grad * (1 / sqrt(accum) + epsilon)

## Inputs

- var: A mutable tensor. Must be one of the data types defined in
TensorType::NumberType(). Should be from a Variable().
- accum: A mutable tensor. Has the same type as "var". Should be from a
Variable().
- lr: A tensor for the learning rate. Has the same type as "var". Should be
from a Variable().
- grad: A tensor for the gradient. Has the same type as "var". Should be
from a Variable().
- epsilon: A scalar. Has the same type as "var".

## Outputs

var: A mutable tensor. Has the same type as input "var".

## Attributes

- update_slots: An optional bool. Defaults to "True".
If "True", "accum" will be updated
- use_locking: An optional bool. Defaults to "False".
If "True", updating of the "var" tensor is protected by a lock;
otherwise the behavior is undefined, but may exhibit less contention.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float32
- input1 accum: float32
- input2 lr: float32
- input3 epsilon: float32
- input4 grad: float32
- output0 var: float32

## Attention Constraints

The input tensors must have the same shape.

## Third-party framework compatibility

Compatible with the TensorFlow operator ApplyAdagrad.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
