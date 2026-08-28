# InplaceApplyProximalAdagrad

```c
REG_OP(InplaceApplyProximalAdagrad)
    .INPUT(var, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(accum, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(lr, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(l1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(l2, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(grad, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(var, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(accum, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(use_locking, Bool, false)
    .OP_END_FACTORY_REG(InplaceApplyProximalAdagrad)
```

```c
  accum_new = accum + grad * grad
  eta = lr / sqrt(accum_new)
  prox = var - eta * grad
  if l1 > 0:
      var_new = sign(prox) * max(|prox| - eta * l1, 0) / (1 + eta * l2)
  else:
      var_new = prox / (1 + eta * l2)
  var = var_new
  accum = accum_new
```

## Brief

Inplace update "var" and "accum" according to FOBOS (Forward-Backward Splitting)
  with Adagrad learning rate. 

## Inputs

Six inputs, including:
- var: A mutable tensor. Must be one of FLOAT32/FLOAT16/BF16. ND format.
   Should be from a Variable().
- accum: A mutable tensor. Has the same type and shape as "var". ND format.
   Should be from a Variable().
- lr: A scalar tensor. Has the same type as "var". ND format.
   Learning rate scaling factor.
- l1: A scalar tensor. Has the same type as "var". ND format.
   L1 regularization strength.
- l2: A scalar tensor. Has the same type as "var". ND format.
   L2 regularization strength.
- grad: A tensor for the gradient. Has the same type and shape as "var". ND format.

## Outputs

Two outputs, including:
- var: A mutable tensor. Has the same type and shape as input "var".
   Inplace alias of input var. ND format.
- accum: A mutable tensor. Has the same type and shape as input "accum".
   Inplace alias of input accum. ND format. 

## Attributes

- use_locking: An optional bool. Defaults to "False".
   If "True", updating of the "var" and "accum" tensors will be protected by a lock;
   otherwise the behavior is undefined, but may exhibit less contention. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: bfloat16,float16,float32
- input1 accum: bfloat16,float16,float32
- input2 lr: bfloat16,float16,float32
- input3 l1: bfloat16,float16,float32
- input4 l2: bfloat16,float16,float32
- input5 grad: bfloat16,float16,float32
- output0 var: bfloat16,float16,float32
- output1 accum: bfloat16,float16,float32

## Attention Constraints

- The input tensors var/accum/grad must have the same shape.
- All input tensors (var/accum/lr/l1/l2/grad) must have the same data type.

## Third-party framework compatibility

Compatible with the TensorFlow operator ApplyProximalAdagrad.


---

[Back to Operator Specifications (Ascend950)](../README.md)
