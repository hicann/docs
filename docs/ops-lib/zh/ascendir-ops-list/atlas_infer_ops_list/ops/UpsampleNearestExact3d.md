# UpsampleNearestExact3d

```c
REG_OP(UpsampleNearestExact3d)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .REQUIRED_ATTR(output_size, ListInt)
    .ATTR(scales, ListFloat, { 0.0f, 0.0f, 0.0f })
    .OP_END_FACTORY_REG(UpsampleNearestExact3d)
```

## Brief

Upsample the 3-D data with the nearest neighbor ​interpolation algorithm. 

## Inputs

One inputs, including: 
x: A 5-D input tensor. The format must be NCDHW. Must be one of the following types:
float16, float32, bfloat16. 

## Outputs

y: A 5-D tensor. The format must be NCDHW. Must be one of the following types:
float16, float32, bfloat16.
Has the same type as input x, shape depends on x and output_size/scales. 

## Attributes

- output_size: An required listInt. Defaults to none.
Contain 3 elements: output_depth, output_height, output_width. The number of elements of 'output_size'
should be the same as the rank of input 'x'. Only one of 'scales' and 'output_size' can be specified. 
- scales: An optional listFloat. Defaults to `[0.0, 0.0, 0.0]`.
The scale array along each dimension, contain 3 elements: scale_depth, scale_height, scale_width.
The number of elements of 'scales' should be the same as the rank of input 'x'. One of 'scales' and
'output_size' must be specified and it is an error if both are specified. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
