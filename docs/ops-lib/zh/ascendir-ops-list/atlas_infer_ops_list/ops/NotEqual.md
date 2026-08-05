# NotEqual

```c
REG_OP(NotEqual)
    .INPUT(x1, TensorType::RealNumberType())
    .INPUT(x2, TensorType::RealNumberType())
    .OUTPUT(y, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(NotEqual)
```

## Brief

Returns the truth value of (x1 != x2) element-wise. Support broadcasting operations.

## Inputs

Two inputs, including:
- x1: A ND Tensor with TensorType::RealNumberType().
- x2: A ND Tensor to be compared to "x1", and the data type is the same as "x1".

## Outputs

y: A ND Tensor. Has the bool dtype. True means x1 != x2, false means x1 == x2.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bool,float16,float32,int8,int32,int64,uint8,uint64
- input1 x2: bool,float16,float32,int8,int32,int64,uint8,uint64
- output0 y: bool
### AI CPU
- input0 x1: bool,double,float16,float32,int8,int16,int32,int64,uint8
- input1 x2: bool,double,float16,float32,int8,int16,int32,int64,uint8
- output0 y: bool

## Third-party framework compatibility

Compatible with the TensorFlow operator NotEqual.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
