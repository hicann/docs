# SparseApplyProximalAdagrad

```c
REG_OP(SparseApplyProximalAdagrad)
    .INPUT(var, TensorType::NumberType())
    .INPUT(accum, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(l1, TensorType::NumberType())
    .INPUT(l2, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .INPUT(indices, TensorType::IndexNumberType())
    .OUTPUT(var, TensorType::NumberType())
    .OUTPUT(accum, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(SparseApplyProximalAdagrad)
```

## Brief

Updates entries in 'var' and 'accum' according to the Proximal Adagrad algorithm.
Compared with op ApplyProximalAdagrad, an additional index tensor is input,
Only the indices into the first dimensions of "var" and "accum" are updated . 

## Inputs

Seven inputs, including:
- var: A mutable Tensor. Support dtype: float32, support format: [NCHW,NC1HWC0,NHWC,ND,FRACTAL_Z].
- accum: A mutable Tensor of the same type as "var".
    Should be a Variable Tensor. Should be greater than or equal to zero.
    Support dtype: float32, support format: [NCHW,NC1HWC0,NHWC,ND,FRACTAL_Z].
    Accum and grad cannot be equal to zero at the same time.
- lr: A Tensor of the same type as "var".
    Scaling factor. Must be a scalar. Should be greater than zero.
    Support dtype: float32, support format: [NCHW,NC1HWC0,NHWC,ND,FRACTAL_Z].
- l1: A Tensor of the same type as "var".
    L1 regulariation. Must be a scalar. Should be greater than or equal to zero.
    Support dtype: float32, support format: [NCHW,NC1HWC0,NHWC,ND,FRACTAL_Z].
- l2: A Tensor of the same type as "var".
    L2 regulariation. Must be a scalar. Should be greater than or equal to zero.
    Support dtype: float32, support format: [NCHW,NC1HWC0,NHWC,ND,FRACTAL_Z].
- grad: A Tensor. Has the same type as "var".
    The gradient.
    Support dtype: float32, support format: [NCHW,NC1HWC0,NHWC,ND,FRACTAL_Z].
- indices: A vector of indices into the first dimension of "var" and "accum".
    The value of indices must be unique. Otherwise, the result is unpredictable .
    Support dtype: int32, int64, support format: [NCHW,NC1HWC0,NHWC,ND,FRACTAL_Z]. 

## Outputs

- var: A mutable Tensor. Has the same type and format as "var" .
- accum: A mutable Tensor. Has the same type and format as "accum" .

## Attributes

use_locking: An optional bool. Defaults to "False".
    If "True", updating of the var and accum tensors will be protected by a lock;
    If "False", the behavior is undefined, but may exhibit less contention.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float32
- input1 accum: float32
- input2 lr: float32
- input3 l1: float32
- input4 l2: float32
- input5 grad: float32
- input6 indices: int32,int64
- output0 var: float32
- output1 accum: float32

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseApplyProximalAdagrad.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
