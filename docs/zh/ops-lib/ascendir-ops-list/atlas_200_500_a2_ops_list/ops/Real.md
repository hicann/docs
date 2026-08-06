# Real

```c
REG_OP(Real)
    .INPUT(input, "TSrc")
    .OUTPUT(output, "Tout")
    .ATTR(Tout, Int, DT_FLOAT)
    .DATATYPE(TSrc, TensorType({DT_FLOAT16, DT_FLOAT, DT_COMPLEX32, DT_COMPLEX64, DT_COMPLEX128}))
    .DATATYPE(Tout, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(Real)
```

## Brief

Returns the real part of a complex number.
If the input is already real, it will be returned unchanged.

## Inputs

input:A ND Tensor of type float16, float32, complex32, complex64, complex128.

## Outputs

output:A ND Tensor of type float16, float32, double. Has the same shape as input.

## Attributes

Tout: A optional type attr, mean the output dtype for outputs. Defaults to DT_FLOAT(float32). 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: complex64,complex128
- output0 output: double,float32

## Third-party framework compatibility.

Compatible with tensorflow Real operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
