# Fills

```c
REG_OP(Fills)
     .INPUT(x, TensorType({BasicType(), DT_BOOL}))
     .OUTPUT(y, TensorType({BasicType(), DT_BOOL}))
     .REQUIRED_ATTR(value, Float)
     .OP_END_FACTORY_REG(Fills)
```

## Brief

Fill tensor with value.

## Inputs

One input, including:
x: A ND tensor. Must be one of the following types:BasicType, bool.

## Outputs

y: A ND tensor. Has the same dtype and shape as "x". 

## Attributes

value: A scale. Must be float. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32,int8,int32,int64,uint8
- output0 y: float16,float32,int8,int32,int64,uint8
### AI CPU
- input0 x: bool,double,float16,float32,int8,int16,int32,int64,uint8
- output0 y: bool,double,float16,float32,int8,int16,int32,int64,uint8

## Attention Constraints

For parameters of the float32 type, there is no precision loss. For INT32 and INT64 parameters,
precision loss occurs when the parameter value exceeds 2^24. it is recommended to use Fill.

## Third-party framework compatibility

Compatible with the PyTorch operator fills.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
