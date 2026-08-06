# PadV2

```c
REG_OP(PadV2)
    .INPUT(x, TensorType({TensorType::BasicType(), DT_BOOL, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN,
                          DT_FLOAT8_E8M0, DT_FLOAT4_E2M1, DT_FLOAT4_E1M2}))
    .INPUT(paddings, TensorType::IndexNumberType())
    .INPUT(constant_values, TensorType({TensorType::BasicType(), DT_BOOL, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN,
                                        DT_FLOAT8_E8M0, DT_FLOAT4_E2M1, DT_FLOAT4_E1M2}))
    .OUTPUT(y, TensorType({TensorType::BasicType(), DT_BOOL, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN,
                           DT_FLOAT8_E8M0, DT_FLOAT4_E2M1, DT_FLOAT4_E1M2}))
    .OP_END_FACTORY_REG(PadV2)
```

## Brief

Pads a tensor with constant values.

## Inputs

Three inputs, including:
- x: A Tensor. Must be one of the following types: float16, bfloat16,
float32, double, int32, uint8, int16, int8, complex64, int64,
qint8, quint8, qint32, qint16, quint16, uint16, complex128, uint32, uint64, bool,
hifloat8, float8_e5m2, float8_e4m3fn, float8_e8m0, float4_e2m1, float4_e1m2.
Supported format list: ["ND"].
- paddings: A Tensor of type int32 or int64.
The shape of paddings must be [N, 2], where N is the rank of x.
paddings[i][0] specifies the number of padding elements to add before x in dimension i.
paddings[i][1] specifies the number of padding elements to add after x in dimension i.
Supported format list: ["ND"].
- constant_values: An optional Tensor, dtype same as "x".
Used only in "constant" mode to specify the value to fill in the padded regions.
If not provided, default value is 0. 

## Outputs

y: A Tensor of the same type as "x".
y.shape[i] = x.shape[i] + paddings[i][0] + paddings[i][1], where y.shape[i] >= 0.
Supported format list: ["ND"]. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int64
- input1 paddings: int32,int64
- input2 constant_values: float16,float32,int64
- output0 y: float16,float32,int64
### AI CPU
- input0 x: bool,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float8_e8m0,hifloat8
- input1 paddings: int32,int64
- input2 constant_values: bool,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float8_e8m0,hifloat8
- output0 y: bool,float4_e1m2,float4_e2m1,float8_e4m3fn,float8_e5m2,float8_e8m0,hifloat8

## Attention Constraints

If the type of x is float4_e2m1 or float4_e1m2, paddings values should be even number.
If the type of x is hifloat8, float8_e5m2, float8_e4m3fn or float8_e8m0,
paddings values should be non-negative integers.
The constant_values should be a scalar tensor with the same dtype as x. 

## Third-party framework compatibility

Compatible with TensorFlow operator PadV2.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
