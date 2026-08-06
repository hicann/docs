# FillDiagonalV2

```c
REG_OP(FillDiagonalV2)
    .INPUT(x, TensorType({BasicType(), DT_BOOL, DT_BF16}))
    .INPUT(fill_value, TensorType({BasicType(), DT_BOOL, DT_BF16}))
    .OUTPUT(x, TensorType({BasicType(), DT_BOOL, DT_BF16}))
    .ATTR(wrap, Bool, false)
    .OP_END_FACTORY_REG(FillDiagonalV2)
```

## Brief

Fill diagonal of at least 2 dimension tensors with value inplace. 

## Inputs

- x: A tensor. Must be one of the following types:float16, float32, float64, int8,
int16, int32, int64, uint8, bool, bfloat16. 
- fill_value: A tensor. Scalar value to be filled, Must have the same type as "x".

## Outputs

x: A tensor. Refers to the same tensor as input "x". 

## Attributes

wrap: An optional bool. Defaults to "False". If "True", use recursive fill. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8
- input1 fill_value: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8
- output0 x: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8

## Third-party framework compatibility

Compatible with the Pytorch operator FillDiagonal.


---

[Back to Operator Specifications (Ascend950)](../README.md)
