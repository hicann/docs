# GeluGradV2

```c
REG_OP(GeluGradV2)
    .INPUT(dy, "T")
    .INPUT(x, "T")
    .OUTPUT(z, "T")
    .DATATYPE(T, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT}))
    .ATTR(approximate, String, "none")
    .OP_END_FACTORY_REG(GeluGradV2)
```

## Brief

Computes the gradient for the gelu of "x" .

## Inputs

Two inputs, including:
- dy: A Tensor. Support 1D ~ 8D. Must be one of the following types:bfloat16, float16, float32.
- x: A Tensor of the same type and format as "dy".

## Outputs

z: A Tensor. Has the same type, shape and format as "dy".

## Attributes

approximate: A optional string.
The gelu grad approximation algorithm to use: 'none' or 'tanh', default is 'none'. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 dy: float16,float32
- input1 x: float16,float32
- output0 z: float16,float32

## Attention Constraints

if the GeluGradV2 operator has approximate='none':
when x is -inf, the computation result is 0.
when x is inf, the computation result is dy.

## Third-party framework compatibility

Compatible with the Pytorch operator GeluGrad.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
