# ApplyFusedEmaAdam

```c
REG_OP(ApplyFusedEmaAdam)
    .INPUT(grad, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(var, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(m, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(v, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(s, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(step, TensorType({DT_INT64}))
    .OUTPUT(var, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(m, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(v, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(s, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .ATTR(lr, Float, 1e-3f)
    .ATTR(ema_decay, Float, 0.9999)
    .ATTR(beta1, Float, 0.9)
    .ATTR(beta2, Float, 0.999)
    .ATTR(eps, Float, 1e-8f)
    .ATTR(mode, Int, 1)
    .ATTR(bias_correction, Bool, true)
    .ATTR(weight_decay, Float, 0.0)
    .OP_END_FACTORY_REG(ApplyFusedEmaAdam)
```

## Brief

A fusion operator for fused Ema-Adam.

## Inputs

Six inputs, including:
- grad: A Tensor with ND format specifying gradient. Support float16, float32, bfloat16.
- var: A Tensor with ND format specifying parameters to be updated. Support float16, float32, bfloat16.
- m: A Tensor with ND format specifying first moment. Support float16, float32, bfloat16.
- v: A Tensor with ND format specifying second moment. Support float16, float32, bfloat16.
- s: A Tensor with ND format specifying weight of EMA. Support float16, float32, bfloat16.
- step: A Tensor with ND format specifying time step. Support int64.

## Outputs

Four outputs, including:
- var: A Tensor specifying updated parameters. Must be one of the following types: float16, float32, bfloat16.
- m: A Tensor specifying updated first moment. Must be one of the following types: float16, float32, bfloat16.
- v: A Tensor specifying updated second moment. Must be one of the following types: float16, float32, bfloat16.
- s: A Tensor specifying updated weight of EMA. Must be one of the following types: float16, float32, bfloat16.

## Attributes

- lr: A Float specifying the learning rate. Optional and defaults to "1e-3".
- ema_decay: A Float specifying ema decay. Must be between 0 and 1. Optional and defaults to "0.9999".
- beta1: A Float used for computing running averages of gradient. Optional and defaults to "0.9".
- beta2: A Float used for computing running averages of gradient's square. Optional and defaults to "0.999".
- eps: A Float ued for improving numerical stability. Optional and defaults to "1e-8".
- mode: An Integer must be 1 or 0. Set to "1" for AdamW and "0" for L2 regularization. Optional and defaults to "1".
- bias_correction: A bool. Set to "true" for bias correction and "false" for no correction. Optional and defaults to "true".
- weight_decay: A Float specifying weight decay. Optional and defaults to "0".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad: bfloat16,float16,float32
- input1 var: bfloat16,float16,float32
- input2 m: bfloat16,float16,float32
- input3 v: bfloat16,float16,float32
- input4 s: bfloat16,float16,float32
- input5 step: int64
- output0 var: bfloat16,float16,float32
- output1 m: bfloat16,float16,float32
- output2 v: bfloat16,float16,float32
- output3 s: bfloat16,float16,float32

## Attention Constraints

- grad, var, m, s and v are required to be of the same datatype and shape.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
