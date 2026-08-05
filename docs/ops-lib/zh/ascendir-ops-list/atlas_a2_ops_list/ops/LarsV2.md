# LarsV2

```c
REG_OP(LarsV2)
    .INPUT(w, TensorType(DT_FLOAT))
    .INPUT(g, TensorType(DT_FLOAT))
    .INPUT(weight_decay, TensorType(DT_FLOAT))
    .INPUT(learning_rate, TensorType(DT_FLOAT))
    .OUTPUT(g_new, TensorType(DT_FLOAT))
    .ATTR(hyperpara, Float, 0.001)
    .ATTR(epsilon, Float, 0.00001)
    .ATTR(use_clip, Bool, false)
    .OP_END_FACTORY_REG(LarsV2)
```

## Brief

Update "g" according to the LARS algorithm . 

## Inputs

Four inputs, including:
- w: A Tensor. Must be of type TensorType::DT_FLOAT. Support format: [FRACTAL_Z,C1HWNCoC0,NC1HWC0,ND].
- g: A Tensor of the same type and shape as "w". Support format: [FRACTAL_Z,C1HWNCoC0,NC1HWC0,ND].
- weight_decay: A Tensor of the same type as "w",  Must be a scalar. Support format: [ND].
- learning_rate: A Tensor of the same type as "w", Must be a scalar . Support format: [ND].

## Outputs

g_new: Tensor of the same type as "w".

## Attributes

Three Attributes, including:
- hyperpara: An optional float. Default value is 0.001.
- epsilon: An optional float. Default value is 1e-5.Avoid denominator is 0.
- use_clip: An optional bool. Defaults to "False".
    If "True", updating learning rate . 


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
