# SyncBatchNormBackwardReduce

```c
REG_OP(SyncBatchNormBackwardReduce)
    .INPUT(sum_dy, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(sum_dy_dx_pad, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(mean, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(invert_std, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(sum_dy_xmu, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(SyncBatchNormBackwardReduce)
```

## Brief

part of SyncBatchNormBackward .

## Inputs

Four inputs, including:
- sum_dy: A ND tensor. Represents the sum of the gradients of the loss function output to the batch normalization layer.
Must be one of the following types: float16, float32, bfloat16.
- sum_dy_dx_pad: A ND tensor. Represents the sum of the gradients of the input of the loss function to the batch normalization layer.
Must be one of the following types: float16, float32, bfloat16. Has the same type, shape and format as "sum_dy".
- mean: A ND tensor. The mean value of the input data calculated during forward propagation.
Must be one of the following types: float16, float32, bfloat16. Has the same type, shape and format as "sum_dy".
- invert_std: A ND tensor. The reciprocal of the input data standard deviation calculated during forward propagation.
Must be one of the following types: float16, float32, bfloat16. Has the same type, shape and format as "sum_dy". 

## Outputs

- sum_dy_xmu: A ND tensor. Represents the sum of the gradients of the loss function against the mean.
Has the same type, shape and format as "sum_dy".
- y: A ND tensor. Indicates the adjusted gradient, which is used for backpropagation to the previous layer.
Has the same type, shape and format as "sum_dy". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 sum_dy: float16,float32
- input1 sum_dy_dx_pad: float16,float32
- input2 mean: float16,float32
- input3 invert_std: float16,float32
- output0 sum_dy_xmu: float16,float32
- output1 y: float16,float32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
