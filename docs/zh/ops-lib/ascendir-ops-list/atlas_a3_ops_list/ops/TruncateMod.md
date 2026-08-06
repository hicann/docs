# TruncateMod

```c
REG_OP(TruncateMod)
    .INPUT(x1, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT64, DT_INT8, DT_UINT8,
                           DT_INT32}))
    .INPUT(x2, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT64, DT_INT8, DT_UINT8,
                           DT_INT32}))
    .OUTPUT(y, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_INT64, DT_INT8, DT_UINT8,
                           DT_INT32}))
    .OP_END_FACTORY_REG(TruncateMod)
```

## Brief

Returns element-wise remainder of division. Support broadcasting operations.

## Inputs

Two inputs, including:
- x1: A ND Tensor. Must be one of the following types: bfloat16, float16, float32,
double, int32, int64, int8, uint8.
- x2: A ND Tensor of the same dtype as "x1".

## Outputs

y: A ND Tensor. Has the same dtype as "x1". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32,int8,int32,uint8
- input1 x2: bfloat16,float16,float32,int8,int32,uint8
- output0 y: bfloat16,float16,float32,int8,int32,uint8
### AI CPU
- input0 x1: double,float16,float32,int32,int64
- input1 x2: double,float16,float32,int32,int64
- output0 y: double,float16,float32,int32,int64

## Attention Constraints

- x2: The input data does not support 0
- When value of tensor exceeds 2048 , the accuracy of operator cannot guarantee the
requirement of double thousandths in Atlas 200/300/500 Inference Product.
- Due to different architectures, the calculation results of this operator
on NPU and CPU may be inconsistent
- If shape is expressed as (D1,D2... ,Dn), then D1*D2... *DN<=1000000,n<=8

## Third-party framework compatibility

Compatible with the TensorFlow operator TruncateMod.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
