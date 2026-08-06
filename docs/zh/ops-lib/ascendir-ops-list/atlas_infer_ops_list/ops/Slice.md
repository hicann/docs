# Slice

```c
REG_OP(Slice)
    .INPUT(x, TensorType({BasicType(), DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT8_E8M0, DT_FLOAT4_E2M1, DT_FLOAT4_E1M2}))
    .INPUT(offsets, TensorType::IndexNumberType())
    .INPUT(size, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType({BasicType(), DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN, DT_FLOAT8_E8M0, DT_FLOAT4_E2M1, DT_FLOAT4_E1M2}))
    .OP_END_FACTORY_REG(Slice)
```

## Brief

Extracts a slice from a tensor.
      This operation extracts a slice of size "size" from a tensor "x"
      starting at the location specified by "offsets".

## Inputs

- x: A Tensor. Must be one of the following types:
bfloat16, float16, float32, double, int64, int32, uint8, uint16, uint32, uint64, int8,
int16, complex64, complex128, qint8, quint8, qint16, quint16, qint32, hifloat8, float8_e5m2, float8_e4m3fn
float8_e8m0, float4_e2m1, float4_e1m2.
- offsets: A Tensor of type int32 or int64. The starting location for the slice.
- size: A Tensor of type int32 or int64. The tensor size for the slice.

## Outputs

y: A Tensor. Has the same type as "x". The slice extracted from the tensor. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 offsets: int32,int64
- input2 size: int32,int64
- output0 y: bool,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
### AI CPU
- input0 x: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 offsets: int32,int64
- input2 size: int32,int64
- output0 y: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

- 0 <= offset[i] <= offset[i] + size[i] <= x_dim[i] for i in [0,n],
n is the dimension of the tensor "x". 
- offsets, size and x must have the same rank.

## Third-party framework compatibility

Compatible with the TensorFlow operator Slice.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
