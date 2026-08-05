# SparseApplyFtrlV2

```c
REG_OP(SparseApplyFtrlV2)
    .INPUT(var, TensorType({DT_FLOAT}))
    .INPUT(accum, TensorType({DT_FLOAT}))
    .INPUT(linear, TensorType({DT_FLOAT}))
    .INPUT(grad, TensorType({DT_FLOAT}))
    .INPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .INPUT(lr, TensorType({DT_FLOAT}))
    .INPUT(l1, TensorType({DT_FLOAT}))
    .INPUT(l2, TensorType({DT_FLOAT}))
    .INPUT(l2_shrinkage, TensorType({DT_FLOAT}))
    .INPUT(lr_power, TensorType({DT_FLOAT}))
    .OUTPUT(var, TensorType({DT_FLOAT}))
    .OUTPUT(accum, TensorType({DT_FLOAT}))
    .OUTPUT(linear, TensorType({DT_FLOAT}))
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(SparseApplyFtrlV2)
```

## Brief

Updates relevant entries in '*var' according to the Ftrl-proximal scheme.
That is for rows we have grad for, "var", "accum" and "linear" are updated . 

## Inputs

Ten inputs, including:
- var: A mutable Tensor. Must be of type TensorType::NumberType().
    Should be a Variable Tensor.
    Support dtype: float32, support format: [NCHW,NHWC,ND].
- accum: A mutable Tensor of the same type as "var".
    Should be a Variable Tensor.
    Support dtype: float32, support format: [NCHW,NHWC,ND].
- linear: A mutable Tensor of the same type as "var".
    Should be a Variable Tensor.
    Support dtype: float32, support format: [NCHW,NHWC,ND].
- grad: A Tensor of the same type as "var", for the gradient.
    Support dtype: float32, support format: [NCHW,NHWC,ND].
- indices: A vector of indices into the first dimension of "var" and "accum".
    The value of indices must be unique. Otherwise, the result is unpredictable . 
    Support dtype: int32, int64, support format: [ND].
- lr: A Tensor of the same type as "var", for the scaling factor. Must be a scalar.
    Support dtype: float32, support format: [ND].
- l1: A Tensor of the same type as "var", for L1 regulariation. Must be a scalar.
    Support dtype: float32, support format: [ND].
- l2: A Tensor of the same type as "var", for L2 regulariation. Must be a scalar.
    Support dtype: float32, support format: [ND].
- l2_shrinkage: A Tensor of the same type as "var", L2 shrinkage regulariation. Must be a scalar.
    Support dtype: float32, support format: [ND].
- lr_power: A Tensor of the same type as "var", for the scaling factor. Must be a scalar .
    Support dtype: float32, support format: [ND]. 

## Outputs

- var: A Tensor. Has the same type and format as input "var" .
- accum: A Tensor. Has the same type and format as input "accum".
- linear: A Tensor. Has the same type and format as input "linear" .

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
- input4 indices: int32,int64
- input5 lr: float32
- input6 l1: float32
- input7 l2: float32
- input8 l2_shrinkage: float32
- input9 lr_power: float32
- output0 var: float32
- output1 accum: float32
- output2 linear: float32

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseApplyFtrlV2.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
