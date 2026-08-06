# UpsampleNearest3d

```c
REG_OP(UpsampleNearest3d)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_UINT8, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_UINT8, DT_BF16}))
    .ATTR(output_size, ListInt, {})
    .ATTR(scales, ListFloat, {})
    .OP_END_FACTORY_REG(UpsampleNearest3d)
```

## Brief

Upsample the 3-D data with the nearest neighbor ​interpolation algorithm. 

## Inputs

One inputs, including: 
x: A 5-D input tensor. The format must be NCDHW. Must be one of the following types:
float16, float32, float64, uint8, bfloat16. 

## Outputs

y: A 5-D tensor. The format must be NCDHW. Must be one of the following types:
float16, float32, float64, uint8, bfloat16.
Has the same type as input x, shape depends on x and output_size/scales. 

## Attributes

- output_size: An optional listInt. Defaults to none.
Contain 3 elements: output_depth, output_height, output_width. The number of elements of 'output_size'
should be the same as the rank of input 'x'. Only one of 'scales' and 'output_size' can be specified. 
- scales: An optional listFloat. Defaults to none.
The scale array along each dimension, contain 3 elements: scale_depth, scale_height, scale_width.
The number of elements of 'scales' should be the same as the rank of input 'x'. One of 'scales' and
'output_size' must be specified and it is an error if both are specified. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: double,float16,float32,uint8
- output0 y: double,float16,float32,uint8


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
