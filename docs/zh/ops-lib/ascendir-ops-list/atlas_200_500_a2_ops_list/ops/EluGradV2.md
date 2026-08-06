# EluGradV2

```c
REG_OP(EluGradV2)
    .INPUT(grads, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(activations, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(alpha, Float, 1.0)
    .ATTR(scale, Float, 1.0)
    .ATTR(input_scale, Float, 1.0)
    .ATTR(is_result, Bool, false)
    .OP_END_FACTORY_REG(EluGradV2)
```

## Brief

Calculate the elu_grad_v2 function.
Applies the element-wise function:
Computes the backward for the elu.

## Inputs

Two inputs, including:
- grads: A tensor. Must be one of the following types:
    float16, float32, bfloat16.
- activations: A tensor. Must be one of the following types:
    float16, float32, bfloat16.

## Outputs

y: A Tensor with the same type and shape of grads's.

## Attributes

- alpha: scalar parameter of type float32, the same as elu forward function,
    it is a hyperparameter controls the value to which an ELU saturates for negative net input,
    default value = 1.0 .
- scale: scalar parameter of type float32, the same scale as elu forward function scale,
    default value = 1.0 .
- input_scale: scalar parameter of type float32, which adjusts the output when activations are less than zero
    default value = 1.0 .
- is_result: optional bool, if true, activations is result tensor,
    if false, activations is self tensor, default value is false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: float16,float32
- input1 activations: float16,float32
- output0 y: float16,float32

## Attention Constraints

Shapes and datatypes of grads and activations must be the same.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
