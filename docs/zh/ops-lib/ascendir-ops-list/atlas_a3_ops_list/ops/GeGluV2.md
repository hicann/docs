# GeGluV2

```c
REG_OP(GeGluV2)
    .INPUT(x, "T")
    .OUTPUT(y, "T")
    .OUTPUT(gelu, "T")
    .DATATYPE(T, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .ATTR(dim, Int, -1)
    .ATTR(approximate, Int, 1)
    .ATTR(activate_left, Bool, false)
    .OP_END_FACTORY_REG(GeGluV2)
```

## Brief

Compute the GeGluV2,
where the activations function in GLU is Gelu.

## Inputs

x: A Tensor. Must be one of the following types: bfloat16, float16, float32.
Shape supports at least 1 dimensions, and at most 8 dimensions.
The length of the split dimension in x must be an even number.

## Outputs

Two outputs, including:
- y: A Tensor. Must be one of the following types: bfloat16, float16, float32.
The dtype of y must exactly same with input x.
The shape of y matches the shape of x in all dimensions except for the split dimension,
where its length is half of length of x's split dimension.
- gelu: A Tensor. Must be one of the following types: bfloat16, float16, float32.
The dtype of gelu must exactly same with input x.
The shape of gelu matches the shape of x in all dimensions except for the split dimension,
where its length is half of length of x's split dimension.

## Attributes

Three attributes, including:
- dim: An optional int. The dimension to be split, default is -1.
- approximate: An optional int. Which formula used for the activation computation.
The gelu approximation algorithm to use: 'none'(0) or 'tanh'(1), default is 'tanh'(1).
Atlas Inference Series Product only support 'tanh'(1).
- activate_left: An optional bool.
The gelu activate_left algorithm to use:
    'false'(activate right) or 'true'(activate left), defalut is 'false'(activate right).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
- output1 gelu: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
