# MatmulAllReduceAddRmsNorm

```c
REG_OP(MatmulAllReduceAddRmsNorm)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_BF16, DT_INT8}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_BF16, DT_INT8, DT_INT4}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT16, DT_BF16, DT_INT32}))
    .INPUT(residual, TensorType({DT_FLOAT16, DT_BF16}))
    .INPUT(gamma, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(antiquant_scale, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(antiquant_offset, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(dequant_scale, TensorType({DT_FLOAT16, DT_BF16, DT_UINT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16}))
    .OUTPUT(norm_out, TensorType({DT_FLOAT16, DT_BF16}))
    .REQUIRED_ATTR(group, String)
    .ATTR(reduce_op, String, "sum")
    .ATTR(is_trans_a, Bool, false)
    .ATTR(is_trans_b, Bool, false)
    .ATTR(comm_turn, Int, 0)
    .ATTR(antiquant_group_size, Int, 0)
    .ATTR(epsilon, Float, 1e-06f)
    .OP_END_FACTORY_REG(MatmulAllReduceAddRmsNorm)
```

## Brief

Function MatmulAllReduceAddRmsNorm.

## Inputs

- x1: A matrix Tensor. The type support float16, bf16, int8.
- x2: A matrix Tensor. The type support float16, bf16, int8, int4.
- bias: A matrix Tensor. The type support float16, bf16, int32.
- residual: A matrix Tensor. The type support float16, bf16.
- gamma: A matrix Tensor. The type support float16, bf16.
- antiquant_scale: A matrix Tensor. The type support float16, bf16.
- antiquant_offset: A matrix Tensor. The type support float16, bf16.
- dequant_scale: A matrix Tensor. The type support float16, bf16, uint64.

## Outputs

- y: A matrix Tensor. The type support float16, bf16.
- norm_out: A matrix Tensor. The type support float16, bf16.

## Attributes

- group: A required String identifying the group of ranks participating in the op.
- reduce_op: A required string identifying the reduction operation to perform. support "sum", "min", "max" ,"prod", *  currently only support "sum".
- is_trans_a: A bool. If True, changes the shape of "x1" from [K, M] to
 [M, K] before multiplication. Default: false.
- is_trans_b: A bool. If True, changes the shape of "x2" from [N, K] to
 [K, N] before multiplication. Default: false.
- comm_turn: An int. Number of communications with AICPU. Default: 0.
- antiquant_group_size: An int. Number of per-group for quant. Default: 0.
- epsilon: A float32. Default: 1e-06.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,int8
- input1 x2: bfloat16,float16,int4,int8
- input2 bias: bfloat16,float16,int32
- input3 residual: bfloat16,float16
- input4 gamma: bfloat16,float16
- input5 antiquant_scale: bfloat16,float16
- input6 antiquant_offset: bfloat16,float16
- input7 dequant_scale: bfloat16,float16,int64,uint64
- output0 y: bfloat16,float16
- output1 norm_out: bfloat16,float16

## Attention Constraints

- Constraints for MatmulAllReduceAddRmsNorm
- The application scenario is the same as that [MatmulAllReduce]. MatmulAllReduceAddRmsNorm is disabled in
 incremental scenarios but enabled in full scenarios.
- x1 can be 2-dimensional or 3-dimensional, and the dimension is (b, s, k) or (s, k). x2 must be
 2-dimensional and its dimension is (k, n). The axis meets the input parameter requirements of the mm operator, and
 their k axes are equal. If bias is not empty, it is one-dimensional and its dimension is (n).
- The input residual must be 3-dimensional and its dimension are (b, s, n). When x1 is two-dimensional,
 (b*s) of residual is equal to s of x1. The input gamma must be one-dimensional
 and its dimension is (n).
- The dimensions and data types of the outputs y and normOut are the same as those of residual.
 If bias is not empty, the shape size is the same as the last dimension.
- The data types of x1, x2, bias (if supported), residual, gamma, y,
 and normOut computation input must be the same.
- The x2 matrix can be transposed or not transposed. The x1 matrix cannot be transposed.
- The value of epsilon must be within the value range (0,1).
- The Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component support 1, 2, 4, and 8 cards.
- Constraints for WeightQuantMatmulAllReduceAddRmsNorm
- The application scenario is the same as that of [MatmulAllReduce].
 WeightQuantMatmulAllReduceAddRmsNorm is disabled in incremental scenarios but enabled in full scenarios.
- x1 can be 2-dimensional or 3-dimensional, and the dimension is (b, s, k) or (s, k). x2 must be
 2-dimensional and its dimension is (k, n). The axis meets the input parameter requirements of the mm operator.
 Their k axes are equal. The range of k and n is [1, 65535]. If bias is not empty,
 bias has one dimension and its dimension is (n).
- The input residual must have three dimensions: (b, s, n). When x1 is two-dimensional,
 (b*s) of residual is equal to s of x1. gamma must be one-dimensional and its dimension is (n).
- The shape of antiquantScale is [1] in the per-tensor scenario; [1,n]\[n] in the per-channel scenario;
 and [ceil(k,antiquantGroupSize),n] in the per-group scenario. If antiquant_offset is not empty,
 the shape is the same as that of antiquantScale.
- The dimensions and data types of the outputs y and normOut are the same as those of residual.
 If bias is not empty, the shape size is the same as the last dimension.
- The data type of x2 must be int8 or int4. The data types of x1, bias (if supported), residual,
 gamma, y, or normOut must be the same.
- The x2 matrix can be transposed or not transposed. The x1 matrix cannot be transposed.
- The value of antiquantGroupSize falls in the range of [32, min(k-1, INT_MAX)] and must be a multiple of 32.
- The value of epsilon must be within the value range (0,1).
- The Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component support 1, 2, 4, and 8 cards.
- Constraints for QuantMatmulAllReduceAddRmsNorm
- The application scenario is the same as that of [MatmulAllReduce].
 QuantMatmulAllReduceAddRmsNorm is disabled in incremental scenarios but enabled in full scenarios.
- The input x1 can be 2-dimensional or 3-dimensional, and the dimension is (b, s, k) or (s, k). x2 must
 be 2-dimensional and its dimension is (k, n). The axis meets the input parameter requirements of the mm operator,
 and their k axes are equal. If bias is not empty, bias has one dimension and its dimension is (n).
- The input residual must have three dimensions: (b, s, n). When x1 is two-dimensional, (b*s) of
 residual is equal to s of x1. The input gamma must be one-dimensional and its dimension is (n).
- The dimensions and data types of the outputs y and normOut are the same as those of residual. If
 bias is not empty, the shape size is the same as the last dimension.
- If the output residual is of FLOAT16 type, the type of dequantScale is UINT64. If the output residual
 is of BFLOAT16 type, the type of dequantScale is BFLOAT16.
- When the data types of x1 and x2 are INT8, and the data type of bias (if supported) is INT32, the
 input data types of residual, gamma, y, and normOut must be the same.
- The x2 matrix can be transposed or not transposed. The x1 matrix cannot be transposed.
- The value of epsilon must be within the value range (0, 1).
- The Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component support 1, 2, 4, and 8 cards.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
