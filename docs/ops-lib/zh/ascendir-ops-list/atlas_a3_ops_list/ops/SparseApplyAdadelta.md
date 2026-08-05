# SparseApplyAdadelta

```c
REG_OP(SparseApplyAdadelta)
    .INPUT(var, TensorType::NumberType())
    .INPUT(accum, TensorType::NumberType())
    .INPUT(accum_update, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(rho, TensorType::NumberType())
    .INPUT(epsilon, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .INPUT(indices, TensorType::IndexNumberType())
    .OUTPUT(var, TensorType::NumberType())
    .OUTPUT(accum, TensorType::NumberType())
    .OUTPUT(accum_update, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(SparseApplyAdadelta)
```

## Brief

Updates "var" in specified index according to the Adadelta algorithm.
   accum <- rho * accum + (1 - rho) * grad.square()
   update <- (accum_update + epsilon).sqrt() * (accum + epsilon()).rsqrt() * grad
   var <- var - update * lr
   accum_update <- rho() * accum_update + (1 - rho()) * update.square()

## Inputs

Eight inputs, including:
- var: A mutable tensor. Support dtype: float32, support format: [NC1HWC0,ND].
- accum: A mutable tensor. Support dtype: float32, support format: [NC1HWC0,ND].
- accum_update: A mutable tensor. Support dtype: float32, support format: [NC1HWC0,ND].
- lr: A scalar. Must have the same type as "var". Support format: [ND].
- rho: A scalar. Must have the same type as "var". Support format: [ND].
- epsilon: A scalar. Must have the same type as "var". Support format: [ND].
- grad: A tensor, specifying the gradient. Has the same type and format as var.
- indices: A vector of indices into the first dimension of "var", "accum" and "accum_update". Support dtype: int32,
int64, support format: [ND].
The value of indices must be unique. Otherwise, the result is unpredictable . 

## Outputs

- var: A mutable tensor. Has the same type and format as input "var".
- accum:  A mutable tensor. Must have the same type and format as input "accum".
- accum_update: A mutable tensor. Must have the same type and format as input "accum_update".

## Attributes

use_locking: An optional "bool". Defaults to "False". If "True", updating of
the "var", "accum", and "accum_update" tensors will be protected by a lock; otherwise the
behavior is undefined, but may exhibit less contention.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float32
- input1 accum: float32
- input2 accum_update: float32
- input3 lr: float32
- input4 rho: float32
- input5 epsilon: float32
- input6 grad: float32
- input7 indices: int32,int64
- output0 var: float32
- output1 accum: float32
- output2 accum_update: float32

## Attention Constraints

- Note that in this sparse implementation, "accum" and "accum_update" will not update
in iterations during which "grad" is 0.
- The input tensors "var", "accum", and "accum_update" must have the same shape.

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseApplyAdadelta.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
