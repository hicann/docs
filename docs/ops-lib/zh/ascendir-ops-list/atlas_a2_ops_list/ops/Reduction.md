# Reduction

```c
REG_OP(Reduction)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(operation, Int, 1)
    .ATTR(axis, Int, 0)
    .ATTR(coeff, Float, 1.0)
    .OP_END_FACTORY_REG(Reduction)
```

## Brief

Compute reduction on dimensions specified by "axis".
Four reduction operations are provided:
SUM     Computes the sum of elements across specified dimensions of a tensor.
ASUM    Computes the sum of absolute values of elements across specified
dimensions of a tensor.
SUMSQ   Computes the sum of squares of elements across specified
dimensions of a tensor.
SUMSQ   Computes the mean values of elements across specified
dimensions of a tensor .

## Inputs

x: A Tensor of type float16 or float32. Support 1D ~ 8D, Support format:["ND", "NC1HWC0"].

## Outputs

y: A Tensor. Has the same type as "x". Support 1D ~ 3D, Support format:["ND", "NC1HWC0"].

## Attributes

- operation: An optional int32 from 1(SUM), 2(ASUM), 3(SUMSQ), and 4(MEAN),
specifying the reduction algorithm. Defaults to "1".
- axis: An optional int32, specifying the first axis to reduce.
Defaults to "0".
The value range is [-N, N-1], where N is the input tensor rank.
- coeff: An optional float32, specifying the scale coefficient.
Defaults to "1.0" . 

## Third-party framework compatibility

Compatible with the Caffe operator Reduction.

## Attention Constraints: The Reduction operator supports type float16

only on the device chip.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
