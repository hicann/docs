# Pad

```c
REG_OP(Pad)
    .INPUT(x, TensorType({TensorType::BasicType(), DT_BOOL, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN,
                          DT_FLOAT8_E8M0, DT_FLOAT4_E2M1, DT_FLOAT4_E1M2}))
    .INPUT(paddings, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType({TensorType::BasicType(), DT_BOOL, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN,
                           DT_FLOAT8_E8M0, DT_FLOAT4_E2M1, DT_FLOAT4_E1M2}))
    .OP_END_FACTORY_REG(Pad)
```

## Brief

Pad a tensor.

## Inputs

Two inputs, including:
- x: A Tensor. Must be one of the following types: bfloat16, float16,
    float32, double, int32, uint8, int16, int8, complex64, int64, qint8,
    quint8, qint32, qint16, quint16, uint16, complex128, uint32, uint64, bool,
    hifloat8, float8_e5m2, float8_e4m3fn, float8_e8m0, float4_e2m1, float4_e1m2. Supported format list ["ND"].
- paddings: A Tensor of type int32 or int64. Supported format list ["ND"].

## Outputs

y: A Tensor of the same type as "x". Supported format list ["ND"]. 
- Due to different architectures, the calculation results of this operator
on NPU and CPU may be inconsistent. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float8_e8m0,hifloat8
- input1 paddings: int32,int64
- output0 y: bool,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float8_e8m0,hifloat8
### AI CPU
- input0 x: bool,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float8_e8m0,hifloat8
- input1 paddings: int32,int64
- output0 y: bool,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float8_e8m0,hifloat8

## Attention Constraints

If the type of x is float4_e2m1 or float4_e1m2, paddings values should be even number.
If the type of x is hifloat8, float8_e5m2, float8_e4m3fn or float8_e8m0,
paddings values should be non-negative integers. 

## Third-party framework compatibility

Compatible with TensorFlow operator Pad.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
