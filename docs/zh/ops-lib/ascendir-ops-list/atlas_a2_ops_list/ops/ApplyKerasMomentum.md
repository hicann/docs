# ApplyKerasMomentum

```c
REG_OP(ApplyKerasMomentum)
    .INPUT(var, TensorType::NumberType())
    .INPUT(accum, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .INPUT(momentum, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .ATTR(use_nesterov, Bool, false)
    .OP_END_FACTORY_REG(ApplyKerasMomentum)
```

## Brief

Updates '*var' according to the momentum scheme.
  accum = accum * momentum - grad * lr
  if use_nesterov is True:
      var += accum * momentum - grad * lr
  else:
      var += accum

## Inputs

- var: A mutable tensor. Must be one of the data types defined in
   TensorType::NumberType(). Should be from a Variable().
- accum: A mutable tensor. Has the same type as "var". Should be from a
   Variable().
- lr: A tensor for the learning rate. Has the same type as "var". Should be
   from a Variable().
- grad: A tensor for the gradient. Has the same type as "var". Should be
   from a Variable().
- momentum: A scalar. Has the same type as "var".

## Outputs

var: A mutable tensor. Has the same type as input "var".

## Attributes

- use_nesterov: An optional bool. Defaults to "False".
   If "True", var will be updated by using Nesterov momentum.
- use_locking: An optional bool. Defaults to "False".
   If "True", updating of the "var" tensor is protected by a lock;
   otherwise the behavior is undefined, but may exhibit less contention.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float32
- input1 accum: float32
- input2 lr: float32
- input3 grad: float32
- input4 momentum: float32
- output0 var: float32

## Attention Constraints

The input tensors must have the same shape.

## Third-party framework compatibility

Compatible with the TensorFlow operator ResourceApplyKerasMomentum.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
