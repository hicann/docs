# Signbit

```c
REG_OP(Signbit)
.INPUT(x, TensorType::RealNumberType()).OUTPUT(y, TensorType({DT_BOOL})).OP_END_FACTORY_REG(Signbit)
```

## Brief

computes the sign bit of each input element. return true if x<0 or x=-0.0
aicore accuracy is not guaranteed.

## Inputs

x: A ND Tensor with TensorType::RealNumberType().

## Outputs

y: A ND tensor. Has the bool dtype. True means x<0 or x=-0.0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,double,float16,float32,int8,int32,int64,uint8,uint64
- output0 y: bool

## Third-party framework compatibility

Compatible with the TensorFlow operator Signbit.


---

[Back to Operator Specifications (Ascend950)](../README.md)
