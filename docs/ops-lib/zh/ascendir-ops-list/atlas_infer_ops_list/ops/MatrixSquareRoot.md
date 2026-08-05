# MatrixSquareRoot

```c
REG_OP(MatrixSquareRoot)
    .INPUT(input, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(MatrixSquareRoot)
```

## Brief

Computes the matrix square root of one or more square matrices . 

## Inputs

input: Shape is `[..., M, M]` . 

## Outputs

y: Shape is `[..., M, M]` . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: complex64,complex128,double,float32
- output0 y: complex64,complex128,double,float32

## Third-party framework compatibility

Compatible with TensorFlow MatrixSquareRoot operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
