# PadV3

```c
REG_OP(PadV3)
    .INPUT(x, TensorType({TensorType::BasicType(), DT_BOOL, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN,
                          DT_FLOAT8_E8M0, DT_FLOAT4_E2M1, DT_FLOAT4_E1M2}))
    .INPUT(paddings, TensorType::IndexNumberType())
    .OPTIONAL_INPUT(constant_values, TensorType({TensorType::BasicType(), DT_BOOL, DT_HIFLOAT8, DT_FLOAT8_E5M2,
                                                 DT_FLOAT8_E4M3FN, DT_FLOAT8_E8M0, DT_FLOAT4_E2M1, DT_FLOAT4_E1M2}))
    .OUTPUT(y, TensorType({TensorType::BasicType(), DT_BOOL, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN,
                           DT_FLOAT8_E8M0, DT_FLOAT4_E2M1, DT_FLOAT4_E1M2}))
    .ATTR(mode, String, "constant")
    .ATTR(paddings_contiguous, Bool, true)
    .OP_END_FACTORY_REG(PadV3)
```

## Brief

Pads a tensor.

## Inputs

Three inputs, including:
- x: A Tensor. Must be one of the following types: float16, bfloat16,
float32, double, int32, uint8, int16, int8, complex64, int64,
qint8, quint8, qint32, qint16, quint16, uint16, complex128, uint32, uint64, bool,
hifloat8, float8_e5m2, float8_e4m3fn, float8_e8m0, float4_e2m1, float4_e1m2.
- paddings: A Tensor of type int32 or int64, specify the padding sizes.
The size of paddings should be twice of the x shape size.
If the type of x is float4_e2m1 or float4_e1m2, paddings values should be even number.
If the type of x is hifloat8, float8_e5m2, float8_e4m3fn or float8_e8m0,
paddings values should be non-negative integers.
- constant_values: An optional Tensor, dtype same as "x".
Is used only in "constant" mode.

## Outputs

y: A Tensor of the same type as "x".
y.shape[i] = x.shape[i] + leftpad_i + rightpad_i, where y.shape[i] >= 0.

## Attributes

- mode: An optional string, Defaults to "constant", indicates paddings mode,
support "constant", "reflect", "edge", "symmetric", "circular".
In constant mode the padded value is constant_values, default 0 while constant_values is null.
In edge mode the padded value is the border value of input x.
In reflect mode the padded value do not include the borders,
while in symmetric mode the padded value do include the borders.
In circular mode, pads x using circular of the input boundary.
- paddings_contiguous: An optional bool value, Defaults to true.
If true, paddings is arranged as [[leftpad_0, rightpad_0], [leftpad_1, rightpad_1], ...]
If false, paddings is arranged as [[leftpad_0, leftpad_1, ...], [rightpad_0, rightpad_1, ...]]

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8,int32
- input1 paddings: int32,int64
- input2 constant_values: float16,float32,int8,int32
- output0 y: float16,float32,int8,int32
### AI CPU
- input0 x: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 paddings: int32,int64
- input2 constant_values: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

"symmetric" and "circular" mode is supported since arch35. 
"symmetric" mode: the leftpad_i and rightpad_i should be in [-x.shape[i], x.shape[i]]. 
"reflect" mode: the leftpad_i and rightpad_i should be in [-x.shape[i], x.shape[i]). 
"constant" mode: the leftpad_i and rightpad_i should be greater than or equal to -x.shape[i]. 
"edge" mode: the leftpad_i and rightpad_i should be greater than or equal to -x.shape[i]. 
"circular" mode: the leftpad_i and rightpad_i should be in [-x.shape[i], x.shape[i]]. 

## Third-party framework compatibility

Compatible with ONNX operator Pad.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
