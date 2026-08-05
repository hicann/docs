# FloorMod

```c
REG_OP(FloorMod)
    .INPUT(x1, TensorType({DT_INT32, DT_INT64, DT_FLOAT,
                           DT_FLOAT16, DT_DOUBLE, DT_BF16}))
    .INPUT(x2, TensorType({DT_INT32, DT_INT64, DT_FLOAT,
                           DT_FLOAT16, DT_DOUBLE, DT_BF16}))
    .OUTPUT(y, TensorType({DT_INT32, DT_INT64, DT_FLOAT,
                           DT_FLOAT16, DT_DOUBLE, DT_BF16}))
    .OP_END_FACTORY_REG(FloorMod)
```

## Brief

Returns element-wise remainder of division.
Consistent with: floor(x1/x2) * x2 + mod(x1, x2) = x1.
Integer division by zero on NPU returns x1. Support broadcasting operations.

## Inputs

Two inputs, including:
- x1: A ND tensor. Must be one of the following types:
   int32, int64, float, float16, double, bfloat16
- x2: A ND tensor. Must have the same dtype as "x1".

## Outputs

y: A ND tensor. Has the same dtype as "x1".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32,int32,int64
- input1 x2: bfloat16,float16,float32,int32,int64
- output0 y: bfloat16,float16,float32,int32,int64
### AI CPU
- input0 x1: double,float16,float32,int32,int64
- input1 x2: double,float16,float32,int32,int64
- output0 y: double,float16,float32,int32,int64

## Attention Constraints

- x2: The input data does not support 0
- When value of tensor exceeds 2048 , the accuracy of operator cannot guarantee the
requirement of double thousandths in the mini platform
- Due to different architectures, the calculation results of this operator
on NPU and CPU may be inconsistent
- If shape is expressed as (D1,D2... ,Dn), then D1*D2... *DN<=1000000,n<=8

## Third-party framework compatibility

Compatible with the TensorFlow operator FloorMod.


---

[Back to Operator Specifications (Ascend950)](../README.md)
