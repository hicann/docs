# PopulationCount

```c
REG_OP(PopulationCount)
  .INPUT(x, TensorType::IntegerDataType())
  .OUTPUT(y, TensorType({DT_UINT8}))
  .OP_END_FACTORY_REG(PopulationCount)
```

## Brief

Computes element-wise population count.

## Inputs

x: A ND Tensor, Must be one of the following types:
int32, uint8, int16, int8, int64, uint16, uint32, uint64. 

## Outputs

y: A ND Tensor of type uint8. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: int16,uint16
- output0 y: uint8
### AI CPU
- input0 x: int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: uint8

## Third-party framework compatibility

Compatible with the TensorFlow operator PopulationCount.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
