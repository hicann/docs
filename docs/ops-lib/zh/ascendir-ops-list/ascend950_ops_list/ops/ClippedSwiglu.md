# ClippedSwiglu

```c
REG_OP(ClippedSwiglu)
        .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
        .OPTIONAL_INPUT(group_index, TensorType({DT_INT64}))
        .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
        .ATTR(dim, Int, -1)
        .ATTR(alpha, Float, 1.702)
        .ATTR(limit, Float, 7.0)
        .ATTR(bias, Float, 1.0)
        .ATTR(interleaved, Bool, true)
        .OP_END_FACTORY_REG(ClippedSwiglu)
```

## Brief

Activation function of SwiGlu with clipping.

## Inputs

Two inputs, including:
- x: A tensor. Type is bfloat16, float16, float32.
- group_index: An optional tensor. Shape is (N,). Type is int64.

## Outputs

one output, including:
y: A tensor. Type is bfloat16, float16, float32.

## Attributes

Five attributes, including:
- dim: An optional int. The dimension to be split, value in [-xDim, xDim-1], default is -1.
- alpha: An optional float. The activation coefficient for the GLU activation function, default is 1.702.
- limit: An optional float. The threshold limit for SWIGLU input, default is 7.0.
- bias: An optional float. The bias applied during SWIGLU linear computation, default is 1.0.
- interleaved: An optional bool. The way of splitting x: true for interleaved splitting, false for front-back splitting, default is true.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- input1 group_index: int64
- output0 y: bfloat16,float16,float32

## Attention Constraints

The dim dimension of x must be divisible by 2, and the dim dimension of y must be equal to the dim dimension of x divided by 2.


---

[Back to Operator Specifications (Ascend950)](../README.md)
