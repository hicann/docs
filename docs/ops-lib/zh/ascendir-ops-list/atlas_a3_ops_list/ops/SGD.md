# SGD

```c
REG_OP(SGD)
    .INPUT(parameters, TensorType(DT_FLOAT, DT_FLOAT16, DT_BF16))
    .INPUT(gradient, TensorType(DT_FLOAT, DT_FLOAT16, DT_BF16))
    .INPUT(learning_rate, TensorType(DT_FLOAT, DT_FLOAT16, DT_BF16))
    .INPUT(accum, TensorType(DT_FLOAT, DT_FLOAT16, DT_BF16))
    .INPUT(momentum, TensorType(DT_FLOAT, DT_FLOAT16, DT_BF16))
    .INPUT(stat, TensorType(DT_FLOAT, DT_FLOAT16, DT_BF16))
    .OUTPUT(parameters, TensorType(DT_FLOAT, DT_FLOAT16, DT_BF16))
    .ATTR(dampening, Float, 0.0)
    .ATTR(weight_decay, Float, 0.0)
    .ATTR(nesterov, Bool, false)
    .OP_END_FACTORY_REG(SGD)
```

## Brief

Implements stochastic gradient descent (optionally with momentum).
Nesterov momentum is based on the formula from
On the importance of initialization and momentum in deep learning.

## Inputs

- parameters: A mutable tensor of type float16, float32 or bfloat16.
Support format: [NC1HWC0,NDC1HWC0,ND,FRACTAL_Z,FRACTAL_Z_3D].
Specifies the iterable of parameters to optimize or dicts defining parameter
groups.
- gradient: A tensor of type float16, float32 or bfloat16.
Support format: [NC1HWC0,NDC1HWC0,ND,FRACTAL_Z,FRACTAL_Z_3D].
Specifies the gradient of training step.
- learning_rate: A tensor of type float16, float32 or bfloat16.
Support format: [ND].
Specifies the learing_rate of training step.
- accum: A tensor of type float16, float32 or bfloat16.
Support format: [NC1HWC0,NDC1HWC0,ND,FRACTAL_Z,FRACTAL_Z_3D].
Specifies the velocity of training step.
- momentum: A tensor of type float16, float32 or bfloat16.
Support format: [ND].
Specifies the momentum factor.
- stat: A tensor of type float16, float32 or bfloat16.
Support format: [NC1HWC0,NDC1HWC0,ND,FRACTAL_Z,FRACTAL_Z_3D].
Specifies the status representing the first step or not . 

## Outputs

parameters: Tensor of the same type and format as input "parameters" . 
@see ApplyMomentum()

## Attributes

- dampening: An optional float, specifying the dampening for momentum.
Defaults to "0.0".
- weight_decay: An optional float, specifying the L2 penalty. Defaults to
"0.0".
- nesterov: An optional bool, specifying whether to enable Nesterov
momentum. Defaults to "False" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 parameters: bfloat16,float16,float32
- input1 gradient: bfloat16,float16,float32
- input2 learning_rate: bfloat16,float16,float32
- input3 accum: bfloat16,float16,float32
- input4 momentum: bfloat16,float16,float32
- input5 stat: bfloat16,float16,float32
- output0 parameters: bfloat16,float16,float32

## Third-party framework compatibility

- Compatible with the PyTorch operator SGD.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
