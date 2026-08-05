# ApplyAdamWithAmsgrad

```c
REG_OP(ApplyAdamWithAmsgrad)
    .INPUT(var, TensorType::NumberType())
    .INPUT(m, TensorType::NumberType())
    .INPUT(v, TensorType::NumberType())
    .INPUT(vhat, TensorType::NumberType())
    .INPUT(beta1_power, TensorType::NumberType())
    .INPUT(beta2_power, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(beta1, TensorType::NumberType())
    .INPUT(beta2, TensorType::NumberType())
    .INPUT(epsilon, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ApplyAdamWithAmsgrad)
```

## Brief

Updates '*var' according to the Adam algorithm..
  lr_t := {learning_rate} * sqrt{1 - beta_2^t} / (1 - beta_1^t)
  m_t := beta_1 * m_{t-1} + (1 - beta_1) * g
  v_t := beta_2 * v_{t-1} + (1 - beta_2) * g * g
  vhat_t := max{vhat_{t-1}, v_t}
  variable := variable - lr_t * m_t / (sqrt{vhat_t} + epsilon)

## Inputs

- var: A mutable tensor. Must be one of the data types defined in
   TensorType::NumberType(). Should be from a Variable().
- m: A mutable tensor. Has the same type as "var". Should be from a
   Variable().
- v: A mutable tensor. Has the same type as "var". Should be from a
   Variable().
- vhat: A mutable tensor. Has the same type as "var". Should be from a
   Variable().
- beta1_power: A mutable tensor. Has the same type as "var". Should be from a
   Variable().
- beta2_power: A mutable tensor. Has the same type as "var". Should be from a
   Variable().
- lr: A tensor for the learning rate. Has the same type as "var". Should be
   from a Variable().
- grad: A tensor for the gradient. Has the same type as "var". Should be
   from a Variable().

## Outputs

- var: A mutable tensor. Has the same type as input "var".
- m: A mutable tensor. Has the same type as input "var"
- v: A mutable tensor. Has the same type as input "var"
- vhat: A mutable tensor. Has the same type as input "var"

## Attributes

- beta1: A scalar. Has the same type as "var".
- beta2: A scalar. Has the same type as "var".
- epsilon: A scalar. Has the same type as "var".
- use_locking: An optional bool. Defaults to "False".
   If "True", updating of the "var" tensor is protected by a lock;
   otherwise the behavior is undefined, but may exhibit less contention.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float32
- input1 m: float32
- input2 v: float32
- input3 vhat: float32
- input4 beta1_power: float32
- input5 beta2_power: float32
- input6 lr: float32
- input7 beta1: float32
- input8 beta2: float32
- input9 epsilon: float32
- input10 grad: float32
- output0 var: float32

## Attention Constraints

The input tensors must have the same shape.

## Third-party framework compatibility

Compatible with the TensorFlow operator ResourceApplyKerasMomentum.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
