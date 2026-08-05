# SyncBatchNormBackwardElemt

```c
REG_OP(SyncBatchNormBackwardElemt)
    .INPUT(grad_output, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(save_input, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(mean, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(invstd, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(weight, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(mean_dy, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .INPUT(mean_dy_xmu, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(grad_input, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OP_END_FACTORY_REG(SyncBatchNormBackwardElemt)
```

## Brief

part of SyncBatchNormBackward .

## Inputs

Seven inputs, including:
- grad_output: A ND tensor(2D-8D). Forward output differential. Must be one of the following types: float16, bfloat16, float32.
- save_input: A ND tensor(2D-8D). The input of forward. Has the same shape, format and type as input "grad_output".
- mean: A ND tensor(2D-8D). Mean of saved forward input. Has the same shape, format and type as input "grad_output".
- invstd: A ND tensor(2D-8D). Reciprocal of the standard deviation of the saved forward input. Has the same shape, format and type as input "grad_output".
- weight: A ND tensor(2D-8D). The weight parameter. Has the same shape, format and type as input "grad_output".
- mean_dy: A ND tensor(2D-8D). A part of sum_dy. Has the same shape, format and type as input "grad_output".
- mean_dy_xmu: A ND tensor(2D-8D). A part of sum_dy_xmu. Has the same shape, format and type as input "grad_output".

## Outputs

grad_input: A ND tensor(2D-8D). The reverse gradient corresponding to the input in the forward calculation. Has the same shape, format and type as input "grad_output". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 grad_output: bfloat16,float16,float32
- input1 save_input: bfloat16,float16,float32
- input2 mean: bfloat16,float16,float32
- input3 invstd: bfloat16,float16,float32
- input4 weight: bfloat16,float16,float32
- input5 mean_dy: bfloat16,float16,float32
- input6 mean_dy_xmu: bfloat16,float16,float32
- output0 grad_input: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
