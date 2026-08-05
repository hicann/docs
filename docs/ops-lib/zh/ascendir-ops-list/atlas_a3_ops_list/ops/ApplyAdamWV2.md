# ApplyAdamWV2

```c
REG_OP(ApplyAdamWV2)
    .INPUT(var, TensorType::FLOAT())
    .INPUT(m, TensorType::FLOAT())
    .INPUT(v, TensorType::FLOAT())
    .INPUT(grad, TensorType::FLOAT())
    .INPUT(step, TensorType({DT_FLOAT, DT_INT64}))
    .OPTIONAL_INPUT(max_grad_norm, TensorType::FLOAT())
    .ATTR(lr, Float, 0.1f)
    .ATTR(beta1, Float, 0.1f)
    .ATTR(beta2, Float, 0.1f)
    .ATTR(weight_decay, Float, 0.1f)
    .ATTR(eps, Float, 0.1f)
    .ATTR(amsgrad, Bool, false)
    .ATTR(maximize, Bool, false)
    .OP_END_FACTORY_REG(ApplyAdamWV2)
```

## Brief

Updates "var" "m" "v" and "max_grad_norm" according to the AdamWV2 algorithm.

## Inputs

- var: A Tensor, dtype is float16 bfloat16 or float32, default is ND.
- m: A Tensor of the same type as "var", default is ND.
- v: A Tensor of the same type as "var", default is ND.
- grad: A Tensor, dtype is float16 bfloat16 or float32, for the gradient, default is ND.
- step: A Tensor, dtype is float32 or int64.
- max_grad_norm: An optional Tensor of the same type as "grad", default is ND.

## Attributes

- lr: A required float, default is 0.1
- beta1: A required float, default is 0.1
- beta2: A required float,default is 0.1
- weight_decay: A required float, default is 0.1
- eps: A required float, default is 0.1
- amsgrad: A required bool, default is false.
- maximize: A required bool, default is false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: bfloat16,float16,float32
- input1 m: bfloat16,float16,float32
- input2 v: bfloat16,float16,float32
- input3 grad: bfloat16,float16,float32
- input4 step: float32,int64
- input5 max_grad_norm: bfloat16,float16,float32

## Attention Constraints

 The input tensors must have the same shape, except for the step. The shape of step must be (1,).
 When the data types of the input tensors var,m,v,grad,max_grad_norm are the same, the data type can be
 float16,bfloat16 or float32.
 The data types of the input tensors var,m and v must be the same.For example,if var tensor is float16,
 the data types of m and v must also be float16.
 The data tytpes of the input tensors grad and max_grad_norm must be the same.For example,if grad tensor is float16,
 the data types of max_grad_norm must also be float16.
 When data type of the input tensor var,m and v are different with input tensor grad and max_grad_norm,
 the data types of var,m and v can only be float32,and the data type of grad and max_grad_norm tensor
 can only be float16 or bfloat16.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
