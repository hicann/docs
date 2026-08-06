# AdaptiveAvgPool

```c
REG_OP(AdaptiveAvgPool)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(output_size, TensorType({DT_INT64, DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OP_END_FACTORY_REG(AdaptiveAvgPool)
```

## Brief

Applies a 1D/2D/3D adaptive average pooling over
an input signal composed of several input planes.

## Inputs

Two input, including:
- x: A Tensor. Must be one of the following data types:
    float16, float32. 
- output_size: A required tensor of shape must be 1 or 2 or 3 ,
 specifying the size  of the output tensor. 

## Outputs

- y: A Tensor. Has the same data type as "x"

## Third-party framework compatibility

Compatible with the Pytorch operator AdaptiveAvgPool.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
