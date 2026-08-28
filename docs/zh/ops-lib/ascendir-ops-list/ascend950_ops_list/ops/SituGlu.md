# SituGlu

```c
REG_OP(SituGlu)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(dim, Int, -1)
    .ATTR(beta, Float, 1.0)
    .ATTR(linear_beta, Float, 0.0)
    .ATTR(activate_left, Bool, true)
    .OP_END_FACTORY_REG(SituGlu)
```

## Brief

SiTU gated linear unit activation.

## Inputs

One input:
- x: A tensor. Type is float32/float16/bfloat16. The dim dimension must be divisible by 2.

## Outputs

One output:
y: A tensor. Type is float32/float16/bfloat16. The dim dimension is half of x.

## Attributes

Four attributes:
- dim: An optional int. The dimension to be split, value in [-xDim, xDim-1], default is -1.
- beta: An optional float. The scale factor for the SiTU gate activation, default is 1.0.
- linear_beta: An optional float. The scale factor for the linear tanh on the up path. When <= 0, the up path is
  used as-is. default is 0.0.
- activate_left: An optional bool. Whether the left (front) half of x is the gate. true: gate is the front half and
  up is the back half; false: gate is the back half and up is the front half. default is true.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Attention Constraints

The dim dimension of x must be divisible by 2, and the dim dimension of y must be equal to the dim dimension of x
divided by 2.


---

[Back to Operator Specifications (Ascend950)](../README.md)
