# SoftmaxV2

```c
REG_OP(SoftmaxV2)
    .INPUT(x, TensorType({ DT_DOUBLE, DT_FLOAT16, DT_BF16, DT_FLOAT }))
    .OUTPUT(y, TensorType({ DT_DOUBLE, DT_FLOAT16, DT_BF16, DT_FLOAT }))
    .ATTR(axes, ListInt, {-1})
    .ATTR(half_to_float, Bool, false)
    .OP_END_FACTORY_REG(SoftmaxV2)
```

## Brief

Applies the Softmax function to an n-dimensional input tensor
 rescaling them. so that the elements of the n-dimensional output tensor lie
 in the range [0,1] and sum to 1.

## Inputs

One input:
x: A mutable input tensor, which can be floating point tensors with different precisions. Must be one of the following data types: float16, float32, bfloat16,
double. Should be a variable tensor. The format must be ND. Shape support 1D ~ 8D. 

## Outputs

y: A ND tensor. The output tensor represents the probability distribution of the input tensor after being processed by the Softmax function.
Has the same dimensionality and shape as the "x" with values in the range [0, 1].
Must be one of the following types: float16, float32, bfloat16, double. 

## Attributes

- axes: An optional list of int. Specifies on which dimensions of input x the Softmax operation is performed.
Multi-axis reduction is supported. Defaults to "{-1}".
In Ascend 950 AI Processor, only single-axis reduction is supported. 
- half_to_float: An optional bool.
This parameter determines whether to convert the output data type to float32 when the input data type is float16.
Defaults to "false".
- If true and the input data type is float16, the output data type should be float32.
- Otherwise, the output data type should be the same as the input data type. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32
### AI CPU
- input0 x: double,float16,float32
- output0 y: double,float16,float32

## Third-party framework compatibility

 Compatible with the TensorFlow operator Softmax.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
