# Lu

```c
REG_OP(Lu)
    .INPUT(input, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(lu, TensorType({DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(p, TensorType({DT_INT32, DT_INT64}))
    .REQUIRED_ATTR(output_idx_type, Type)
    .OP_END_FACTORY_REG(Lu)
```

## Brief

Computes the LU decomposition of one or more square matrices . 

## Inputs

input: A tensor of shape `[..., M, M]` whose inner-most 2 dimensions form
matrices of size `[M, M]` . 

## Outputs

- lu: A tensor of shape `[..., M, M]` whose strictly lower triangular part
denotes the lower triangular factor `L` with unit diagonal.
- p: upper triangular part denotes the upper triangular factor `U`.Permutation
of the rows encoded as a list of indices in `0..M-1`. Shape is `[..., M]` . 

## Attributes

output_idx_type: DType from: int32, int64.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 input: complex64,complex128,double,float32
- output0 lu: complex64,complex128,double,float32
- output1 p: int32,int64

## Third-party framework compatibility

Compatible with TensorFlow Lu operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
