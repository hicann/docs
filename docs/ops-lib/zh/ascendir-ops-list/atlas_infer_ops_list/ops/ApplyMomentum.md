# ApplyMomentum

```c
REG_OP(ApplyMomentum)
    .INPUT(var, TensorType::NumberType())
    .INPUT(accum, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .INPUT(momentum, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_nesterov, Bool, false)
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ApplyMomentum)
```

## Brief

Updates "var" according to the momentum scheme. Set use_nesterov = True if you
  want to use Nesterov momentum.
 computing process:
 accum = accum * momentum + grad.
 var -= lr * accum.

## Inputs

- var: A mutable tensor. Should be from a Variable().
- accum: A mutable tensor. Has the same type as "var".
    Should be from a Variable().
- lr: A scalar. Has the same type as "var".
- grad: A tensor for the gradient. Has the same type as "var".
- momentum: Momentum. Must be a scalar.

## Outputs

var: A mutable tensor. Has the same type as input "var".

## Attributes

- use_nesterov: An optional bool. Defaults to "False".
    If "True", the tensor passed to compute grad will be
    var - lr * momentum * accum, so in the end, the var you get is actually
    var - lr * momentum * accum.
- use_locking: An optional bool. Defaults to "False".
    If "True", updating of the "var", "ms", and "mom" tensors is protected by a lock;
    otherwise the behavior is undefined, but may exhibit less contention.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 var: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input1 accum: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input2 lr: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input3 grad: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input4 momentum: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- output0 var: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64

## Attention Constraints

 the input tensors must have the same shape.

## Third-party framework compatibility

Compatible with the TensorFlow operator ApplyMomentum.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
