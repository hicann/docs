# GroupedMatmulFinalizeRouting

```c
REG_OP(GroupedMatmulFinalizeRouting)
.INPUT(x, TensorType({DT_INT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3, DT_FLOAT4_E2M1, DT_HIFLOAT8}))
.INPUT(w, TensorType({DT_INT8, DT_INT4, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3, DT_FLOAT4_E2M1, DT_HIFLOAT8}))
.OPTIONAL_INPUT(scale, TensorType({DT_FLOAT, DT_INT64, DT_BF16, DT_FLOAT8_E8M0}))
.OPTIONAL_INPUT(bias, TensorType({DT_FLOAT, DT_BF16}))
.OPTIONAL_INPUT(pertoken_scale, TensorType({DT_FLOAT, DT_FLOAT8_E8M0}))
.OPTIONAL_INPUT(group_list, TensorType({DT_INT64}))
.OPTIONAL_INPUT(shared_input, TensorType({DT_BF16}))
.OPTIONAL_INPUT(logit, TensorType({DT_FLOAT}))
.OPTIONAL_INPUT(row_index, TensorType({DT_INT64, DT_INT32}))
.OPTIONAL_INPUT(offset, TensorType({DT_FLOAT}))
.OUTPUT(y, TensorType({DT_FLOAT}))
.ATTR(dtype, Int, 0)
.ATTR(shared_input_weight, Float, 1.0)
.ATTR(shared_input_offset, Int, 0)
.ATTR(transpose_x, Bool, false)
.ATTR(transpose_w, Bool, false)
.ATTR(output_bs, Int, 0)
.ATTR(group_list_type, Int, 1)
.ATTR(tuning_config, ListInt, {0})
.OP_END_FACTORY_REG(GroupedMatmulFinalizeRouting)
```

## Brief

Function GroupedMatmulFinalizeRouting. This op mixs GroupedMatmul和MoeFinalizeRouting. After the calculation of GroupedMatmul, perform a combine operation on the output according to the index, and support the format where w is in the Ascend affinity data layout.

## Inputs

- x: A tensor, which is the input x in the formula, supports the ND data format (refer to Data Format), and the shape supports 2 dimensions with the dimension being (m, k). The data type supports INT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT4_E2M1, DT_HIFLOAT8.
- w: A tensor of weight, which supports the Ascend affinity data layout format as described in Data Format. The data type supports INT8, INT4, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT4_E2M1, and the shape supports 3 or 5 dimensions. On Ascend950PR/Ascend950DT, five-dimensional shapes are supported only when the data type is INT8, DT_FLOAT8_E4M3FN or DT_HIFLOAT8.
When transposew is false, each dimension is represented as: (e, n1, k1, k0, n0), where k0 = 16, n0 = 32. The k in the x shape and the k1 in the w shape need to satisfy the following relationship: ceilDiv(k, 16) = k1.
The aclnnCalculateMatmulWeightSizeV2 interface and the aclnnTransMatmulWeight interface can be used to complete the conversion of the input format from the ND format to the Ascend affinity data layout format.
- scale: It represents the scaling factor in the quantization parameters. It supports the ND data format as described in Data Format. The supported data type is FLOAT32, INT64, BFLOAT16, DT_FLOAT8_E8M0.
and if w is INT4, the shape is three-dimensional (e, 1, n), others scenarios is two-dimensional (e, n), where the values of e and n are consistent with those of e and n in w.  The supported data type is BFLOAT16.
- bias: A tensor of bias, contains all bias of inputs for matmul. For each tensor, the data type of elements supports float32; the format supports ND..
- offset: A tensor of offset, only supported when w is INT4, the shape is three-dimensional (e, 1, n), the format supports ND. The supported data types is FLOAT32.
- pertoken_scale: The dequantization parameters for matrix calculation support the ND data format (refer to Data Format). They correspond to the x matrix, with a dimension of (m). The supported data type is FLOAT32, DT_FLOAT8_E8M0. Non-contiguous tensors are not supported.
- group_list: a tensor, indicates M-axis distributation of groups of matmuls for inputs and outputs.
Data type of elements is int64. Format: ND. The first dimension of group_list should not be greater than 1024, meaning it supports up to 1024 groups.
- shared_input: In the MoE (Mixture of Experts) calculation, the output of the shared experts needs to undergo a combine operation with the output of the MoE experts. The supported data types are bfloat16.
- logit: In the MoE (Mixture of Experts), for the logit magnitudes of each token, the output of the matrix multiplication is multiplied by these logits, and then combined according to the indices. The supported data type is float32.
- row_index: The outputs of the MoE (Mixture of Experts) are combined according to the rowIndex, where the values in rowIndex serve as the indices for the scatter add operation during the combination. The supported data types are int64 and int32.

## Outputs

y: A tensor List, contains all result of groups of matmuls. For each tensor,
the data type of elements supports float32; the format supports ND. 

## Attributes

