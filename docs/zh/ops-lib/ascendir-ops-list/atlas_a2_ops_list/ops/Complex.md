# Complex

```c
REG_OP(Complex)
    .INPUT(real, "T")
    .INPUT(imag, "T")
    .OUTPUT(out, "Tout")
    .ATTR(Tout, Int, DT_COMPLEX64)
    .DATATYPE(T, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .DATATYPE(Tout, TensorType({DT_COMPLEX32, DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(Complex)
```

## Brief

get complex.

## Inputs

- real: An ND tensor of type  float16,float32,double, representing the real part of a complex number.
- imag: An ND tensor of type  float16,float32,double, representing the imaginary part of a complex number.

## Outputs

out: An ND tensor of type complex32, complex64, complex128 

## Attributes

Tout: representing the output of type.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 real: float16,float32
- input1 imag: float16,float32
- output0 out: complex32,complex64
### AI CPU
- input0 real: double,float32
- input1 imag: double,float32
- output0 out: complex64,complex128


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
