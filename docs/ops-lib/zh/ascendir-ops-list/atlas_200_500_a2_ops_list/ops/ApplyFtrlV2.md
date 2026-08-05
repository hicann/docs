# ApplyFtrlV2

```c
REG_OP(ApplyFtrlV2)
    .INPUT(var, TensorType::NumberType())
    .INPUT(accum, TensorType::NumberType())
    .INPUT(linear, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(l1, TensorType::NumberType())
    .INPUT(l2, TensorType::NumberType())
    .INPUT(l2_shrinkage, TensorType::NumberType())
    .INPUT(lr_power, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ApplyFtrlV2)
```

## Brief

Update "var" according to the Ftrl-proximal scheme . 

## Inputs

Nine inputs, including:
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
- l2_shrinkage: A Tensor of the same type as "var".
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
- input0 var: float32
- input1 accum: float32
- input2 linear: float32
- input3 grad: float32
- input4 lr: float32
- input5 l1: float32
- input6 l2: float32
- input7 l2_shrinkage: float32
- input8 lr_power: float32
- output0 var: float32

## Third-party framework compatibility

Compatible with the TensorFlow operator ApplyFtrlV2.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
