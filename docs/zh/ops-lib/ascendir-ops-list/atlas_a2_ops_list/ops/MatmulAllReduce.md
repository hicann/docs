# MatmulAllReduce

```c
REG_OP(MatmulAllReduce)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_BF16, DT_INT8, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT4_E2M1}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_BF16, DT_INT8, DT_INT4, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT4_E2M1}))
    .OPTIONAL_INPUT(bias, TensorType({DT_FLOAT16, DT_BF16, DT_INT32, DT_FLOAT}))
    .OPTIONAL_INPUT(x3, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(antiquant_scale, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(antiquant_offset, TensorType({DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(dequant_scale, TensorType({DT_FLOAT16, DT_BF16, DT_UINT64, DT_INT64, DT_FLOAT, DT_FLOAT8_E8M0}))
    .OPTIONAL_INPUT(pertoken_scale, TensorType({DT_FLOAT, DT_FLOAT8_E8M0, DT_FLOAT16, DT_BF16}))
    .OPTIONAL_INPUT(comm_quant_scale_1, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OPTIONAL_INPUT(comm_quant_scale_2, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .REQUIRED_ATTR(group, String)
    .ATTR(reduce_op, String, "sum")
    .ATTR(is_trans_a, Bool, false)
    .ATTR(is_trans_b, Bool, false)
    .ATTR(comm_turn, Int, 0)
    .ATTR(antiquant_group_size, Int, 0)
    .ATTR(group_size, Int, 0)
    .ATTR(y_dtype, Int, DT_UNDEFINED)
    .ATTR(comm_quant_mode, Int, 0)
    .ATTR(comm_mode, String, "ai_cpu")
    .OP_END_FACTORY_REG(MatmulAllReduce)
```

## Brief

Function MatmulAllReduce.

## Inputs

- x1: A matrix tensor, left matrix of mm. The type support float16, bf16, int8, hifloat8,
float8_e5m2, float8_e4m3, float4_e2m1, float4_e1m2.
- x2: A matrix tensor, right matrix of mm. The type support float16, bf16, int8, int4, hifloat8, float8_e5m2,
float8_e4m3, float4_e2m1, float4_e1m2.
- bias: A matrix tensor, input biasOptional in the formula. The type support float16, bf16, int32, float32.
- x3: A matrix tensor, input x3Optional in the formula. The type support float16, bf16, float32.
- antiquant_scale: A matrix tensor. The type support float16, bf16, float32.
- antiquant_offset: A matrix tensor. The type support float16, bf16.
- dequant_scale: A matrix tensor. This parameter indicates the dequantization coefficient after the mm operation.
The shape is (1) in the per-tensor scenario and (n)/(1, n) in the per-channel scenario.
The type support float16, bf16, uint64, int64, float32, float8_e8m0.
- pertoken_scale: A matrix tensor, the per-token dequantization coefficient after the MM computation.
The type support float32, float8_e8m0, float16, bf16.
- comm_quant_scale_1: A matrix tensor. The per-channel quantization coefficient after the matmulAdd computation.
The type support float16, bf16, float32.
- comm_quant_scale_2: A matrix tensor. The per-channel quantization coefficient after the allGather computation.
The type support float16, bf16, float32. 

## Outputs

y: A matrix tensor. The type support float16, bf16. 

## Attributes

- group: A required String identifying the group of ranks
 participating in the op.
- reduce_op: A required string identifying the reduction operation to
 perform. support "sum", "min", "max", "prod", currently only support "sum".
- is_trans_a: A bool. If True, changes the shape of "x1" from [K, M] to
 [M, K] before multiplication. Default: false.
- is_trans_b: A bool. If True, changes the shape of "x2" from [N, K] to
 [K, N] before multiplication. Default: false.
- comm_turn: An int. Number of communications with AICPU. Default: 0.
- antiquant_group_size: An int. Number of per-group for quant. Default: 0.
- group_size: An int. group_size = group size K | group size N << 16 | group size M << 32. Default: 0.
- y_dtype: An int. The y_dtype only support 0(float32)/1(float16)/27(bfloat16) in current version.
Default: 28(ge::DataType::DT_UNDEFINED).
- comm_quant_mode: An int. Number of low-bits communicate mode. Static quant: 0. Dynamic quant: 1. Default: 0.
- comm_mode: An string identifying the communication engine. support "ai_cpu", "ccu", ""(empty string). Default: "".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,int8
- input1 x2: bfloat16,float16,int4,int8
- input2 bias: bfloat16,float16,int32
- input3 x3: bfloat16,float16
- input4 antiquant_scale: bfloat16,float16
- input5 antiquant_offset: bfloat16,float16
- input6 dequant_scale: bfloat16,float16,float32,int64,uint64
- input7 pertoken_scale: float32
- input8 comm_quant_scale_1: bfloat16,float16
- input9 comm_quant_scale_2: bfloat16,float16
- output0 y: bfloat16,float16

