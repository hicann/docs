# GaussianBlur

```c
REG_OP(GaussianBlur)
    .INPUT(x, "T")
    .OUTPUT(y, "T")
    .REQUIRED_ATTR(kernel_size, ListInt)
    .REQUIRED_ATTR(sigma, ListFloat)
    .ATTR(padding_mode, String, "constant")
    .DATATYPE(T, TensorType({DT_UINT8, DT_FLOAT}))
    .OP_END_FACTORY_REG(GaussianBlur)
```

## Brief

Applies a gaussian blur to an image. 

## Inputs

- x: An NCHW or NHWC tensor of type T.
- matrix: transformation matrix, format ND , shape must be (2, 3), type must be float32.

## Outputs

y: output tensor, has the same type and shape as input x. 

## Attributes

- kernel_size: A required ListInt.
contain 2 elements: [size_width, size_height].
every element must be 1 or 3 or 5.
- sigma: A required ListFloat.
contain 2 elements: [sigma_x, sigma_y].
- padding_mode: An optional string. padding mode, only support "constant" and "reflect", default "constant".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### Dvpp
- input0 x: float32,uint8
- output0 y: float32,uint8

## Attention Constraints

This operator will be deprecated in the future.

## DataType

- T: type of uint8 or float32.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
