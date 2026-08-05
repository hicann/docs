# FillDiagonal

```c
REG_OP(FillDiagonal)
    .INPUT(x, TensorType({BasicType(), DT_BOOL, DT_BF16}))
    .OUTPUT(y, TensorType({BasicType(), DT_BOOL, DT_BF16}))
    .REQUIRED_ATTR(fill_value, Float)
    .ATTR(wrap, Bool, false)
    .OP_END_FACTORY_REG(FillDiagonal)
```

## Brief

Fill diagonal of at least 2 dimension tensors with value . 

## Inputs

x: A Tensor. Must be one of the following types:float16, float32, float64, int8,
int16, int32, int64, uint8, bool, bfloat16. 

## Outputs

y: A Tensor. Has the same type as "x" . 

## Attributes

fill_value:The value to fill in
wrap: An optional bool. Defaults to "False". If "True", Use recursive fill. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8
- output0 y: bfloat16,bool,double,float16,float32,int8,int16,int32,int64,uint8

## Third-party framework compatibility

Compatible with the Pytorch operator FillDiagonal.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
