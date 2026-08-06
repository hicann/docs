# ApplyAdamV2

```c
REG_OP(ApplyAdamV2)
    .INPUT(var, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .INPUT(m, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .INPUT(v, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .INPUT(lr, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .INPUT(beta1, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .INPUT(beta2, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .INPUT(epsilon, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .INPUT(grad, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .OPTIONAL_INPUT(max_grad_norm, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .INPUT(global_grad_norm, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .INPUT(weight_decay, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .OPTIONAL_INPUT(step_size, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .OUTPUT(var, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .OUTPUT(m, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .OUTPUT(v, TensorType({ DT_FLOAT, DT_FLOAT16 }))
    .ATTR(adam_mode, String, "adam")
    .OP_END_FACTORY_REG(ApplyAdamV2)
```

## Brief

Count adam result. 

## Inputs

Eleven inputs, including:
- var: A ND Tensor of weight. Support float16/float32.
- m: A ND Tensor of the 1st moment estimates. Datatype and shape are same as var.
- v: A ND Tensor of the 2nd moment estimates. Datatype and shape are same as var.
- lr: A ND Tensor of learning rate. Datatype is same as var. Shape (1, ).
- beta1: A ND Tensor of the exponential decay rate for the 1st moment estimates. Datatype is same as var. Shape (1, ).
- beta2: A ND Tensor of the exponential decay rate for the 2nd moment estimates. Datatype is same as var. Shape (1, ).
- epsilon: A ND Tensor for numerical stability. Datatype is same as var. Shape (1, ).
- grad: A ND Tensor. Datatype and shape are same as var.
- max_grad_norm: An Optional Tensor. Datatype is same as var. Shape (1, ).
- global_grad_norm: A ND Tensor. Datatype is same as var. Shape (1, ).
- weight_decay: A ND Tensor. Datatype is same as var. Shape (1, ).
- step_size: An Optional Tensor. Datatype is same as var. Shape (1, ).

## Outputs

Three inputs, including:
- var: A ND Tensor of weight. Datatype and shape are same as var.
- m: A ND Tensor of the 1st moment estimates. Datatype and shape are same as var.
- v: A ND Tensor of the 2nd moment estimates. Datatype and shape are same as var.

## Attributes

- adam_mode: An optional bool. Defaults to "adam".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 var: float16,float32
- input1 m: float16,float32
- input2 v: float16,float32
- input3 lr: float16,float32
- input4 beta1: float16,float32
- input5 beta2: float16,float32
- input6 epsilon: float16,float32
- input7 grad: float16,float32
- input8 max_grad_norm: float16,float32
- input9 global_grad_norm: float16,float32
- input10 weight_decay: float16,float32
- input11 step_size: float16,float32
- output0 var: float16,float32
- output1 m: float16,float32
- output2 v: float16,float32
### AI CPU
- input0 var: float16,float32
- input1 m: float16,float32
- input2 v: float16,float32
- input3 lr: float16,float32
- input4 beta1: float16,float32
- input5 beta2: float16,float32
- input6 epsilon: float16,float32
- input7 grad: float16,float32
- input8 max_grad_norm: float16,float32
- input9 global_grad_norm: float16,float32
- input10 weight_decay: float16,float32
- input11 step_size: float16,float32
- output0 var: float16,float32
- output1 m: float16,float32
- output2 v: float16,float32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
