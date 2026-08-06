# InplaceApplyKerasMomentum

```c
REG_OP(InplaceApplyKerasMomentum)
    .INPUT(var, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(accum, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(lr, TensorType({DT_FLOAT}))
    .INPUT(grad, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(momentum, TensorType({DT_FLOAT}))
    .OUTPUT(var, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(accum, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(use_locking, Bool, false)
    .ATTR(use_nesterov, Bool, false)
    .OP_END_FACTORY_REG(InplaceApplyKerasMomentum)
```

## Brief

Updates '*var' according to the Keras momentum scheme (inplace dual output).
  accum_new = accum * momentum - grad * lr
  if use_nesterov is True:
      var += momentum * accum_new - grad * lr
  else:
      var += accum_new
  accum = accum_new

## Inputs

- var: A mutable tensor. Must be one of FLOAT32/FLOAT16/BF16. Should be from a Variable().
- accum: A mutable tensor. Has the same type as "var". Should be from a Variable().
- lr: A scalar tensor of FLOAT32. Learning rate.
- grad: A tensor for the gradient. Has the same type as "var".
- momentum: A scalar tensor of FLOAT32. Momentum coefficient.

## Outputs

- var: A mutable tensor. Has the same type as input "var". inplace_with(var).
- accum: A mutable tensor. Has the same type as input "accum". inplace_with(accum).

## Attributes

- use_locking: An optional bool. Defaults to "False".
   If "True", updating of the "var" tensor is protected by a lock;
   NPU 单流执行忽略，保留属性兼容 TF ResourceApplyKerasMomentum。
- use_nesterov: An optional bool. Defaults to "False".
   If "True", var will be updated by using Nesterov momentum.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: bfloat16,float16,float32
- input1 accum: bfloat16,float16,float32
- input2 lr: float32
- input3 grad: bfloat16,float16,float32
- input4 momentum: float32
- output0 var: bfloat16,float16,float32
- output1 accum: bfloat16,float16,float32

## Attention Constraints

The input tensors var/accum/grad must have the same shape.

## Third-party framework compatibility

Compatible with the TensorFlow operator ResourceApplyKerasMomentum.


---

[Back to Operator Specifications (Ascend950)](../README.md)
