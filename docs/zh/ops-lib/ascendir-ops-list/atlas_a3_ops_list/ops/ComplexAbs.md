# ComplexAbs

```c
REG_OP(ComplexAbs)
    .INPUT(x, TensorType({DT_COMPLEX32, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .ATTR(Tout, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(ComplexAbs)
```

## Brief

Computes the complex absolute value of a tensor.

## Inputs

x: x of complex numbers, this operation returns a tensor of type
float or double that is the absolute value of each element in x .
A Tensor of type complex32, complex64, complex128.

## Outputs

y:A tensor of type `float` or `double` that is the absolute value of each element in `x`.
A Tensor of type float16(when x is complex32), float32(when x is complex64), double(when x is complex128).

## Attributes

Tout: a Type attr, representing the type of output, donot use. default is DT_FLOAT

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: complex32,complex64
- output0 y: float16,float32
### AI CPU
- input0 x: complex64,complex128
- output0 y: double,float32

## Third-party framework compatibility.

Compatible with tensorflow ComplexAbs operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
