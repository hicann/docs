# Relu6

```c
REG_OP(Relu6)
    .INPUT(x, TensorType::RealNumberType())
    .OUTPUT(y, TensorType::RealNumberType())
    .OP_END_FACTORY_REG(Relu6)
```

## Brief

Computes rectified linear 6.
activations = min(max(x, 0), 6) .

## Inputs

x: A ND Tensor of type RealNumberType(includes: double, float32, float16,
int16, int32, int64, int8, uint16, uint32, uint64, uint8, bfloat16) . 

## Outputs

y: A ND Tensor with the same type as x . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32,int32
- output0 y: bfloat16,float16,float32,int32
### AI CPU
- input0 x: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Third-party framework compatibility

Compatible with the TensorFlow operator Relu6.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
