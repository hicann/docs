# ApplyGradientDescent

```c
REG_OP(ApplyGradientDescent)
    .INPUT(var, TensorType::NumberType())
    .INPUT(alpha, TensorType::NumberType())
    .INPUT(delta, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ApplyGradientDescent)
```

## Brief

Updates "var" by subtracting 'alpha' * 'delta' from it.
  var -= delta * alpha

## Inputs

- var: A mutable tensor. Should be from a Variable().
- alpha: A scalar. Has the same type as "var".
- delta: A tensor for the change. Has the same type as "var".

## Outputs

var: A mutable tensor. Has the same type as input "var".

## Attributes

use_locking: An optional bool. Defaults to "False".
    If "True", updating of the "var" tensors is protected
    by a lock; otherwise the behavior is undefined, but may exhibit less
    contention.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: bfloat16,float16,float32
- input1 alpha: bfloat16,float16,float32
- input2 delta: bfloat16,float16,float32
- output0 var: bfloat16,float16,float32

## Attention Constraints

 the input tensors must have the same shape.

## Third-party framework compatibility

Compatible with the TensorFlow operator ApplyGradientDescent.


---

[Back to Operator Specifications (Ascend950)](../README.md)
