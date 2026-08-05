# ApplyProximalGradientDescent

```c
REG_OP(ApplyProximalGradientDescent)
    .INPUT(var, TensorType::NumberType())
    .INPUT(alpha, TensorType::NumberType())
    .INPUT(l1, TensorType::NumberType())
    .INPUT(l2, TensorType::NumberType())
    .INPUT(delta, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ApplyProximalGradientDescent)
```

## Brief

Updates "var" as FOBOS algorithm with fixed learning rate.
 prox_v = var - alpha * delta
 var = sign(prox_v)/(1+alpha * l2) * max{|prox_v|-alpha * l1,0}

## Inputs

- var: A mutable tensor. Should be from a Variable().
 Supported data type: float16, float.
 Supported format: NC1HWC0,C1HWNCoC0,ND,FRACTAL_Z,NC1HWC0,C1HWNCoC0,ND,FRACTAL_Z.
- alpha: A scalar. Has the same data type as "var".
- l1: A scalar. Has the same data type as "var".
- l2: A scalar. Has the same data type as "var".
- delta: A tensor. Has the same data type, shape, and format as "var".

## Outputs

var: A mutable tensor. Has the same data type, shape, and format as input "var".

## Attributes

use_locking: An optional bool. Defaults to "False".
    If "True", updating of the "var", "ms", and "mom" tensors is protected
    by a lock; otherwise the behavior is undefined, but may exhibit less
    contention.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float16,float32
- input1 alpha: float16,float32
- input2 l1: float16,float32
- input3 l2: float16,float32
- input4 delta: float16,float32
- output0 var: float16,float32

## Attention Constraints

 the input tensors must have the same shape.

## Third-party framework compatibility

Compatible with the TensorFlow operator ApplyProximalGradientDescent.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
