# Mod

```c
REG_OP(Mod)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT8, DT_UINT8,
                           DT_INT64, DT_DOUBLE, DT_BF16}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT8, DT_UINT8,
                           DT_INT64, DT_DOUBLE, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT8, DT_UINT8,
                           DT_INT64, DT_DOUBLE, DT_BF16}))
    .OP_END_FACTORY_REG(Mod)
```

## Brief

Returns element-wise remainder of division. Support broadcasting operations.

## Inputs

Two inputs, including:
- x1: A ND tensor. Must be one of the following types: bfloat16, float16, float32,
int32, int64, int8, uint8, double.
- x2: A ND tensor of the same dtype as "x1".

## Outputs

y: A ND tensor. Has the same dtype as "x1". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32,int8,int32,uint8
- input1 x2: float16,float32,int8,int32,uint8
- output0 y: float16,float32,int8,int32,uint8
### AI CPU
- input0 x1: double,float16,float32,int8,int32,int64,uint8
- input1 x2: double,float16,float32,int8,int32,int64,uint8
- output0 y: double,float16,float32,int8,int32,int64,uint8

## Attention Constraints

- x2: The input data does not support 0.
- When NUM exceeds 2048 , the accuracy of operator cannot guarantee the
requirement of double thousandths in the mini form.
- Due to different architectures, the calculation results of this operator
on NPU and CPU may be inconsistent.
- If shape is expressed as (D1,D2... ,Dn),
then D1*D2... *DN<=1000000,n<=8. 

## Third-party framework compatibility

Compatible with the TensorFlow operator Mod.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
