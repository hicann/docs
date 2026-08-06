# ZerosLike

```c
REG_OP(ZerosLike)
    .INPUT(x, TensorType({BasicType(), DT_VARIANT, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_HIFLOAT8, DT_FLOAT4_E1M2, DT_FLOAT4_E2M1}))
    .OUTPUT(y, TensorType({BasicType(), DT_VARIANT, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_HIFLOAT8, DT_FLOAT4_E1M2, DT_FLOAT4_E2M1}))
    .OP_END_FACTORY_REG(ZerosLike)
```

## Brief

Returns a tensor of the same dtype and shape as the input tensor with all elements set to zero.

## Inputs

x: An ND or 5HD tensor. support 1D ~ 8D. Must be one of the following types: BasicType() and variant.

## Outputs

y: A ND Tensor of the same data type as "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,float16,float32,int8,int32,int64,uint8
- output0 y: bfloat16,bool,float16,float32,int8,int32,int64,uint8
### AI CPU
- input0 x: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,string,uint8,uint16,variant
- output0 y: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,string,uint8,uint16,variant

## Attention Constraints

The output has the same shape and type as the input.
The dtype DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_HIFLOAT8, DT_FLOAT4_E1M2, DT_FLOAT4_E2M1 only support version since Ascend950

## Third-party framework compatibility

Compatible with the TensorFlow operator zeros_like.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
