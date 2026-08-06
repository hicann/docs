# ApplyRMSProp

```c
REG_OP(ApplyRMSProp)
    .INPUT(var, TensorType::NumberType())
    .INPUT(ms, TensorType::NumberType())
    .INPUT(mom, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(rho, TensorType::NumberType())
    .INPUT(momentum, TensorType::NumberType())
    .INPUT(epsilon, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(ApplyRMSProp)
```

## Brief

Updates "var" according to the RMSProp algorithm.
   mean_square = decay * mean_square + (1-decay) * gradient ** 2
   Delta = learning_rate * gradient / sqrt(mean_square + epsilon)
   ms <- rho * ms_{t-1} + (1-rho) * grad * grad
   mom <- momentum * mom_{t-1} + lr * grad / sqrt(ms + epsilon)
   var <- var - mom

## Inputs

- var: A mutable tensor. Must be one of the data types defined in
TensorType::NumberType(). Should be from a Variable().
- ms: A mutable tensor. Must have the same type as "var". Should be from a
Variable().
- mom: A mutable tensor. Must have the same type as "var". Should be from a
Variable().
- lr: A scalar. Must have the same type as "var".
- rho: A scalar. Must have the same type as "var".
- momentum: A scalar. Must have the same type as "var".
- epsilon: A scalar. Must have the same type as "var".
- grad: A tensor, specifying the gradient. Must have the same type as "var".

## Outputs

var: A mutable tensor. Has the same type as input "var".

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
- output0 var: float32
### AI CPU
- input0 var: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input1 ms: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input2 mom: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input3 lr: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input4 rho: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input5 momentum: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input6 epsilon: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input7 grad: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- output0 var: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64

## Attention Constraints

- Note that in dense implementation of this algorithm, "ms" and "mom" will
update even if "grad" is 0, but in this sparse implementation, "ms" and "mom"
will not update in iterations during which "grad" is 0.
- The input tensors "var", "ms", "mom" and "grad" must have the same shape.

## Third-party framework compatibility

- Compatible with the TensorFlow operator ApplyRMSProp.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
