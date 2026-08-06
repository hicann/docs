# InplaceApplyCenteredRMSProp

```c
REG_OP(InplaceApplyCenteredRMSProp)
    .INPUT(var, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(mg, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(ms, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(mom, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(lr, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(rho, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(momentum, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(epsilon, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(grad, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(var, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(mg, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(ms, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(mom, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(InplaceApplyCenteredRMSProp)
```

## Brief

Centered RMSProp optimizer step with in-place state update.
      epsilon is inside sqrt (TF-aligned): sqrt(ms - mg² + ε)

## Inputs

Nine inputs, including:
- var: A ND Tensor. Must be one of: float16, float. Persistent state (in-place updated).
- mg: A ND Tensor. Same shape/dtype as var. Mean gradient (in-place updated).
- ms: A ND Tensor. Same shape/dtype as var. Mean square (in-place updated).
- mom: A ND Tensor. Same shape/dtype as var. Momentum buffer (in-place updated).
- lr: A scalar Tensor (rank 0 or [1]). Learning rate.
- rho: A scalar Tensor (rank 0 or [1]). Decay rate (smoothing constant).
- momentum: A scalar Tensor (rank 0 or [1]). Momentum factor.
- epsilon: A scalar Tensor (rank 0 or [1]). Numerical stability constant (inside sqrt).
- grad: A ND Tensor. Same shape/dtype as var. Gradient.

## Outputs

Four outputs (in-place alias with corresponding inputs):
- var: Updated weight (shares GM address with input var).
- mg: Updated mean gradient (shares GM address with input mg).
- ms: Updated mean square (shares GM address with input ms).
- mom: Updated momentum buffer (shares GM address with input mom).

## Attributes

- use_locking: Bool, default false. Reserved for TF compatibility.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float16,float32
- input1 mg: float16,float32
- input2 ms: float16,float32
- input3 mom: float16,float32
- input4 lr: float16,float32
- input5 rho: float16,float32
- input6 momentum: float16,float32
- input7 epsilon: float16,float32
- input8 grad: float16,float32
- output0 var: float16,float32
- output1 mg: float16,float32
- output2 ms: float16,float32
- output3 mom: float16,float32

## Third-party framework compatibility

Compatible with TensorFlow ResourceApplyCenteredRMSProp (epsilon inside sqrt).


---

[Back to Operator Specifications (Ascend950)](../README.md)
