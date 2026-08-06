# AdaptiveAvgPool2dAssistMatrix

```c
REG_OP(AdaptiveAvgPool2dAssistMatrix)
    .INPUT(input_size, TensorType({DT_INT64}))
    .OUTPUT(left_matrix, TensorType({DT_FLOAT}))
    .OUTPUT(right_matrix, TensorType({DT_FLOAT}))
    .OUTPUT(weight_matrix, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(output_size, ListInt)
    .OP_END_FACTORY_REG(AdaptiveAvgPool2dAssistMatrix)
```

## Brief

The operator generates three assist matrixs which will be used in AdaptiveAvgPool2d. 

## Outputs

three inputs, including:
- left_matrix: A Tensor of type float32.
- right_matrix: A Tensor of type float32.
- weight_matrix: A Tensor of type float32.

## Attributes

output_size: A required attribute.  

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_size: int64
- output0 left_matrix: float32
- output1 right_matrix: float32
- output2 weight_matrix: float32

## Input

input_size: A Tensor of type int64.  


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
