# QuantGroupedMatmulInplaceAdd

```c
REG_OP(QuantGroupedMatmulInplaceAdd)
    .INPUT(x1, TensorType({DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .INPUT(x2, TensorType({DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN}))
    .INPUT(scale2, TensorType({DT_FLOAT, DT_FLOAT8_E8M0}))
    .INPUT(group_list, TensorType({DT_INT64}))
    .INPUT(y, TensorType({DT_FLOAT}))
    .OPTIONAL_INPUT(scale1, TensorType({DT_FLOAT, DT_FLOAT8_E8M0}))
    .OUTPUT(y, TensorType({DT_FLOAT}))
    .ATTR(group_list_type, Int, 0)
    .ATTR(group_size, Int, 0)
    .OP_END_FACTORY_REG(QuantGroupedMatmulInplaceAdd)
```

## Brief

Function QuantGroupedMatmulInplaceAdd. This op fuse GroupedMatmul with InplaceAdd.

## Inputs

- x1: A tensor. Format supports ND. Data type supports hifloat8, float8_e5m2, float8_e4m3fn.
- x2: A tensor. Format supports ND. Data type supports hifloat8, float8_e5m2, float8_e4m3fn.
- scale2: A tensor. Indicating scaling factor of quantization parameter, introduced by x2 quantization.
Format supports ND. Data type supports float32, float8_e8m0.
- group_list: A tensor. Indicating the matmul size distribution along separated dimension.
Format supports ND. Data type supports int64. The first dimension of group_list should not be greater than 1024, meaning it supports up to 1024 groups.
- y: A tensor. Format supports ND. Data type supports float32.
- scale1: A tensor. Indicating the scaling factor of the quantization parameter, introduced by x1 quantization.
Format supports ND. The data type supports float32, float8_e8m0.

## Outputs

y: A Tensor. Format supports ND.
The data type supports float32.
- The following are the supported quantization modes, data types and shapes(for Ascend950PR/Ascend950DT):
| quantization         | x1 type                   | x2 type                   | scale1 type                    | scale2 type                    | x1 shape  | x2 shape            | y shape   | scale2 shape                  | scale1 shape          |
|----------------------|---------------------------|---------------------------|--------------------------------|--------------------------------|-----------|---------------------|-----------|-------------------------------|-----------------------|
| pertensor-pertensor  | hifloat8                  | hifloat8                  | float32                        | float32                        | (K,M)     | (K,N)               | (B,M,N)   | (B,)/(B,1)                    | (B,)/(B,1)            |
| pertensor-perchannel | hifloat8                  | hifloat8                  | float32                        | float32                        | (K,M)     | (K,N)               | (B,M,N)   | (B,N)                         | (B,)/(B,1)            |
| mx                   | float8_e4m3fn/float8_e5m2 | float8_e4m3fn/float8_e5m2 | float8_e8m0                    | float8_e8m0                    | (K,M)     | (K,N)               | (B,M,N)   | (K/64+B,N,2)                  | (K/64+B,M,2)          |

## Attributes

- group_list_type: An int. Indicates whether the value in group_list is cumsum or count.
0, value in group_list is cumsum. 1, value in group_list is count. Default: 0.
- group_size: An int. Default: 0. Value only supports 0 for now.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float8_e4m3fn,float8_e5m2,hifloat8
- input1 x2: float8_e4m3fn,float8_e5m2,hifloat8
- input2 scale2: float8_e8m0,float32
- input3 group_list: int64
- input4 y: float32
- input5 scale1: float8_e8m0,float32
- output0 y: float32

## Attention Constraints

- When group_list_type is 0, group_list must be a non-negative monotone non-decreasing array, when group_list_type is 1, it must be a non-negative array.
- Each axis for tensor x1 and tensor x2 should be less than or equal to 2147483647 (maximum of data type int32) after aligning to 32 byte.
- Input tensor x1 and x2 should have dim num 2, input tensor y should have dim num 3.
- The group_list must be passed, if group_list_type equals to 0, the last value in group_list must be no greater than the first dimension of tensor x1,
if group_list_type equals to 1, sum of values in group_list must be no greater than the first dimension of tensor x1. 


---

[Back to Operator Specifications (Ascend950)](../README.md)