- dtype: The type of GroupedMatmul. The type is int, which output:0：FLOAT32；1：FLOAT16；2：BFLOAT16.
- shared_input_weight: The coefficients for combining the shared experts and the MoE experts. The shareInput is multiplied first with these coefficients, and then the result is accumulated with the output of the MoE experts. The supported data type is float32.
- shared_input_offset: The offset of the output of the shared experts in the total output. The supported data type is int64.
- transpose_x: Whether the left matrix is transposed. Default value: false(not transposed).
- transpose_w: Whether the right matrix is transposed. Default value: false(not transposed).
- output_bs: The size of the highest dimension of the output.
- group_list_type: Group type of GroupedMatmul. Default value: 1. When configured as 0: It is in the cumsum mode, which means it is the prefix sum. When configured as 1: It is in the count mode. The supported data type is int64.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: int8
- input1 w: int4,int8
- input2 scale: bfloat16,float32,int64
- input3 bias: bfloat16,float32
- input4 pertoken_scale: float32
- input5 group_list: int64
- input6 shared_input: bfloat16
- input7 logit: float32
- input8 row_index: int32,int64
- input9 offset: float32
- output0 y: float32

## Attention Constraints

Support combinations of data type: 
 | x             | w             |  scale           | bias     | offset  | pertokenScale | groupList | sharedInput | logit   | rowIndex    |  out    | 
 | ----          | ----          | -------          | -------  | ------- | ------------- | --------- | ----------- | ------- | --------    | ------- | 
 | INT8          | INT4          | INT64            | FLOAT32  | FLOAT32 | FLOAT32       | INT64     | BFLOAT16    | FLOAT32 | INT64       | FLOAT32 | 
 | INT8          | INT4          | INT64            | FLOAT32  | null    | FLOAT32       | INT64     | BFLOAT16    | FLOAT32 | INT64       | FLOAT32 | 
 | INT8          | INT8          | FLOAT32          | null     | null    | FLOAT32       | INT64     | BFLOAT16    | FLOAT32 | INT64       | FLOAT32 | 
 | INT8          | INT8          | FLOAT32          | null     | null    | FLOAT32       | INT64     | null        | null    | INT64       | FLOAT32 | 
 | INT8          | INT8          | FLOAT32          | BFLOAT16 | null    | FLOAT32       | INT64     | null        | null    | INT64       | FLOAT32 | 
 | INT8          | INT8          | BFLOAT16         | BFLOAT16 | null    | FLOAT32       | INT64     | null        | null    | INT64       | FLOAT32 | 
 | INT8          | INT8          | FLOAT32/BFLOAT16 | BFLOAT16 | null    | FLOAT32/null  | INT64     | BFLOAT16    | FLOAT32 | INT64/INT32 | FLOAT32 | 
 | FLOAT8_E4M3FN | FLOAT8_E4M3FN | FLOAT32/BFLOAT16 | BFLOAT16 | null    | FLOAT32/null  | INT64     | BFLOAT16    | FLOAT32 | INT64       | FLOAT32 | 
 | HIFLOAT8      | HIFLOAT8      | FLOAT32/BFLOAT16 | BFLOAT16 | null    | FLOAT32/null  | INT64     | BFLOAT16    | FLOAT32 | INT64       | FLOAT32 | 
Among them: 
The dimension m = batch * topk, and the value range is [1, 16 * 1024 * 8]. The functionality is not guaranteed if it exceeds this range. 
k supports the value include of 256、512、1024、1408、2048. The functionality is not guaranteed if it exceeds this range. 
n supports the value include of 2048、7168、7680. The functionality is not guaranteed if it exceeds this range. 
The value range of e is [1, 256]. The functionality is not guaranteed if it exceeds this range. 
The value range of bs/p is [1, 2 * 1024], and p = [8, 16, 32, 48, 64, 96, 128, 144, 288]. 
The value range of bs is [1, 16 * 1024]. The functionality is not guaranteed if it exceeds this range. 
The sum of the values in grouplist is less than or equal to m. 
When group_list_type is 0, group_list must be a non-negative monotone non-decreasing array; when group_list_type is 1, it must be a non-negative array. 

## Attention MX Quantization Constraints

 |             x             |            w              |     scale     |      bias    | offset  | pertokenScale | groupList |  sharedInput  | logit   | rowIndex |  out    | 
 | ------------------------- | ------------------------- | ------------- | ------------ | ------- | ------------- | --------- | ------------- | ------- | -------- | ------- | 
 | FLOAT8_E4M3FN/FLOAT8_E5M2 | FLOAT8_E4M3FN/FLOAT8_E5M2 | FLOAT8_E8M0   | FLOAT32/NULL | NULL    | FLOAT8_E8M0   | INT64     | BFLOAT16/NULL | FLOAT32 | INT64    | FLOAT32 | 
 | FLOAT4_E2M1               | FLOAT4_E2M1               | FLOAT8_E8M0   | FLOAT32/NULL | NULL    | FLOAT8_E8M0   | INT64     | BFLOAT16/NULL | FLOAT32 | INT64    | FLOAT32 | 
PertokenScale dimension is represented as: (m, ceil(k/64), 2). The data type supports FLOAT8_E8M0, and the shape supports 3 dimensions.
Scale dimension is represented as: (e, ceil(k/64), n, 2) or (e, n, ceil(k/64), 2). The data type supports FLOAT8_E8M0, and the shape supports 4 dimensions.
In the MXFP4 scenario, the constraint that k must be even. Under non-transposed x2, n must also be even.
In MXFP4/MXFP8 scenarios, weight(w) transposition is supported. The transposition property of w must be consistent with that of scale.
e must be less than or equal to 1024.
In the MXFP4 scenario, k cannot be equal to 2.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
