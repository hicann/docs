# SparseApplyRMSProp

```c
REG_OP(SparseApplyRMSProp)
    .INPUT(var, TensorType::NumberType())
    .INPUT(ms, TensorType::NumberType())
    .INPUT(mom, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(rho, TensorType::NumberType())
    .INPUT(momentum, TensorType::NumberType())
    .INPUT(epsilon, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .INPUT(indices, TensorType::IndexNumberType())
    .OUTPUT(var, TensorType::NumberType())
    .OUTPUT(ms, TensorType::NumberType())
    .OUTPUT(mom, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(SparseApplyRMSProp)
```

## Brief

Updates "var" in specified index according to the RMSProp algorithm.
   mean_square = decay * mean_square + (1-decay) * gradient ** 2
   Delta = learning_rate * gradient / sqrt(mean_square + epsilon)
   ms <- rho * ms_{t-1} + (1-rho) * grad * grad
   mom <- momentum * mom_{t-1} + lr * grad / sqrt(ms + epsilon)
   var <- var - mom

## Inputs

Nine inputs, including:
- var: A mutable tensor. Support dtype: float32, support format: [NC1HWC0,ND].
- ms: A mutable tensor. Support dtype: float32, support format: [NC1HWC0,ND].
- mom: A mutable tensor. Support dtype: float32, support format: [NC1HWC0,ND].
- lr: A scalar. Must have the same type as "var", support format: [ND].
- rho: A scalar. Must have the same type as "var", support format: [ND].
- momentum: A scalar. Must have the same type as "var", support format: [ND].
- epsilon: A scalar. Must have the same type as "var", support format: [ND].
- grad: A tensor, specifying the gradient. Support dtype: float32, support format: [NC1HWC0,ND].
- indices: A vector of indices into the first dimension of "var", "mom" and "ms". Support dtype: int32,
int64, support format: [ND].
The value of indices must be unique. Otherwise, the result is unpredictable . 

## Outputs

- var: A mutable tensor. Has the same type and format as input "var".
- ms:  A mutable tensor. Must have the same type and format as input "ms".
- mom: A mutable tensor. Must have the same type and format as input "mom".

## Attributes

use_locking: An optional "bool". Defaults to "False". If "True", updating of
the "var", "ms", and "mom" tensors will be protected by a lock; otherwise the
behavior is undefined, but may exhibit less contention.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float32
- input1 ms: float32
- input2 mom: float32
- input3 lr: float32
- input4 rho: float32
- input5 momentum: float32
- input6 epsilon: float32
- input7 grad: float32
- input8 indices: int32,int64
- output0 var: float32
- output1 ms: float32
- output2 mom: float32

## Attention Constraints

- Note that in this sparse implementation, "ms" and "mom" will not update
in iterations during which "grad" is 0.
- The input tensors "var", "ms", and "mom" must have the same shape.

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseApplyRMSProp.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
