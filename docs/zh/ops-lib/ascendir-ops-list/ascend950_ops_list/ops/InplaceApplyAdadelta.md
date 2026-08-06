# InplaceApplyAdadelta

```c
REG_OP(InplaceApplyAdadelta)
    .INPUT(var, TensorType::NumberType())
    .INPUT(accum, TensorType::NumberType())
    .INPUT(accum_update, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(rho, TensorType::NumberType())
    .INPUT(epsilon, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .OUTPUT(accum, TensorType::NumberType())
    .OUTPUT(accum_update, TensorType::NumberType())
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(InplaceApplyAdadelta)
```

## Brief

Update '*var' according to the Adadelta algorithm (V2, three explicit
       in-place outputs).
  accum_new        = rho * accum + (1 - rho) * grad^2
  update           = sqrt(accum_update + epsilon) / sqrt(accum_new + epsilon) * grad
  var_new          = var - lr * update
  accum_update_new = rho * accum_update + (1 - rho) * update^2

## Inputs

 7 Tensor inputs:
  @li var:          A Tensor of type float16 or float32. Weight to update.
  @li accum:        A Tensor of type float16 or float32. Gradient squared accumulator.
  @li accum_update: A Tensor of type float16 or float32. Update squared accumulator.
  @li lr:           Scalar Tensor ([1]) learning rate.
  @li rho:          Scalar Tensor ([1]) decay rate, range [0, 1).
  @li epsilon:      Scalar Tensor ([1]) numerical-stability constant, must be > 0.
  @li grad:         A Tensor, same shape/dtype as var.

## Outputs

 3 Tensor outputs (each in-place aliased to its corresponding input):
  @li var:          Updated var (in-place alias of input var).
  @li accum:        Updated accum (in-place alias of input accum).
  @li accum_update: Updated accum_update (in-place alias of input accum_update).

## Attributes

  @li use_locking: An optional bool. Defaults to "false". Semantic placeholder.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float16,float32
- input1 accum: float16,float32
- input2 accum_update: float16,float32
- input3 lr: float16,float32
- input4 rho: float16,float32
- input5 epsilon: float16,float32
- input6 grad: float16,float32
- output0 var: float16,float32
- output1 accum: float16,float32
- output2 accum_update: float16,float32

## Third-party framework compatibility

Compatible with the reference ApplyAdadelta contract (three in-place outputs
reflect the Adadelta algorithm's full in-place update semantics).


---

[Back to Operator Specifications (Ascend950)](../README.md)
