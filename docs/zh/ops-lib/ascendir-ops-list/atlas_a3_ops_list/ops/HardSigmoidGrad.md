# HardSigmoidGrad

```c
REG_OP(HardSigmoidGrad)
    .INPUT(grads, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(input_x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(alpha, Float, 0.16666666)
    .ATTR(beta, Float, 0.5)
    .OP_END_FACTORY_REG(HardSigmoidGrad)
```

## Brief

Calculate the backward outputs of the function "hard_sigmoid"

## Inputs

Two inputs, including:
- grads: A ND tensor. The shape should be within the range of 0D to 8D.
    Must be one of the following types:float16, float32, bfloat16.
- input_x: A ND tensor. The shape should be within the range of 0D to 8D.
    Must be one of the following types: float16, float32, bfloat16.

## Outputs

One output, including:
y: A ND tensor with the same type and shape as 'input_x'.

## Attributes

- alpha: An optional float. Slope of the operator, defaults to 0.16666666.
- beta: An optional float. Offset of the operator, defaults to 0.5.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grads: bfloat16,float16,float32
- input1 input_x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator HardSigmoidGrad.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
