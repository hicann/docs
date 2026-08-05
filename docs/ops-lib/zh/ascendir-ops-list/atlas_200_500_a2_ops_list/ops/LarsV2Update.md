# LarsV2Update

```c
REG_OP(LarsV2Update)
    .INPUT(w, TensorType(DT_FLOAT))
    .INPUT(g, TensorType(DT_FLOAT))
    .INPUT(w_square_sum, TensorType(DT_FLOAT))
    .INPUT(g_square_sum, TensorType(DT_FLOAT))
    .INPUT(weight_decay, TensorType(DT_FLOAT))
    .INPUT(learning_rate, TensorType(DT_FLOAT))
    .OUTPUT(g_new, TensorType(DT_FLOAT))
    .ATTR(hyperpara, Float, 0.001)
    .ATTR(epsilon, Float, 0.00001)
    .ATTR(use_clip, Bool, false)
    .OP_END_FACTORY_REG(LarsV2Update)
```

## Brief

Update "g" according to the LARS algorithm . 

## Inputs

Six inputs, including:
- w: A ND Tensor. Must be of type float32
- g: A ND Tensor of the same type and shape as "w".
- w_square_sum: A 1D Tensor of  square_sum(w), has the same type as "w",  Must be a scalar or 1D tensor.
- g_square_sum: A 1D Tensor of  square(g), has the same type as "w", Must be a scalar or 1D tensor.
- weight_decay: A 1D Tensor of the same type as "w",  Must be a scalar or 1D tensor.
- learning_rate: A 1D Tensor of the same type as "w", Must be a scalar or 1D tensor.

## Outputs

g_new: a ND Tensor of the same type as "w".

## Attributes

Three Attributes, including:
- hyperpara: An optional float. Default value is 0.001.
- epsilon: An optional float. Default value is 1e-5.Avoid denominator is 0.
- use_clip: An optional bool. Defaults to "False".
    If "True", updating learning rate . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 w: float32
- input1 g: float32
- input2 w_square_sum: float32
- input3 g_square_sum: float32
- input4 weight_decay: float32
- input5 learning_rate: float32
- output0 g_new: float32


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
