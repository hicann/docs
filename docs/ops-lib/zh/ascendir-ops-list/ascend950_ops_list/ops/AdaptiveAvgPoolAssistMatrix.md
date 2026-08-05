# AdaptiveAvgPoolAssistMatrix

```c
REG_OP(AdaptiveAvgPoolAssistMatrix)
    .INPUT(input_size, TensorType({DT_INT64, DT_INT32}))
    .INPUT(output_size, TensorType({DT_INT64, DT_INT32}))
    .OUTPUT(left_matrix, TensorType({DT_FLOAT}))
    .OUTPUT(right_matrix, TensorType({DT_FLOAT}))
    .OUTPUT(weight_matrix, TensorType({DT_FLOAT}))
    .OP_END_FACTORY_REG(AdaptiveAvgPoolAssistMatrix)
```

## Brief

The operator generates three assist matrixs which will be used in AdaptiveAvgPool. 

## Outputs

three inputs, including:
- left_matrix: A Tensor of type float32.
- right_matrix: A Tensor of type float32.
- weight_matrix: A Tensor of type float32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input_size: int32,int64
- input1 output_size: int32,int64
- output0 left_matrix: float32
- output1 right_matrix: float32
- output2 weight_matrix: float32

## Input

input_size: A Tensor of type int64.  
output_size: A Tensor of type int64.  


---

[Back to Operator Specifications (Ascend950)](../README.md)
