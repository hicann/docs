# ApplyAdam

```c
REG_OP(ApplyAdam)
    .INPUT(var, TensorType::NumberType())
    .INPUT(m, TensorType::NumberType())
    .INPUT(v, TensorType::NumberType())
    .INPUT(beta1_power, TensorType::NumberType())
    .INPUT(beta2_power, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(beta1, TensorType::NumberType())
    .INPUT(beta2, TensorType::NumberType())
    .INPUT(epsilon, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .ATTR(use_nesterov, Bool, false)
    .OP_END_FACTORY_REG(ApplyAdam)
```

## Brief

Updates "var" according to the Adam algorithm.
 lr_t <- text{learning\_rate} * sqrt{1 - beta_2^t} / (1 - beta_1^t)
 m_t <- beta_1 * m_{t-1} + (1 - beta_1) * g
 v_t <- max(beta2 * v{t-1}, abs(g))
 variable <- variable - lr_t * m_t / (sqrt{v_t} + epsilon)

## Inputs

- var: A mutable Tensor of the type TensorType::NumberType().
    Should be from a Variable().
- m: A mutable Tensor of the same type as "var".
    Should be from a Variable().
- v: A mutable Tensor of the same type as "var".
    Should be from a Variable().
- beta1_power: A scalar of the same type as "var".
- beta2_power: A scalar of the same type as "var".
- lr: learning_rate. A scalar of the same type as "var".
- beta1: A scalar of the same type as "var".
- beta2: A scalar of the same type as "var".
- epsilon: A scalar of the same type as "var".
- grad: A Tensor of the same type as "var", for the gradient.

## Outputs

var: A mutable Tensor. Has the same type as intput "var" . 

## Attributes

- use_locking: An optional bool. Defaults to "False".
    If "True", updating of the "var", m", and "v" tensors will be protected
    by a lock; otherwise the behavior is undefined, but may exhibit less
    contention.
- use_nesterov: An optional bool. Defaults to "False".
If "True", uses the nesterov update.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float32
- input1 m: float32
- input2 v: float32
- input3 beta1_power: float32
- input4 beta2_power: float32
- input5 lr: float32
- input6 beta1: float32
- input7 beta2: float32
- input8 epsilon: float32
- input9 grad: float32
- output0 var: float32
### AI CPU
- input0 var: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input1 m: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input2 v: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input3 beta1_power: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input4 beta2_power: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input5 lr: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input6 beta1: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input7 beta2: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- input8 grad: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64
- output0 var: complex64,complex128,double,float16,float32,int8,int16,int32,int64,qint8,qint32,quint8,uint8,uint16,uint32,uint64

## Attention Constraints

 *The input tensors must have the same shape.*

## Third-party framework compatibility

Compatible with the TensorFlow operator ApplyAdam.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
