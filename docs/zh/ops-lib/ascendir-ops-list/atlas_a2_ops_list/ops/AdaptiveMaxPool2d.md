# AdaptiveMaxPool2d

```c
REG_OP(AdaptiveMaxPool2d)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT32, DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT32, DT_DOUBLE}))
    .OUTPUT(argmax, TensorType::IndexNumberType())
    .REQUIRED_ATTR(output_size, ListInt)
    .OP_END_FACTORY_REG(AdaptiveMaxPool2d)
```

## Brief

Applies a 2D adaptive max pooling over an input signal conposed of several input planes.
The output is of size H x W, for any input size.

## Inputs

One input, including:
- x: A Tensor. Must be one of the following data types:
    float16, float32, float64. 

## Outputs

- y: A Tensor. Has the same data type as "x".
- argmax: A Tensor. Describing the index of outputs.

## Attributes

- output_size: A required list of 2 ints
   specifying the size (H,W) of the output tensor. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16
- output0 y: float16
- output1 argmax: int32
### AI CPU
- input0 x: double,float16,float32
- output0 y: double,float16,float32
- output1 argmax: int32,int64

## Third-party framework compatibility

Compatible with the Pytorch operator AdaptiveMaxPool2d.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
