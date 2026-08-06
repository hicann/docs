# MatmulReduceScatterV2

```c
REG_OP(MatmulReduceScatterV2)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2, DT_HIFLOAT8}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT8_E4M3FN, DT_FLOAT8_E5M2, DT_HIFLOAT8}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(x1_scale, TensorType({DT_FLOAT, DT_FLOAT_E8M0}))
    .OPTIONAL_INPUT(x2_scale, TensorType({DT_FLOAT, DT_FLOAT_E8M0}))
    .OPTIONAL_INPUT(quant_scale, TensorType({DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(amax_out, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(group, String)
    .ATTR(reduce_op, String, "sum")
    .ATTR(is_trans_a, Bool, false)
    .ATTR(is_trans_b, Bool, false)
    .ATTR(comm_turn, Int, 0)
    .ATTR(rank_size, Int, 0)
    .ATTR(block_size, Int, 0)
    .ATTR(group_size, Int, 0)
    .ATTR(is_amax_out, Bool, false)
    .ATTR(y_dtype, Int, 0)
    .ATTR(comm_mode, String, "aicpu")
    .OP_END_FACTORY_REG(MatmulReduceScatterV2)
```

## Brief

Fusion op of matmul and reduce scatter v2.

## Inputs

six inputs, including:
- x1: A matrix tensor. The type supports float16, bfloat16, hifloat8, float8_e5m2, float8_e4m3fn.The format supports ND. The x1 only supports two dimensions in current version, for example (M, K). The x1 doesn't support transposed.
- x2: A matrix tensor. The type supports float16, bfloat16, hifloat8, float8_e5m2, float8_e4m3fn.The x2 only supports two dimensions in current version, for example (K, N). The x2 supports transposed and non-transposed.
The K value in x2 should be same as the K value in x1 when x2 is non-transposed, and the K value should be in range [256, 65535).
- bias: A matrix tensor. The format supports ND. If x1 type is float8_e4m3fn, float8_e5m2, hifloat8, then the bias type supports float32.
If x1 type is float16, bfloat16, then the bias type supports float16, bfloat16 and the current version doesn't supports the scenario where bias is not 0. 
The bias only supports one dimension in current version, for expample (N,). 
The bias only supports nullptr in the per_block scenario. 
- x1_scale: A matrix tensor. The type supports float32, float_e8m0. The format supports ND.  The x1_scale only supports nullptr when x1's type is float16 or bfloat16.
The x1_scale only supports one dimension and only one element in the per_tensor scenario, for expample (1,). 
The x1_scale only supports two dimensions in the per_block scenario, for expample (ceildiv(M, 128), ceildiv(K, 128)). 
- x2_scale: A matrix tensor. The type supports float32, float_e8m0. The format supports ND.  The x2_scale only supports nullptr when x1's type is float16 or bfloat16.
The x2_scale only supports one dimension and only one element in the per_tensor scenario, for expample (1,). 
The x2_scale only supports two dimensions in the per_block scenario, for expample (ceildiv(K, 128), ceildiv(N, 128)). 
- quant_scale: A matrix tensor. The type supports float32. The format supports ND. The quant_scale only supports one dimension and only one element, for example (1,). The quant_scale only supports nullptr in current version.

## Outputs

- y: A matrix tensor. If x1 type is float16, bfloat16, The type is same as x1.
If x1 type is float8_e4m3fn, float8_e5m2, hifloat8, the output type supports float16, bfloat16, float32. The format supports ND. The y is two dimensions, for example (M/rank_size, N).
- amax_out: A matrix tensor. The type supports float32. The format supports ND. The amax_out is 1 dimension and only one element, for example (1,). The amax_out only supports nullptr in current version.

## Attributes

- group: A required String identifying the group of ranks
participating in the op.
- reduce_op: A required string identifying the reduction operation to perform. Default: "sum". The reduce_op only supports sum in current version.
- is_trans_a: A bool. If True, changes the shape of "x1" from [K, M] to [M, K] before multiplication.
If False, don't change the shape of "x1" before multiplication. Default: "false". The is_trans_a only supports false in current version.
- is_trans_b: A bool. If True, changes the shape of "x2" from [N, K] to [K, N] before multiplication.
If False, don't change the shape of "x2" before multiplication. Default: "false".
- comm_turn: An int. Number of communications with CCU. Default: "0". The comm_turn only supports 0 in current version.
- rank_size: An int. Number of rank num. Default: "0".The rank_size only supports 2/4/8/16/32/64 in current version.
- block_size: An int. Number of values in the M, N directions in y correspond to one dequantization coefficient. Default: "0". The block_size only supports 0 in current version.
- group_size: An int. Number of values in the M, N, K directions in x1/x2 correspond to one dequantization coefficient.
Default: "0". Reserved attribute. The block_size only supports 549764202624 in the per_block scenario. The block_size only supports 0 in the other scenario. 
- is_amax_out: A bool. whether the output of amax_out is supported . Default: "false". If True, supports output amax_out.
- y_dtype: An int. Default: "0". The y_dtype only supports 0(float32)/1(float16)/27(bfloat16) in current version.
- comm_mode: A string. communication Mode. Default: "". The comm_mode only supports "aicpu" or "aiv" in current version.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,int8
- input1 x2: bfloat16,float16,int8
- input2 bias: bfloat16,float16,float32
- input3 x1_scale: float32
- input4 x2_scale: float32,int64
- input5 quant_scale: float32
- output0 y: bfloat16,float16
- output1 amax_out: float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
