# ApplyAddSign

```c
REG_OP(ApplyAddSign)
    .INPUT(var, TensorType::NumberType())
    .INPUT(m, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(alpha, TensorType::NumberType())
    .INPUT(sign_decay, TensorType::NumberType())
    .INPUT(beta, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ApplyAddSign)
```

## Brief

Updates "var" according to the AddSign update . 

## Inputs

Seven inputs, including:
- var: A ND Tensor of type TensorType::NumberType().
- m: A ND Tensor of the same type as "var".
- lr: A Tensor of the same type as "var", for the scaling factor. Must be a scalar.
    Support Dimension: 1D.
    Support format: ND.
- alpha: A Tensor of the same type as "var". Must be a scalar.
    Support Dimension: 1D.
    Support format: ND.
- sign_decay: A Tensor of the same type as "var". Must be a scalar.
    Support Dimension: 1D.
    Support format: ND.
- beta: A Tensor of the same type as "var". Must be a scalar.
    Support Dimension: 1D.
    Support format: ND.
- grad: A Tensor of the same type as "var", for the gradient.
    Support format: ND.
    Support Dimension: 2D.

## Outputs

var: A ND Tensor. Has the same type and shape with "var" . 

## Attributes

use_locking: An optional bool. Defaults to "False".
    If "True", updating of the "var" and "m" tensors will be
    protected by a lock; otherwise the behavior is undefined,
    but may exhibit less contention . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float32
- input1 m: float32
- input2 lr: float32
- input3 alpha: float32
- input4 sign_decay: float32
- input5 beta: float32
- input6 grad: float32
- output0 var: float32

## Third-party framework compatibility

Compatible with the TensorFlow operator ApplyAddSign.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
