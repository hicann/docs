# QuantAllReduce

```c
REG_OP(QuantAllReduce)
    .INPUT(x, "T1")
    .INPUT(scales, "T2")
    .OUTPUT(out_put, "T3")
    .DATATYPE(T1, TensorType({DT_INT8, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT4_E1M2, DT_FLOAT4_E2M1}))
    .DATATYPE(T2, TensorType({DT_FLOAT, DT_FLOAT8_E8M0}))
    .DATATYPE(T3, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .REQUIRED_ATTR(group, String)
    .ATTR(reduce_op, String, "sum")
    .ATTR(output_dtype, Int, DT_BF16)
    .REQUIRED_ATTR(world_size, Int)
    .OP_END_FACTORY_REG(QuantAllReduce)
```

## Brief

Fusion op of quant all reduce.

## Inputs

two inputs, including:
- x: A matrix tensor. The type support int8, hifloat8, float8_e4m3fn, float8_e5m2, float4_e1m2, float4_e2m1. The format supports ND.
- scale: A matrix tensor. The type support float32, float8_e8m0. The format supports ND.

## Outputs

out_put: A matrix tensor. The type support float16, bfloat16, float32. The format supports ND.

## Attributes

- group: A required string identifying the group of ranks participating in the op.
- reduce_op: An optional string identifying the reduction operation to perform. Default: "sum".
- output_dtype: An optional int identifying the data type of output. The type support 0(float), 1(float16), 27(bfloat16). Default: 27(bfloat16).
- world_size: A required int identifying the rank size.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,hifloat8,int8
- input1 scales: float8_e8m0,float32
- output0 out_put: bfloat16,float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
