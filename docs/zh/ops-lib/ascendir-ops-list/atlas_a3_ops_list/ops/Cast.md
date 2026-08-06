# Cast

```c
REG_OP(Cast)
    .INPUT(x, TensorType({DT_BOOL, DT_FLOAT16, DT_FLOAT, DT_INT8, DT_INT32, DT_UINT32, DT_UINT8,
                          DT_INT64, DT_UINT64, DT_INT16, DT_UINT16, DT_DOUBLE, DT_COMPLEX64,
                          DT_COMPLEX128, DT_QINT8, DT_QUINT8, DT_QINT16, DT_QUINT16, DT_QINT32, DT_BF16, DT_UINT1,
                          DT_COMPLEX32, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN,
                          DT_FLOAT4_E1M2, DT_FLOAT4_E2M1}))
    .OUTPUT(y, TensorType({DT_BOOL, DT_FLOAT16, DT_FLOAT, DT_INT8, DT_INT32, DT_UINT32, DT_UINT8,
                           DT_INT64, DT_UINT64, DT_INT16, DT_UINT16, DT_DOUBLE, DT_COMPLEX64,
                           DT_COMPLEX128, DT_QINT8, DT_QUINT8, DT_QINT16, DT_QUINT16, DT_QINT32,
                           DT_BF16, DT_COMPLEX32, DT_HIFLOAT8, DT_FLOAT8_E5M2, DT_FLOAT8_E4M3FN,
                           DT_FLOAT4_E1M2, DT_FLOAT4_E2M1, DT_INT4}))
    .REQUIRED_ATTR(dst_type, Int)
    .OP_END_FACTORY_REG(Cast)
```

## Brief

Cast a tensor from src data type to dst data type.

## Inputs

One input:
x:An ND or 5HD tensor. Support 1D~8D. Must be one of the following types: bool, float16, float, int8, int32, uint32, uint8, bfloat16, uint1,
int64, uint64, int16, uint16, double, complex32, complex64, complex128, qint8, quint8, qint16, quint16, qint32,
hifloat8, float8_e5m2, float8_e4m3fn, float4_e1m2, float4_e2m1.

## Outputs

y:An ND Tensor with same shape as x, and data type is specified by dst_type.

## Attributes

dst_type: A required attribute of type int32, specifying the dst data type.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,float16,float32,int8,int16,int32,int64,uint1,uint8,uint16,uint32
- output0 y: bfloat16,bool,complex32,complex64,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32
### AI CPU
- input0 x: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bfloat16,bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

- In the scenario where the data type is converted from float16 to int16:
    If the input data contains inf, inf is converted into the maximum value of int16. 
    If the input data contains -inf, -inf is converted into the minimum value of int16. 
- In the scenarios where the data type is converted from INT32 to INT8:
    It can only guarantee that the input data has no precision errors within the range of (-2048, 1920).
- Atlas Inference Series Product in the scenarios where the data type is converted from FLOAT32 to INT8:
    It can only guarantee that the input data has no precision errors within the range of (-2048, 1920).
- Atlas Inference Series Product in the scenarios where the data type is converted from FLOAT32 to INT64 and from FLOAT32 to UINT8:
    It can only guarantee that the input data has no precision errors within the range of (-2147483648, 2147483583).
- Atlas Inference Series Product in the scenarios where the data type is converted from INT64 to FLOAT32:
    It can only guarantee that the input data has no precision errors within the range of (-2147483648, 2147483647).
- Ascend 950 AI Processor in the scenario where the data type is converted from INT32 to INT4:
    The last dim of x must be an even number.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
