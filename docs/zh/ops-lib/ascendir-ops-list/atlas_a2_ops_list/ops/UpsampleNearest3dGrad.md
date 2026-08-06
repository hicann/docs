# UpsampleNearest3dGrad

```c
REG_OP(UpsampleNearest3dGrad)
    .INPUT(grad_output, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_UINT8, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_UINT8, DT_BF16}))
    .REQUIRED_ATTR(input_size, ListInt)
    .ATTR(output_size, ListInt, {})
    .ATTR(scales, ListFloat, {})
    .OP_END_FACTORY_REG(UpsampleNearest3dGrad)
```

## Brief

Upsample the 3-D gradient data with the nearest neighbor ​interpolation algorithm. 

## Inputs

One inputs, including: 
grad_output: A 5-D input tensor. The format must be NCDHW. Must be one of the following types:
float16, float32, float64, uint8, bfloat16. 

## Outputs

y: A 5-D tensor. The format must be NCDHW. Must be one of the following types:
float16, float32, float64, uint8, bfloat16.
Has the same type as input grad_output, shape depends on Attributes:input_size. 

## Attributes

- input_size: An required listInt.
Contain 5 elements: [min_batch, channels, depth, height, width]. Must:
input_size[0] == grad_output_tensor_size[0]
input_size[1] == grad_output_tensor_size[1]. 
- output_size: An optional listInt. Defaults to none.
Contain 3 elements: depth, height, width. The number of elements of 'output_size' should
be the same as the rank of input 'grad_output'. Only one of 'scales' and 'output_size' can be specified. Must:
grad_output_tensor_size[2] == floor(input_size[2] * scales[0]) == output_size[0]
grad_output_tensor_size[3] == floor(input_size[3] * scales[1]) == output_size[1]
grad_output_tensor_size[4] == floor(input_size[4] * scales[2]) == output_size[2]. 
- scales: An optional listFloat. Defaults to none.
The scale array along each dimension, contain 3 elements: scale_depth, scale_height, scale_width.
The number of elements of 'scales' should be the same as the rank of input 'grad_output'.
One of 'scales' and 'output_size' must be specified and it is an error if both are specified. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad_output: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 grad_output: double,float16,float32,uint8
- output0 y: double,float16,float32,uint8


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
