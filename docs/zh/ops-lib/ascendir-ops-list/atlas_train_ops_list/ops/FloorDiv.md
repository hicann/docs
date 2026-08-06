# FloorDiv

```c
REG_OP(FloorDiv)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_INT32, DT_UINT8,
                           DT_INT64, DT_INT16, DT_UINT16, DT_DOUBLE, DT_BF16}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_INT32, DT_UINT8,
                           DT_INT64, DT_INT16,DT_UINT16, DT_DOUBLE, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT8, DT_INT32, DT_UINT8,
                           DT_INT64, DT_INT16,DT_UINT16, DT_DOUBLE, DT_BF16}))
    .OP_END_FACTORY_REG(FloorDiv)
```

## Brief

Divides "x1/x2" element-wise, rounding toward the
       most negative integer. Support broadcasting operations.

## Inputs

Two inputs, including:
- x1: A ND Tensor.
Must be one of the following types: float16, float32, int32, int64, int8,
    uint8, int16, uint16, double, bfloat16.
- x2: A ND Tensor of the same dtype as "x1".

## Outputs

y: A ND Tensor. Has the same dtype as "x1". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32,int8,int32,int64,uint8
- input1 x2: float16,float32,int8,int32,int64,uint8
- output0 y: float16,float32,int8,int32,int64,uint8
### AI CPU
- input0 x1: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 x2: double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Third-party framework compatibility

Compatible with the TensorFlow operator FloorDiv.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
