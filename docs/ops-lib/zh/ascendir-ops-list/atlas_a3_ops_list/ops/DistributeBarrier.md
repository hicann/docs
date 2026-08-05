# DistributeBarrier

```c
REG_OP(DistributeBarrier)
    .INPUT(x_ref, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_BOOL, DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64}))
    .OPTIONAL_INPUT(time_out, TensorType({DT_INT32}))
    .OPTIONAL_INPUT(elastic_info, TensorType({DT_INT32}))
    .OUTPUT(x_ref, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_BOOL, DT_INT8, DT_INT16, DT_INT32, DT_INT64, DT_UINT8, DT_UINT16, DT_UINT32, DT_UINT64}))
    .REQUIRED_ATTR(group, String)
    .REQUIRED_ATTR(world_size, Int)
    .OP_END_FACTORY_REG(DistributeBarrier)
```

## Brief

DistributeBarrier operator interface implementation.

## Inputs

Three inputs, including:
- x_ref: An optional tensor, reserved. Support dtype:bfloat16, float16, float32, bool, int8, int16, int32, int64, uint8, uint16, uint32, uint64. Support format: ND.
- time_out: An optional tensor. Support dtype:int32. Support format: ND.
- elastic_info: An optional tensor. Support dtype:int32. Support format: ND.

## Outputs

One outputs, including:
- x_ref: A tensor. reserved. Support dtype:bfloat16, float16, float32, bool, int8, int16, int32, int64, uint8, uint16, uint32, uint64. Support format: ND.

## Attributes

- group: Required. Input comm group name, means experts parallelism, dtype: String.
- world_size: Required. Input comm world size, dtype: int64.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x_ref: bfloat16,bool,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int4,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 time_out: int32
- input2 elastic_info: int32
- output0 x_ref: bfloat16,bool,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float16,float32,hifloat8,int4,int8,int16,int32,int64,uint8,uint16,uint32,uint64


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
