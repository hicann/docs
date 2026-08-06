# ApplyProximalAdagrad

```c
REG_OP(ApplyProximalAdagrad)
    .INPUT(var, TensorType::NumberType())
    .INPUT(accum, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(l1, TensorType::NumberType())
    .INPUT(l2, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ApplyProximalAdagrad)
```

## Brief

Update "var" and "accum" according to FOBOS with Adagrad learning rate . 

## Inputs

Six inputs, including:
- var: A mutable Tensor of type TensorType::NumberType().
   Should be from a Variable().
- accum: A mutable Tensor of the same type as "var". Should be from a Variable().
- lr: A Tensor of the same type as "var", for the scaling factor. Must be a scalar.
- l1: A Tensor of the same type as "var", for L1 regulariation. Must be a scalar.
- l2: A Tensor of the same type as "var", for L2 regulariation. Must be a scalar.
- grad: A Tensor of the same type as "var", for the gradient .

## Outputs

var: A mutable tensor. Must have the same type as input "var" . 

## Attributes

use_locking: An optional bool. Defaults to "False". If "True", updating of the "var" and "accum" *tensors will be protected by a lock; otherwise the behavior is undefined, but may exhibit less *contention . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float32
- input1 accum: float32
- input2 lr: float32
- input3 l1: float32
- input4 l2: float32
- input5 grad: float32
- output0 var: float32

## Third-party framework compatibility

Compatible with the TensorFlow operator ApplyProximalAdagrad.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
