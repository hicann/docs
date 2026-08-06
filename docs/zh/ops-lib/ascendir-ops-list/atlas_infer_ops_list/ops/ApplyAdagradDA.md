# ApplyAdagradDA

```c
REG_OP(ApplyAdagradDA)
    .INPUT(var, TensorType::NumberType())
    .INPUT(gradient_accumulator, TensorType::NumberType())
    .INPUT(gradient_squared_accumulator, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(l1, TensorType::NumberType())
    .INPUT(l2, TensorType::NumberType())
    .INPUT(global_step, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ApplyAdagradDA)
```

## Brief

Updates "var" according to the proximal adagrad scheme . 

## Inputs

Eight inputs, including:
- var: A mutable Tensor. Must be one of the following types:
    TensorType::NumberType(). Should be a Variable Tensor.
- gradient_accumulator: A mutable Tensor. Must have the same
    type as "var". Should be a Variable Tensor.
- gradient_squared_accumulator: A mutable Tensor of the same type as "var".
    Should be a Variable Tensor.
- grad: A Tensor of the same type as "var", for the gradient.
- lr: A Tensor of the same type as "var".
    Scaling factor. Must be a scalar.
- l1: A Tensor of the same type as "var".
    L1 regulariation. Must be a scalar.
- l2: A Tensor of the same type as "var".
    L2 regulariation. Must be a scalar.
- global_step: A Tensor of type int32 or int64.
    Training step number. Must be a scalar . 

## Outputs

var: A mutable Tensor. Has the same type as "var" . 

## Attributes

use_locking: An optional bool. Defaults to "False".
    If "True", updating of the var and accum tensors will be
    protected by a lock; otherwise the behavior is undefined,
    but may exhibit less contention . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float32
- input1 gradient_accumulator: float32
- input2 gradient_squared_accumulator: float32
- input3 grad: float32
- input4 lr: float32
- input5 l1: float32
- input6 l2: float32
- input7 global_step: int32
- output0 var: float32

## Third-party framework compatibility

Compatible with the TensorFlow operator ApplyAdagradDA.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
