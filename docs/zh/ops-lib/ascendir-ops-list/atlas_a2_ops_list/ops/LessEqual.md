# LessEqual

```c
REG_OP(LessEqual)
    .INPUT(x1, TensorType::RealNumberType())
    .INPUT(x2, TensorType::RealNumberType())
    .OUTPUT(y, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(LessEqual)
```

## Brief

Returns the truth value of (x1 <= x2) element-wise. Support broadcasting operations. 
When input is int32 and (x2 - x1) > 2^31 or < -2^31,
aicore accuracy is not guaranteed.

## Inputs

Two inputs, including:
- x1: A ND Tensor with TensorType::RealNumberType().
- x2: A ND Tensor to be compared to "x1", and the data type is the same as "x1".

## Outputs

y: A ND Tensor. Has the bool dtype. True means x1 <= x2, false means x1 > x2.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,float16,float32,int8,int32,int64,uint8
- input1 x2: bfloat16,float16,float32,int8,int32,int64,uint8
- output0 y: bool
### AI CPU
- input0 x1: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 x2: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bool

## Third-party framework compatibility

Compatible with the TensorFlow operator LessEqual.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
