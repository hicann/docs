# ClippedSwigluGrad

```c
REG_OP(ClippedSwigluGrad)
    .INPUT(grad_y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .OPTIONAL_INPUT(group_index, TensorType({DT_INT64}))
    .OUTPUT(grad_x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .ATTR(dim, Int, -1)
    .ATTR(alpha, Float, 1.702)
    .ATTR(limit, Float, 7.0)
    .ATTR(bias, Float, 1.0)
    .ATTR(interleaved, Bool, true)
    .OP_END_FACTORY_REG(ClippedSwigluGrad)
```

## Brief

Compute the ClippedSwigluGrad,
where the activations function in GLU is SwishGrad.

## Inputs

Three inputs, including:
- grad_y: A Tensor, which is the output gradient of forward operator and which
has the same shape as "x" except for the dimension specified by the "dim" parameter.
The dimension size specified by "dim" is half of the corresponding dimension of x.
Must be one of the following types: bfloat16, float16, float32.
- x: A Tensor. Must be one of the following types: bfloat16, float16, float32.
- group_index: An optional tensor. Shape is (N,). Type is int64.

## Outputs

one Output, including:
grad_x: A Tensor, which is the gradient of x and has the same shape as "x".
Must be one of the following types: bfloat16, float16, float32.

## Attributes

Five attributes, including:
- dim: An optional int. The dimension to be split, value in [-xDim, xDim-1], default is -1.
- alpha: An optional float. The activation coefficient for the GLU activation function, default is 1.702.
- limit: An optional float. The threshold limit for SWIGLU input, default is 7.0.
- bias: An optional float. The bias applied during SWIGLU linear computation, default is 1.0.
- interleaved: An optional bool. The way of splitting x: true for interleaved splitting,
false for front-back splitting, default is true.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad_y: bfloat16,float16,float32
- input1 x: bfloat16,float16,float32
- input2 group_index: int64
- output0 grad_x: bfloat16,float16,float32

## Attention Constraints

The dim dimension of x must be divisible by 2, and the dim dimension of grad_y must be equal
to the dim dimension of x divided by 2.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
