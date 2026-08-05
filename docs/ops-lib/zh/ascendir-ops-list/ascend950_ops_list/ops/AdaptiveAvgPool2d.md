# AdaptiveAvgPool2d

```c
REG_OP(AdaptiveAvgPool2d)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(output_size, ListInt)
    .OP_END_FACTORY_REG(AdaptiveAvgPool2d)
```

## Brief

Applies a 2D adaptive average pooling over
an input signal composed of several input planes.

## Inputs

One input, including:
- x: A Tensor. Must be one of the following data types:
    float16, float32, bfloat16. 
For Ascend 950PR/Ascend 950DT: Support Format: [NCHW].

## Outputs

- y: A Tensor. Has the same data type and the same format as "x"

## Attributes

- output_size: A required list of 2 ints
   specifying the size (H,W) of the output tensor. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator AdaptiveAvgPool2d.


---

[Back to Operator Specifications (Ascend950)](../README.md)