## Attention Constraints

- Constraints for MatmulAllreudce:
- MatmulAllReduce has poor performance when the product of the 1th dimension(b) and 2st dimension(s) of input x1 is small.
- x1 can be 2-dimensional or 3-dimensional, and the dimension is (b, s, k) or (m, k). x2 must be
 2-dimensional and its dimension is (k, n). The axis meets the input parameter requirements of the mm operator,
 and their k axes are equal. If bias is not empty, it is 1-dimensional.
- Dimensions except the last one of output are the same as those of x1. The last dimension is the same as
 that of x2. If bias is not empty, the shape size is the same as the last dimension of output.
- The input data type of x1, x2 and bias (if supported) computation must be the same as the output data
 type of output computation.
- The x2 matrix can be transposed or not transposed. The x1 matrix cannot be transposed.
- The Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component support 1, 2, 4, and 8 cards.
- Constraints for WeightQuantMatmulAllreudce:
- WeightQuantMatmulAllreudce has poor performance when the product of the 1th dimension(b) and 2st dimension(s) of input x1 is small.
- x1 can be 2-dimensional or 3-dimensional, and the dimension is (b, s, k) or (m, k). x2 must be
 2-dimensional. Its dimension is (k, n). The k axis meets the input parameter requirements of the matmul operator.
 Their k axes are equal. The range of k and n is [1, 65535].
- The passed x1, x2, antiquant_scale, or output cannot be a null pointer.
- Dimensions except the last one of x3 (non-empty) and output are the same as those of x1. The last
 dimension of x3 (non-empty) and output are the same as that of x2. If bias is not empty, the shape
 size is the same as the last dimension of output. The shape of antiquant_scale is [1] in the per-tensor
 scenario, [1,n]\[n] in the per-channel scenario, and [ceil(k,antiquant_group_size),n] in the per-group scenario. If
 `n` is 1, there is only one element in both per-tensor and per-channel scenarios, and the per-channel scenario
 equals the per-tensor scenario. If antiquantOffset is not empty, the shape is the same as that of antiquant_scale.
- The data types and data formats of x1, x2, x3 (non-empty), antiquant_scale,
 antiquantOffset (non-empty), output, and bias (non-empty) must be supported.
- The output data types of x1, antiquant_scale, antiquantOffset (non-empty), x3 (non-empty), and
 bias (non-empty) must be the same.
- The value of antiquant_group_size must be within the value range and be a multiple of 32.
- The x2 matrix can be transposed or not transposed. The x1 matrix cannot be transposed.
- In the long sequence scenario, as b/s or m increases, OOM or computation timeout may occur.
- When the format of x2 is FRACTAL_NZ, only two dimensions are supported. CalculateMatmulWeightSizeV2
 TransMatmulWeightGetWorkspaceSize/TransMatmulWeight needs to be used to convert the format ND into NZ.
- The Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component support 1, 2, 4, and 8 cards.
- Constraints for QuantMatmulAllreudce:
- QuantMatmulAllreudce has poor performance when the product of the 1th dimension(b) and 2st dimension(s) of input x1 is small.
- x1 can be a 2-dimensional or 3-dimensional tensor and cannot be empty. The dimension of x1 is (b, s, k)
 or (m, k). x2 must be 2-dimensional. Its dimension is (k, n). The k axis meets the input parameter
 requirements of the mm operator, and their k axes are equal.
- Dimensions except the last one of output are the same as those of x1. The last dimension is the same as
 that of x2. If bias is not empty, the shape size is the same as the last dimension of output. If x3
 is not empty, the shape size is the same as that of output.
- The passed x1, x2, dequantScale, or output cannot be a null pointer.
- The data types and data formats of x1, x2, dequantScale, output, bias (non-empty),
 and x3 (non-empty) must be within the supported ranges.
- If output is of FLOAT16 type, the type of dequantScale is INT64 or UINT64 (x3 is not supported in
 this case). If  output is of BFLOAT16 type, the types of dequantScaleand x3 both are BFLOAT16.
- The value of reduce_op must be within the available range. Currently, only sum is supported.
- The x2 matrix can be transposed or not transposed. The x1 matrix cannot be transposed.
- The Ascend 950 AI processor newly suported hifloat8, float8_e5m2, float8_e4m3, float4_e2m1, float4_e1m2,
 output suport float32 when input datatype is hifloat8, float8_e5m2, float8_e4m3, float4_e2m1, float4_e1m2.
- The Atlas A2 Training Series Product/Atlas 800I A2 Inference Product/A200I A2 Box Heterogeneous Component support 1, 2, 4, and 8 cards.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
