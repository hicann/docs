# FusedMulApplyKerasMomentum

```c
REG_OP(FusedMulApplyKerasMomentum)
    .INPUT(var, TensorType::NumberType())
    .INPUT(accum, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(x1, TensorType::NumberType())
    .INPUT(momentum, TensorType::NumberType())
    .INPUT(x2, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .OUTPUT(accum, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .ATTR(use_nesterov, Bool, false)
    .OP_END_FACTORY_REG(FusedMulApplyKerasMomentum)
```

## Brief

Updates '*var' according to the momentum scheme.
  accum = accum * momentum - x1 * x2 * lr
  if use_nesterov is True:
      var += accum * momentum - x1 * x2 * lr
  else:
      var += accum

## Inputs

- var: A mutable tensor. Should be from a Variable(). Supported dtype: float32.
   Supported format: NC1HWC0, C1HWNCoC0, ND, FRACTAL_Z.
- accum: A mutable tensor. Has the same shape, data type, and format as "var".
   Should be from a Variable(). Supported dtype: float32
- x1: A mutable Tensor. Has the same shape, data type, and format as "var".
   Should be from a Variable(). Supported dtype: float32
- momentum: A scalar. Has the same data type as "var". Supported dtype: float32
- x2: A scalar has the same data type as "var". Supported dtype: float32
- lr: A scalar. has the same data type as "var". Supported dtype: float32

## Outputs

- var: A mutable tensor. Has the same data type, shape, and format as input "var".
- accum: A mutable tensor. Has the same data type, shape, and format as input "accum".

## Attributes

- use_nesterov: An optional bool. Defaults to "False".
   If "True", var will be updated by using Nesterov momentum.
- use_locking: An optional bool. Defaults to "False".
   If "True", updating of the "var" tensor is protected by a lock;
   otherwise the behavior is undefined, but may exhibit less contention.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float16,float32
- input1 accum: float16,float32
- input2 lr: float16,float32
- input3 x1: float16,float32
- input4 momentum: float16,float32
- input5 x2: float16,float32
- output0 var: float16,float32
- output1 accum: float16,float32

## Attention Constraints

- var: A mutable tensor. Has the same type as input "var".
- accum: A mutable tensor. Has the same type as input "accum".

## Third-party framework compatibility

Compatible with the TensorFlow operator ResourceApplyKerasMomentum.


---

[Back to Operator Specifications (Ascend950)](../README.md)
