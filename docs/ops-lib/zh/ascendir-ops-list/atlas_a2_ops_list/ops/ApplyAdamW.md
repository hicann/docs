# ApplyAdamW

```c
REG_OP(ApplyAdamW)
    .INPUT(var, TensorType::NumberType())
    .INPUT(m, TensorType::NumberType())
    .INPUT(v, TensorType::NumberType())
    .INPUT(beta1_power, TensorType::NumberType())
    .INPUT(beta2_power, TensorType::NumberType())
    .INPUT(lr, TensorType::NumberType())
    .INPUT(weight_decay, TensorType::NumberType())
    .INPUT(beta1, TensorType::NumberType())
    .INPUT(beta2, TensorType::NumberType())
    .INPUT(epsilon, TensorType::NumberType())
    .INPUT(grad, TensorType::NumberType())
    .OPTIONAL_INPUT(max_grad_norm, TensorType::NumberType())
    .OUTPUT(var, TensorType::NumberType())
    .OUTPUT(m, TensorType::NumberType())
    .OUTPUT(v, TensorType::NumberType())
    .ATTR(amsgrad, Bool, false)
    .ATTR(maximize, Bool, false)
    .OP_END_FACTORY_REG(ApplyAdamW)
```

```c
 if maximize:
      gt = -grad
  else:
      gt = grad
  m_out = m * beta1 - (beta1 - 1) * gt
  v_out = v * beta2 - (beta2 - 1) * gt * gt
  var_t = var * (1 + (-lr * weight_decay))
  beta1_power_out = beta1_power * beta1
  beta2_power_out = beta2_power * beta2
  if amsgrad:
      max_grad_norm_out = max(max_grad_norm, v_out)
      denom = sqrt(-max_grad_norm_out / (beta2_power_out -1)) + epsilon
  else:
      denom = sqrt(-v_out / (beta2_power_out -1)) + epsilon
  var_out = var_t + ((lr / (beta1_power_out -1)) * (m_out / denom))
```

## Brief

Updates "var" according to the AdamW algorithm. For clarity, the output variable is suffixed with "_out" in the fomulas below (e.g. m_out).

## Inputs

- var: A tensor of ND, dtype is float16 bfloat16 or float32.
    Specifying parameters to be updated.
    Should be from a Variable().
- m: A tensor of ND, dtype is float16 bfloat16 or float32.
    Specifying first moment.
    Should be from a Variable().
- v: A tensor of ND, dtype is float16 bfloat16 or float32.
    Specifying second moment. Values must be greater than or equal to 0.
    Should be from a Variable().
- beta1_power: A scalar of the same type as "var", value is beta1^(step-1), between 0 and 1.
- beta2_power: A scalar of the same type as "var", value is beta2^(step-1), between 0 and 1.
- lr: Specifying learning_rate. A scalar of the same type as "var", value is between 0 and 1 generally (e.g. 1e-3).
- weight_decay: Specifying weight decay. A scalar of the same type as "var", value is between 0 and 1 generally (e.g. 1e-2).
- beta1: Specifying beta1. A scalar of the same type as "var", value is between 0 and 1 (e.g. 0.9).
- beta2: Specifying beta2. A scalar of the same type as "var", value is between 0 and 1 (e.g. 0.999).
- epsilon: A scalar of the same type as "var", used to improve numerical stability.
    Should be a minimum value greater than 0 (e.g. 1e-8).
- grad: A tensor of the same type as "var", dtype is float16 bfloat16 or float32.
    Specifying gradient.
- max_grad_norm: A mutable tensor of the same type as "var", an optional input,
    dtype is float16 bfloat16 or float32.
    Should be from a Variable().

## Outputs

- var: A mutable tensor. Has the same shape and type as input "var".
- m: A mutable tensor. Has the same shape and type as input "m".
- v: A mutable tensor. Has the same shape and type as input "v".

## Attributes

- amsgrad: An optional bool. Specifying using max_grad_norm in the calculation. Defaults to "False", only support "False".
- maximize: An optional bool. Specifying maximize the objective with respect to the params, instead of minimizing. Defaults to "False".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: bfloat16,float16,float32
- input1 m: bfloat16,float16,float32
- input2 v: bfloat16,float16,float32
- input3 beta1_power: bfloat16,float16,float32
- input4 beta2_power: bfloat16,float16,float32
- input5 lr: bfloat16,float16,float32
- input6 weight_decay: bfloat16,float16,float32
- input7 beta1: bfloat16,float16,float32
- input8 beta2: bfloat16,float16,float32
- input9 epsilon: bfloat16,float16,float32
- input10 grad: bfloat16,float16,float32
- input11 max_grad_norm: bfloat16,float16,float32
- output0 var: bfloat16,float16,float32
- output1 m: bfloat16,float16,float32
- output2 v: bfloat16,float16,float32

## attention Constraints

- The input tensors must have the same shape.
- Ensure the argument for the square root is non-negative.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
