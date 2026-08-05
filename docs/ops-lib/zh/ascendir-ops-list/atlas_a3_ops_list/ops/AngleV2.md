# AngleV2

```c
REG_OP(AngleV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_COMPLEX64, DT_BOOL, DT_UINT8,
                          DT_INT8, DT_INT16, DT_INT32, DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OP_END_FACTORY_REG(AngleV2)
```

## Brief

Computes the element_wise angle(in radians) of the given input tensor.

## Inputs

x: A ND tensor of type float16, float, complex64, bool, uint8, int8, int16, int32, int64. 

## Outputs

y: A ND tensor of type float16, float32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool,complex64,float16,float32,int8,int16,int32,int64,uint8
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator Angle. 


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
