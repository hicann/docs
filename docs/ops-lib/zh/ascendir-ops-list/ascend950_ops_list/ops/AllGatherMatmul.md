# AllGatherMatmul

```c
REG_OP(AllGatherMatmul)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(gather_out, TensorType({DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(group, String)
    .ATTR(is_trans_a, Bool, false)
    .ATTR(is_trans_b, Bool, false)
    .ATTR(gather_index, Int, 0)
    .ATTR(comm_turn, Int, 0)
    .ATTR(rank_size, Int, 0)
    .ATTR(is_gather_out, Bool, true)
    .OP_END_FACTORY_REG(AllGatherMatmul)
```

## Brief

Fusion op of allgather and matmul.

## Inputs

three inputs, including:
- x1: A matrix Tensor. The type support float16, bfloat16. The format supports ND. The x1 only supports 2 dimensions in current version, for example (M, K). The x1 doesn't support transposed.
- x2: A matrix Tensor. The type support float16, bfloat16. The format supports ND. The x2 only supports 2 dimensions in current version, for example (K, N). The x2 supports transposed and non-transposed.
The K value in x2 should be same as the K value in x1 when x2 is non-transposed, and the K value should be in range [256, 65535).
- bias: A matrix Tensor. The type support float16, bfloat16. The format supports ND. The current version does not support the scenario where bias is not 0.

## Outputs

- y: A matrix Tensor. The type support float16, bfloat16. The format supports ND. The y is 2 dimensions, for example (M*rank_size, N).
- gather_out: A matrix Tensor. The type support float16, bfloat16. The format supports ND.

## Attributes

- group: A string. A required string identifying the group of ranks participating in the op.
- is_trans_a: A bool. If true, changes the shape of "x1" from [K, M] to [M, K] before multiplication. Default: false.
- is_trans_b: A bool. If true, changes the shape of "x2" from [N, K] to [K, N] before multiplication. Default: false.
- gather_index: An int. Represents the input index for doing gather, 0: left matrix, 1: right matrix. Default: 0. The gather_index only supports 0 in current version.
- comm_turn: An int. Number of communications with AICPU. Default: 0. The comm_turn only supports 0 in current version.
- rank_size: An int. Number of ranks in the group. Default: 0.
The Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component support 2, 4, 8. 
The Atlas A3 Training Series Product/Atlas A3 Inference Series Product support 2, 4, 8, 16. 
- is_gather_out: A bool. If true, output gather_out matrix. Default: true.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16
- input1 x2: bfloat16,float16
- input2 bias: bfloat16,float16
- output0 y: bfloat16,float16
- output1 gather_out: bfloat16,float16


---

[Back to Operator Specifications (Ascend950)](../README.md)
