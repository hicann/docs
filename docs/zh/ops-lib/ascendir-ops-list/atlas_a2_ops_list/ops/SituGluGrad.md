# SituGluGrad

```c
REG_OP(SituGluGrad)
    .INPUT(grad_y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(grad_x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(dim, Int, -1)
    .ATTR(beta, Float, 1.0)
    .ATTR(linear_beta, Float, 0.0)
    .ATTR(activate_left, Bool, true)
    .OP_END_FACTORY_REG(SituGluGrad)
```

## Brief

SiTU gated linear unit backward.

## Inputs

Two inputs:
- grad_y: A tensor. Type is float32/float16/bfloat16. The dim dimension is half of x.
- x: A tensor. Type is float32/float16/bfloat16. The dim dimension must be divisible by 2.

## Outputs

One output:
grad_x: A tensor. Type is float32/float16/bfloat16. The shape is the same as x.

## Attributes

Four attributes:
- dim: An optional int. The dimension to be split, value in [-xDim, xDim-1], default is -1.
- beta: An optional float. The scale factor for the SiTU gate activation, default is 1.0.
- linear_beta: An optional float. The scale factor for the linear tanh on the up path. When <= 0, the up path is
  used as-is. default is 0.0.
- activate_left: An optional bool. Whether the left (front) half of x is the gate. default is true.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad_y: bfloat16,float16,float32
- input1 x: bfloat16,float16,float32
- output0 grad_x: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
