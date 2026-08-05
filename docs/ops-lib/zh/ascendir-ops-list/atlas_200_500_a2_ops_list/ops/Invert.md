# Invert

```c
REG_OP(Invert)
    .INPUT(x, TensorType::IntegerDataType())
    .OUTPUT(y, TensorType::IntegerDataType())
    .OP_END_FACTORY_REG(Invert)
```

## Brief

Reverses specific dimensions of a tensor.

## Inputs

One input: 
x: A ND Tensor, Must be one of the following types:
int32, uint8, int16, int8, int64, uint16, uint32, uint64,
and format can be [NCHW,NHWC,ND]. 

## Outputs

y: A ND Tensor. Has the same dtype and format as "x". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: int16,uint16
- output0 y: int16,uint16
### AI CPU
- input0 x: int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator Invert.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
