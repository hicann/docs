# ApplyFtrl

```c
REG_OP(ApplyFtrl)
    .INPUT(var, TensorType::NumberType())
    .INPUT(accum, TensorType::NumberType())
    .INPUT(linear, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(l1, TensorType::NumberType())
    .INPUT(l2, TensorType::NumberType())
    .INPUT(lr_power, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ApplyFtrl)
```

## Brief

Updates "var" according to the Ftrl-proximal scheme . 

## Inputs

Eight inputs, including:
- var: A mutable Tensor. Must be of type TensorType::NumberType().
    Should be a Variable Tensor.
- accum: A mutable Tensor of the same type as "var".
    Should be a Variable Tensor.
- linear: A mutable Tensor of the same type as "var".
    Should be a Variable Tensor.
- grad: A Tensor of the same type as "var", for the gradient.
- lr: A Tensor of the same type as "var", for the scaling factor. Must be a scalar.
- l1: A Tensor of the same type as "var", for L1 regulariation. Must be a scalar.
- l2: A Tensor of the same type as "var", for L2 regulariation. Must be a scalar.
- lr_power: A Tensor of the same type as "var", for the scaling factor. Must be a scalar .

## Outputs

var: A mutable Tensor. Has the same type as "var" . 

## Attributes

use_locking: An optional bool. Defaults to "False".
    If "True", updating of the "var" and "accum" tensors will be
    protected by a lock; otherwise the behavior is undefined,
    but may exhibit less contention . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: bfloat16,float16,float32
- input1 accum: bfloat16,float16,float32
- input2 linear: bfloat16,float16,float32
- input3 grad: bfloat16,float16,float32
- input4 lr: bfloat16,float16,float32
- input5 l1: bfloat16,float16,float32
- input6 l2: bfloat16,float16,float32
- input7 lr_power: bfloat16,float16,float32
- output0 var: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator ApplyFtrl.


---

[Back to Operator Specifications (Ascend950)](../README.md)
