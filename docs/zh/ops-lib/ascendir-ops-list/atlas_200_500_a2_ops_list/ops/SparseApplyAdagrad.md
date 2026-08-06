# SparseApplyAdagrad

```c
REG_OP(SparseApplyAdagrad)
    .INPUT(var, TensorType({DT_FLOAT}))
    .INPUT(accum, TensorType({DT_FLOAT}))
    .INPUT(lr, TensorType({DT_FLOAT}))
    .INPUT(grad, TensorType({DT_FLOAT}))
    .INPUT(indices, TensorType({DT_INT32}))
    .OUTPUT(var, TensorType({DT_FLOAT}))
    .OUTPUT(accum, TensorType({DT_FLOAT}))
    .ATTR(use_locking, Bool, false)
    .ATTR(update_slots, Bool, true)
    .OP_END_FACTORY_REG(SparseApplyAdagrad)
```

## Brief

Updates relevant entries in "var" and "accum" according to the adagrad scheme . 

## Inputs

Five inputs, including:
- var: An NCHW, NHWC, or ND Tensor of type float32.
- accum: An NCHW, NHWC, or ND Tensor of type float32.
- lr: An NCHW, NHWC, or ND Tensor of type float32.
- grad: An NCHW, NHWC, or ND Tensor of type float32.
- indices: An NCHW, NHWC, or ND Tensor of type float32 .
The value of indices must be unique. Otherwise, the result is unpredictable . 

## Outputs

var: A Tensor. Has the same type and format as input "var" . 

## Attributes

- use_locking: An optional bool. Defaults to "False". If "True", the operation will be protected by a lock.
- update_slots: An optional bool. Defaults to "True". If "True", the calcution will be different as "False" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float32
- input1 accum: float32
- input2 lr: float32
- input3 grad: float32
- input4 indices: int32,int64
- output0 var: float32
- output1 accum: float32

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseApplyAdagrad.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
