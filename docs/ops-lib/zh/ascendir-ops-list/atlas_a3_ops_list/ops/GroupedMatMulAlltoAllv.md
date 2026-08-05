# GroupedMatMulAlltoAllv

```c
REG_OP(GroupedMatMulAlltoAllv)
      .INPUT(gmm_x, TensorType({DT_FLOAT16, DT_BF16}))
      .INPUT(gmm_weight, TensorType({DT_FLOAT16, DT_BF16}))
      .OPTIONAL_INPUT(send_counts_tensor, TensorType({DT_INT32, DT_INT64}))
      .OPTIONAL_INPUT(recv_counts_tensor, TensorType({DT_INT32, DT_INT64}))
      .OPTIONAL_INPUT(mm_x, TensorType({DT_FLOAT16, DT_BF16}))
      .OPTIONAL_INPUT(mm_weight, TensorType({DT_FLOAT16, DT_BF16}))
      .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16}))
      .OUTPUT(mm_y, TensorType({DT_FLOAT16, DT_BF16}))
      .REQUIRED_ATTR(group, String)
      .REQUIRED_ATTR(ep_world_size, Int)
      .REQUIRED_ATTR(send_counts, ListInt)
      .REQUIRED_ATTR(recv_counts, ListInt)
      .ATTR(trans_gmm_weight, Bool, false)
      .ATTR(trans_mm_weight, Bool, false)
      .ATTR(comm_mode, String, "")
      .OP_END_FACTORY_REG(GroupedMatMulAlltoAllv)
```

## Brief

Fusion of grouped matmul and alltoallv.

## Inputs

- gmm_x: A matrix tensor of shape [A, H1]. The data type of elements supports float16 or bfloat16; the format supports ND.
- gmm_weight: A matrix tensor of shape [e, H1, N1]. The data type of elements supports float16 or bfloat16 and should match that of gmm_x; the format supports ND.
- send_counts_tensor: A tensor of shape [e * ep]. The data type of elements supports int32 or int64; the format supports ND.
- recv_counts_tensor: A tensor of shape [e * ep]. The data type of elements supports int32 or int64; the format supports ND.
Data type of elements is int64. Format: ND.
- mm_x: A matrix tensor of shape [BS, H2]. The data type of elements supports float16 or bfloat16; the format supports ND.
- mm_weight: gmm_weight: A matrix tensor of shape [H2, N2]. The data type of elements supports float16 or bfloat16 and should match that of mm_x; the format supports ND.

## Outputs

- y: A matrix tensor of shape [BSK, N1] containing result of grouped matmul. The data type of elements supports float16 or bfloat16; the format supports ND.
- mm_y_optional: A matrix tensor of shape [BS, N2] containing result of matmul. The data type of elements supports float16 or bfloat16; the format supports ND.

## Attributes

- group: A required String identifying the expert group of ranks
- ep_world_size: A required int identifying the number of expert parallel group rank num.
- send_counts: An int list. A list containing amount of data to be sent.
- recv_counts: An int list. A list containing amount of data to be received.
- trans_gmm_weight: A boolean value. Indicating whether gmm_weight is transposed.
- trans_mm_weight: A boolean value. Indicating whether mm_weight is transposed.
- comm_mode:A string value. Indicating communication mode.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 gmm_x: bfloat16,float16
- input1 gmm_weight: bfloat16,float16
- input2 send_counts_tensor: int32,int64
- input3 recv_counts_tensor: int32,int64
- input4 mm_x: bfloat16,float16
- input5 mm_weight: bfloat16,float16
- output0 y: bfloat16,float16
- output1 mm_y: bfloat16,float16


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
