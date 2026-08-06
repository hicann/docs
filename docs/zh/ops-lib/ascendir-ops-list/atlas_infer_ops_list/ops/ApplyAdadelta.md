# ApplyAdadelta

```c
REG_OP(ApplyAdadelta)
    .INPUT(var, TensorType::NumberType())
    .INPUT(accum, TensorType::NumberType())
    .INPUT(accum_update, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(rho, TensorType::NumberType())
    .INPUT(epsilon, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ApplyAdadelta)
```

## Brief

Updates "var" according to the proximal adadelta scheme . 

## Inputs

Seven inputs, including:
- var: A mutable Tensor of type TensorType::NumberType().
    Should be a Variable Tensor.
- accum: A mutable Tensor of the same type as "var".
    Should be a Variable Tensor.
- accum_update: A mutable Tensor of the same type as "var".
    Should be a Variable Tensor.
- lr: A scalar of the same type as "var", for the scaling factor.
- rho: A scalar of the same type as "var", for the decay factor.
- epsilon: A scalar of the same type as "var", for the constant factor.
- grad: A Tensor of the same type as "var", for the gradient .

## Outputs

var: A mutable Tensor. Has the same type as "var" . 

## Attributes

use_locking: An optional bool. Defaults to "False".
    If "True", updating of the "var", "accum" and "accum_update" tensors will be
    protected by a lock; otherwise the behavior is undefined,
    but may exhibit less contention . 

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
- output0 var: float32

## Third-party framework compatibility

Compatible with the TensorFlow operator ApplyAdadelta.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
