# GroupedMatmulSwigluQuantV2

```c
REG_OP(GroupedMatmulSwigluQuantV2)
      .INPUT(x, TensorType({DT_INT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT4_E2M1, DT_HIFLOAT8, DT_FLOAT4_E1M2}))
      .INPUT(x_scale, TensorType({DT_FLOAT, DT_FLOAT8_E8M0}))
      .INPUT(group_list, TensorType{DT_INT64})
      .DYNAMIC_INPUT(weight, TensorType({DT_INT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT4_E2M1, DT_HIFLOAT8, DT_FLOAT4_E1M2}))
      .DYNAMIC_INPUT(weight_scale, TensorType({DT_FLOAT, DT_FLOAT8_E8M0, DT_BF16, DT_FLOAT16}))
      .DYNAMIC_INPUT(weight_assist_matrix, TensorType{DT_FLOAT})
      .OPTIONAL_INPUT(bias, TensorType{DT_FLOAT})
      .OPTIONAL_INPUT(smooth_scale, TensorType{DT_FLOAT})
      .ATTR(dequant_mode, Int, 0)
      .ATTR(dequant_dtype, Int, 0)
      .ATTR(quant_mode, Int, 0)
      .ATTR(quant_dtype, Int, 0)
      .ATTR(transpose_weight, Bool, false)
      .ATTR(group_list_type, Int, 0)
      .ATTR(tuning_config, ListInt, {0})
      .OUTPUT(y, TensorType({DT_INT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT4_E2M1, DT_HIFLOAT8, DT_FLOAT4_E1M2}))
      .OUTPUT(y_scale, TensorType({DT_FLOAT, DT_FLOAT8_E8M0}))
      .OP_END_FACTORY_REG(GroupedMatmulSwigluQuantV2)
```

## Brief

GroupedMatmulSwigluQuantV2 operator interface implementation.

## Inputs

- x: A tensor. The format supports ND. The type supports int8, float8_e5m2, float8_e4m3fn, float4_e2m1, hifloat8, float4_e1m2(only weight nz supported).
- x_scale: A tensor. Scales for x for each token. The format supports ND. The type supports float32, float8_e8m0.
- group_list: A tensor. Indicates the matmul size distribution along separated dimension.
The format supports ND. The type supports int64. The first dimension of group_list should not be greater than 1024, meaning it supports up to 1024 groups.
- weight: A tensor List. The format supports ND/NZ. The type supports int8, float8_e5m2, float8_e4m3fn, float4_e2m1, hifloat8, float4_e1m2(only weight nz supported).
In MXFP4 and MXFP8 scenarios, weight supports either one tensor or multiple tensors. In the multi-tensor
weight-NZ scenario, the tensor list length must equal the number of groups.
- weight_scale: A tensor List. Format supports ND. The type supports float32, float8_e8m0, bfloat16, float16.
In the multi-tensor weight-NZ scenario, its tensor list length must equal that of weight.
- weight_assist_matrix: A tensor List. The format supports ND. The type supports float32.
- bias: A tensor. The format supports ND. The type supports float32.
- smooth_scale: A tensor. The format supports ND. The type supports float32.

## Attributes

- dequant_mode: Optional. Indicates the mode of dequant. dtype: Int64. Default: 0. Reserved parameter.
- dequant_dtype: Optional. Indicates the dtype of dequant. dtype: Int64. Default: 0. Reserved parameter.
- quant_mode: Optional. Indicates the mode of quant. dtype: Int64. Default: 0. Reserved parameter.
- quant_dtype: Optional. Indicates the dtype of quant. dtype: Int64. Default: 0. Reserved parameter.
- transpose_weight: A bool. Default: false. Reserved parameter.
- group_list_type: An int. Indicates whether the value in group_list is cumsum or count.
0, value in group_list is cumsum. 1, value in group_list is count. Default: 0.
- tuning_config: A ListInt. The first element in the array indicates the expected number of tokens processed by each expert.
The operator tiling performs optimal tiling based on the first element in the array. Default: {0}.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: int4,int8
- input1 x_scale: float32
- input2 group_list: int64
- input3 weight: int4,int8
- input4 weight_scale: bfloat16,float16,float32,uint64
- input5 weight_assist_matrix: float32
- input6 bias: float32
- input7 smooth_scale: float32
- output0 y: int8
- output1 y_scale: float32

