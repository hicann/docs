# SparseApplyAdagradV2

```c
REG_OP(SparseApplyAdagradV2)
    .INPUT(var, TensorType({DT_FLOAT}))
    .INPUT(accum, TensorType({DT_FLOAT}))
    .INPUT(lr, TensorType({DT_FLOAT}))
    .INPUT(epsilon, TensorType({DT_FLOAT}))
    .INPUT(grad, TensorType({DT_FLOAT}))
    .INPUT(indices, TensorType({DT_INT32}))
    .OUTPUT(var, TensorType({DT_FLOAT}))
    .OUTPUT(accum, TensorType({DT_FLOAT}))
    .ATTR(use_locking, Bool, false)
    .ATTR(update_slots, Bool, true)
    .OP_END_FACTORY_REG(SparseApplyAdagradV2)
```

## Brief

Updates relevant entries in "var" and "accum" according to the adagrad scheme . 

## Inputs

Six inputs, including:
- var: An NCHW, NHWC, or ND Tensor of type float32.
- accum: An NCHW, NHWC, or ND Tensor of type float32.
- lr: An NCHW, NHWC, or ND Tensor of type float32.
- epsilon: An NCHW, NHWC, or ND Tensor of type float32.
- grad: An NCHW, NHWC, or ND Tensor of type float32.
- indices: An NCHW, NHWC, or ND Tensor of type float32 .
The value of indices must be unique. Otherwise, the result is unpredictable . 

## Outputs

- var: A Tensor. Has the same type and format as input "var" .
- accum: A Tensor. Has the same type and format as input "accum" .

## Attributes

- use_locking: An optional bool. Defaults to "False". If "True", the operation will be protected by a lock.
- update_slots: An optional bool. Defaults to "True". If "False", the computation logic will be different .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float32
- input1 accum: float32
- input2 lr: float32
- input3 epsilon: float32
- input4 grad: float32
- input5 indices: int32,int64
- output0 var: float32
- output1 accum: float32

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseApplyAdagradV2.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
