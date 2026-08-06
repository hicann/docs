# AlltoAllAllGatherBatchMatMul

```c
REG_OP(AlltoAllAllGatherBatchMatMul)
    .INPUT(x, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(weight, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(y1, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(y2, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(y3, TensorType({DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(group_ep, String)
    .REQUIRED_ATTR(group_tp, String)
    .REQUIRED_ATTR(ep_world_size, Int)
    .REQUIRED_ATTR(tp_world_size, Int)
    .ATTR(x_shard_type, Int, 0)
    .ATTR(act_type, Int, 0)
    .ATTR(transpose_weight, Bool, false)
    .ATTR(output_y2_flag, Bool, false)
    .ATTR(output_y3_flag, Bool, false)
    .OP_END_FACTORY_REG(AlltoAllAllGatherBatchMatMul)
```

## Brief

Fusion op of alltoall, allgather, and batch matmul.

## Inputs

Three inputs, including (Tp is short for tp_world_size, and ep is short for ep_world_size.):
- x: A matrix Tensor. The type support float16, bfloat16. The format supports ND. The x only supports 3 dimensions.
x_shard_type 0: x (E, C, H/tp), x_shard_type 1: x (E, C/tp, H).
- weight: A matrix Tensor. The type support float16, bfloat16 and its type must be the same as the tpye of x. The format supports ND. The weight only supports 3 dimensions.
weight (E/ep, H, M/tp).
- bias: A matrix Tensor. The type support float16, float32. When x is float16, bias must be float16. When x is bfloat16, bias must be float32. 2D and 3D are supported. The data format can be ND.
bias (E/ep, 1, M/tp), 3 dims; bias (E/ep, M/tp), 2 dims. 

## Outputs

- y1: A batch matmul or activation matrix Tensor. The type support float16, bfloat16. 3D is supported. The data type is the same as that of the input x. The data format can be ND. If there is an activation function, the result is the output of the activation function. Otherwise, the result is the output of BatchMatMul.
x_shard_type 0: y1 (E/ep, ep*C, M/tp), x_shard_type 1: y1 (E/ep, ep*tp*C/tp, M/tp).
- y2: A allgather matrix Tensor. The type support float16, bfloat16. 3D is supported. The data type is the same as that of the input x. The data format can be ND. This parameter indicates AllGather output, which may be required for backpropagation. A null pointer indicates that the output is not required.
x_shard_type 0: y2 (E/ep, ep*C, H), x_shard_type 1: y2 (E/ep, ep*tp*C/tp, H).
- y3: A batch matmul matrix Tensor. The type support float16, bfloat16. 3D is supported. The data type is the same as that of the input x. The data format can be ND. This parameter indicates BatchMatMul output when there is an activation function. A null pointer indicates that the output is not required.
x_shard_type 0: y3 (E/ep, ep*C, M/tp), x_shard_type 1: y3 (E/ep, ep*tp*C/tp, M/tp). 

## Attributes

- group_ep: A required String identifying the expert group of ranks
participating in the op. The string length must be greater than 0 and less than 128.
- group_tp: A required String identifying the tensor group of ranks
participating in the op. The string length must be greater than 0 and less than 128.
- ep_world_size: A required int identifying the number of expert parallel group rank num. The value can be 2, 4, 8, 16 or 32.
- tp_world_size: A required int identifying the number of tensor parallel group rank num. The value can be 2, 4, 8, 16 or 32.
- x_shard_type: An int. Represents the input x shards on dim 2 or 3 in tensor parallel group. Default: "0". The value 0 indicates that AllGather is performed in the H dimension (2nd dimension of x, which has three dimensions: 0th, 1st, and 2nd) based on the tensor parallel group.
The value 1 indicates that AllGather is performed in the C dimension (1st dimension of x) based on the tensor parallel group.
- act_type: An int. Represents the activation function type. Default: "0". 0: None, 1: GELU, 2: Silu, 3: Relu, 4: FastGELU. None indicates no activation function.
- transpose_weight: A bool. If True, changes the shape of "weight" from [E, N, K] to
[E, K, N] before multiplication. Default: "false".
- output_y2_flag: A bool. If True, y2 tensor will output a allgather matrix Tensor
as a result. Default: "false".
- output_y3_flag: A bool. If True, y3 tensor will output a batch matmul matrix Tensor
as a result. Default: "false". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- input1 weight: bfloat16,float16
- input2 bias: bfloat16,float16,float32
- output0 y1: bfloat16,float16
- output1 y2: bfloat16,float16
- output2 y3: bfloat16,float16

## Attention Constraints

- The x[0] means E value, w[0] means E/ep, so the w[0] multi ep should equal the x[0]. Other divisible relationships are similar to this one.
- The value range of E is [2, 512], and E is an integer multiple of ep.
- The value range of H is [1, 65535], and H is an integer multiple of tp when x_shard_type is 0.
- The value range of M/tp is [1, 65535].
- The value range of E/ep is [1, 32].
- C must be greater than 0 and cannot exceed the upper limit of the operator's device memory. C is an integer multiple of tp when x_shard_type is 1.
- Group_ep and group_tp can't be consistent. Ep and tp can only be 2, 4, 8, 16 or 32. Supernodes cannot be crossed.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