## Attention Constraints

- In the MX quantization scenario with weight format ND, when the input dtype is float8, N must be 2 aligned; when the input dtype is float4, N must be 4 aligned. This constraint applies only to Ascend950PR/Ascend950DT.
- In the MX quantization scenario with weight format NZ, when the input dtype is float8, N must be 64 aligned; when the input dtype is float4, N must be 128 aligned. This constraint applies only to Ascend950PR/Ascend950DT.
- In MXFP4 and MXFP8 multi-tensor weight-NZ scenarios, weight and weight_scale must have the same tensor
list length, and the length must equal the length of group_list. All tensors in each list must have consistent shapes.
- When group_list_type is 0, group_list must be a non-negative monotone non-decreasing array. The last value in group_list must be no greater than the first dimension of tensor x1;
When group_list_type is 1, it must be a non-negative array. Sum of values in group_list must be no greater than the first dimension of tensor x1. 

## Output

- y: A tensor. The type supports int8, float8_e5m2, float8_e4m3fn, float4_e2m1, float4_e1m2, hifloat8. The format supports ND.
- y_scale: A tensor. The type supports float32, float8_e8m0. The format supports ND.
- The following are the supported format, data types and shapes(for Ascend950PR/Ascend950DT):
| Tensor    | x                         | x_scale             | group_list | weight                                            | weight_scale                                    | y                                                    | y_scale                  |
| :-------: | :-----------------------: | :-----------------: | :--------: | :-----------------------------------------------: | :---------------------------------------------: | :--------------------------------------------------: |:-----------------------: |
| Format1   | ND                        | ND                  | ND         | ND                                                | ND                                              | ND                                                   | ND                       |
| Dtype     | float8_e4m3fn/float8_e5m2 | float8_e8m0         | int64      | float8_e4m3fn/float8_e5m2                         | float8_e8m0                                     | float8_e4m3fn/float8_e5m2                            | float8_e8m0              |
| Shape     | (M,K)                     | (M,ceil(K/64),2)    | (B,)       | [(B,K,N)]/[(B,N,K)]                               | [(B,ceil(K/64),N,2)]/[(B,N,ceil(K/64),2)]       | (M,N/2)                                              | (M,ceil((N/2)/64),2)     |
| Dtype     | float4_e2m1               | float8_e8m0         | int64      | float4_e2m1                                       | float8_e8m0                                     | float8_e4m3fn/float8_e5m2/float4_e2m1                | float8_e8m0              |
| Shape     | (M,K)                     | (M,ceil(K/64),2)    | (B,)       | [(B,K,N)]/[(B,N,K)]                               | [(B,ceil(K/64),N,2)]/[(B,N,ceil(K/64),2)]       | (M,N/2)                                              | (M,ceil((N/2)/64),2)     |
| Dtype     | int8                      | float32             | int64      | int8                                              | bf16/float32/float16                            | int8                                                 | float32                  |
| Shape     | (M,K)                     | (M,)                | (B,)       | [(B,K,N)]/[(B,N,K)]                               | (B,N)                                         | (M,N/2)                                              | (M,)                     |
| Dtype     | float8_e4m3fn/float8_e5m2 | float32             | int64      | float8_e4m3fn/float8_e5m2                         | bf16/float32                                    | float8_e4m3fn/float8_e5m2                            | float32                  |
| Shape     | (M,K)                     | (M,)                | (B,)       | [(B,K,N)]/[(B,N,K)]                               | (B,N)                                         | (M,N/2)                                              | (M,)                     |
| Dtype     | hifloat8                  | float32             | int64      | hifloat8                                          | bf16/float32                                    | hifloat8                                             | float32                  |
| Shape     | (M,K)                     | (M,)                | (B,)       | [(B,K,N)]/[(B,N,K)]                               | (B,N)                                         | (M,N/2)                                              | (M,)                     |
| Format2   | ND                        | ND                  | ND         | FRACTAL_NZ                                        | ND                                              | ND                                                   | ND                       |
| Dtype     | float8_e4m3fn             | float8_e8m0         | int64      | float8_e4m3fn                                     | float8_e8m0                                     | float8_e4m3fn                                        | float8_e8m0              |
| Shape     | (M,K)                     | (M,ceil(K/64),2)    | (B,)       | [(B,N/32,K/16,16,32)]/[(B,K/32,N/16,16,32)]       | [(B,ceil(K/64),N,2)]/[(B,N,ceil(K/64),2)]       | (M,N/2)                                              | (M,ceil((N/2)/64),2)     |
| Shape     | (M,K)                     | (M,ceil(K/64),2)    | (B,)       | [(N,K),(N,K),...]/[(K,N),(K,N),...]               | [(N,ceil(K/64),2),...]/[(ceil(K/64),N,2),...]   | (M,N/2)                                              | (M,ceil((N/2)/64),2)     |
| Dtype     | float4_e2m1               | float8_e8m0         | int64      | float4_e2m1                                       | float8_e8m0                                     | float4_e2m1                                          | float8_e8m0              |
| Shape     | (M,K)                     | (M,ceil(K/64),2)    | (B,)       | [(B,N/64,K/16,16,64)]/[(B,K/64,N/16,16,64)]       | [(B,ceil(K/64),N,2)]/[(B,N,ceil(K/64),2)]       | (M,N/2)                                              | (M,ceil((N/2)/64),2)     |
| Shape     | (M,K)                     | (M,ceil(K/64),2)    | (B,)       | [(N,K),(N,K),...]/[(K,N),(K,N),...]               | [(N,ceil(K/64),2),...]/[(ceil(K/64),N,2),...]   | (M,N/2)                                              | (M,ceil((N/2)/64),2)     |
| Dtype     | float4_e1m2               | float8_e8m0         | int64      | float4_e2m1                                       | float8_e8m0                                     | float4_e2m1                                          | float8_e8m0              |
| Shape     | (M,K)                     | (M,ceil(K/64),2)    | (B,)       | [(B,N/64,K/16,16,64)]/[(B,K/64,N/16,16,64)]       | [(B,ceil(K/64),N,2)]/[(B,N,ceil(K/64),2)]       | (M,N/2)                                              | (M,ceil((N/2)/64),2)     |
| Shape     | (M,K)                     | (M,ceil(K/64),2)    | (B,)       | [(N,K),(N,K),...]/[(K,N),(K,N),...]               | [(N,ceil(K/64),2),...]/[(ceil(K/64),N,2),...]   | (M,N/2)                                              | (M,ceil((N/2)/64),2)     |
| Dtype     | float4_e2m1               | float8_e8m0         | int64      | float4_e1m2                                       | float8_e8m0                                     | float4_e2m1                                          | float8_e8m0              |
| Shape     | (M,K)                     | (M,ceil(K/64),2)    | (B,)       | [(B,N/64,K/16,16,64)]/[(B,K/64,N/16,16,64)]       | [(B,ceil(K/64),N,2)]/[(B,N,ceil(K/64),2)]       | (M,N/2)                                              | (M,ceil((N/2)/64),2)     |
| Shape     | (M,K)                     | (M,ceil(K/64),2)    | (B,)       | [(N,K),(N,K),...]/[(K,N),(K,N),...]               | [(N,ceil(K/64),2),...]/[(ceil(K/64),N,2),...]   | (M,N/2)                                              | (M,ceil((N/2)/64),2)     |
| Dtype     | float4_e1m2               | float8_e8m0         | int64      | float4_e1m2                                       | float8_e8m0                                     | float4_e2m1                                          | float8_e8m0              |
| Shape     | (M,K)                     | (M,ceil(K/64),2)    | (B,)       | [(B,N/64,K/16,16,64)]/[(B,K/64,N/16,16,64)]       | [(B,ceil(K/64),N,2)]/[(B,N,ceil(K/64),2)]       | (M,N/2)                                              | (M,ceil((N/2)/64),2)     |
| Shape     | (M,K)                     | (M,ceil(K/64),2)    | (B,)       | [(N,K),(N,K),...]/[(K,N),(K,N),...]               | [(N,ceil(K/64),2),...]/[(ceil(K/64),N,2),...]   | (M,N/2)                                              | (M,ceil((N/2)/64),2)     |


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
