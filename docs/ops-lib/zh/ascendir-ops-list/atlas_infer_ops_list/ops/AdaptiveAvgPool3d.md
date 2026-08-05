# AdaptiveAvgPool3d

```c
REG_OP(AdaptiveAvgPool3d)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(output_size, ListInt)
    .ATTR(data_format, String, "NDHWC")
    .OP_END_FACTORY_REG(AdaptiveAvgPool3d)
```

## Brief

Applies a 3D adaptive average pooling over
an input signal composed of several input planes.

## Inputs

One input, including:
- x: A Tensor. Must be one of the following data types:
    float16, bfloat16, float32. 

## Outputs

- y: A Tensor. Has the same data type as "x"
- data_format: An optional string, Specify the data format of the input and
output data. With the default format "NDHWC" . 

## Attributes

- output_size: A required list of 3 ints
   specifying the size (D,H,W) of the output tensor. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator AdaptiveAvgPool3d.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
