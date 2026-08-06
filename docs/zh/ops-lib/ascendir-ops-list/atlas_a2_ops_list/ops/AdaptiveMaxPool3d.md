# AdaptiveMaxPool3d

```c
REG_OP(AdaptiveMaxPool3d)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OUTPUT(indices, TensorType({DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(output_size, ListInt)
    .ATTR(indices_dtype, Int, 3)
    .OP_END_FACTORY_REG(AdaptiveMaxPool3d)
```

## Brief

Applies a 3D adaptive max pooling over
an input signal composed of several input planes.

## Inputs

One input, including:
- x: A Tensor. Must be one of the following data types:
    float16, bfloat16, float32. 

## Outputs

- y: A Tensor. Has the same data type as "x"
- indices: A Tensor. Has the same shape as "x"

## Attributes

- output_size: A required list of 0, 1 or 3 ints.
0 specifies the shape of the output tensor is the same as x.
1 specifies the size (D,D,D) of the output tensor.
3 specifies the size (D,H,W) of the output tensor. 
- indices_dtype: An optional int, default value is 3.
(3 is int32, 9 is int64) 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
- output1 indices: int32

## Third-party framework compatibility

Compatible with the Pytorch operator AdaptiveMaxPool3d.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
