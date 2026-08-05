# MoeFinalizeRouting

```c
REG_OP(MoeFinalizeRouting)
    .INPUT(expanded_x, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(x1, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(x2, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(bias, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(scales, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(expanded_row_idx, TensorType({DT_INT32}))
    .INPUT(expanded_expert_idx, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .OP_END_FACTORY_REG(MoeFinalizeRouting)
```

## Brief

In MoE computation, the final step involves processing and merging the output results of the MoE FNN.

## Inputs

- expanded_x: A 2D Tensor. Type is:BFloat16, Float16 or Float32. Shape support(NUM\_ROWS \* K, H).
- x1: A 2D Tensor. Type is:BFloat16, Float16 or Float32. The data type requirement of A is consistent
with expandedX,and the shape requirements are consistent with the shape of out.
- x2: An optional 2D Tensor. Type is:BFloat16, Float16 or Float32. The data type requirement of A is consistent
with expandedX,and the shape requirements are consistent with the shape of out. If the parameter A is not entered,
the parameter B can also not be entered.
- bias: A 2D Tensor. Type is:BFloat16, Float16 or Float32.The data type requirement of A is consistent
with expandedX.Shape support(E, H). E is the total number of experts, and H is the number of columns.
- scales: A 2D Tensor. Type is:BFloat16, Float16 or Float32. The data type requirement of A is consistent
with expandedX.Shape support(NUM\_ROWS, K).
- expanded_row_idx: A 1D Tensor. Type is:Int32.Shape support(NUM\_ROWS \* K).Values in Tensor are
[0,NUM\_ROWS \* K-1].
- expanded_expert_idx: A 2D Tensor. Type is Int32. Shape support(NUM\_ROWS, K).
Values in Tensor are [0, E-1].

## Outputs

- y: A 2D Tensor. Type is:BFloat16, Float16 or Float32. Shape support(NUM\_ROWS, H).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 expanded_x: bfloat16,float16,float32
- input1 x1: bfloat16,float16,float32
- input2 x2: bfloat16,float16,float32
- input3 bias: bfloat16,float16,float32
- input4 scales: bfloat16,float16,float32
- input5 expanded_row_idx: int32
- input6 expanded_expert_idx: int32
- output0 y: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
