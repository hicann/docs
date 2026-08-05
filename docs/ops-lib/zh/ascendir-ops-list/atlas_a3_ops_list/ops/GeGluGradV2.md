# GeGluGradV2

```c
REG_OP(GeGluGradV2)
    .INPUT(dy, "T")
    .INPUT(x, "T")
    .INPUT(gelu, "T")
    .OUTPUT(dx, "T")
    .DATATYPE(T, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .ATTR(dim, Int, -1)
    .ATTR(approximate, Int, 1)
    .ATTR(activate_left, Bool, false)
    .OP_END_FACTORY_REG(GeGluGradV2)
```

## Brief

Computes the gradient of x through GeGluV2.

## Inputs

Three inputs, including:
- dy: A Tensor of the same type as "x".
The shape of dy matches the shape of x in all dimensions except for the split dimension,
where its length is half of the length of x's split dimension.
- x: A Tensor. Must be one of the following types: float16, bfloat16, float32.
Shape supports at least 1 dimension, and at most 8 dimensions.
The length of the split dimension in x must be an even number.
- gelu: A Tensor of the same type as "x".
The shape of gelu matches the shape of x in all dimensions except for the split dimension,
where its length is half of the length of x's split dimension.

## Outputs

dx: A Tensor. Has the same type as "x". Shape should be same as x.

## Attributes

- dim: An optional Int. The dimension to be split, default is -1.
- approximate: An optional Int. Determines which formula to use for the activation computation.
The gelu grad approximation algorithm to use: 0('none') or 1('tanh'), default is 1('tanh').
Atlas Inference Series Product only supports 'tanh'(1).
- activate_left: An optional Bool.
Whether the left side of x is used as an input parameter to the activation function,
default is false, use the right side.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: bfloat16,float16,float32
- input1 x: bfloat16,float16,float32
- input2 gelu: bfloat16,float16,float32
- output0 dx: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator GeGluGradV2.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
