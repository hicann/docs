# Atan

```c
REG_OP(Atan)
    .INPUT(x, TensorType::UnaryDataType())
    .OUTPUT(y, TensorType::UnaryDataType())
    .OP_END_FACTORY_REG(Atan)
```

## Brief

Computes the trignometric inverse tangent of x element-wise.
The atan operation returns the inverse of tan, such that if y = tan(x) then, x = atan(y).

## Inputs

x: An ND or 5HD tensor. support 1D ~ 8D. Must be one of the following types:
int8, int16, int32, int64, uint8, bool, float32, float16, float64, bfloat16.

## Outputs

y: A tensor. Must be one of the following types: float32, float16, float64, bfloat16.
The output of atan will lie within the invertible range of tan, i.e (-pi/2, pi/2).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 x: double,float16,float32
- output0 y: double,float16,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator Atan.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
