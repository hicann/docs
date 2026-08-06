# SparseTensorDenseMatMul

```c
REG_OP(SparseTensorDenseMatMul)
    .INPUT(x1_indices, TensorType({DT_INT32, DT_INT64}))
    .INPUT(x1_values, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT32, DT_COMPLEX64, DT_COMPLEX128, DT_FLOAT16, DT_INT64}))
    .INPUT(x1_shape, TensorType({DT_INT64}))
    .INPUT(x2, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT64, DT_INT32, DT_COMPLEX64, DT_COMPLEX128, DT_FLOAT16}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE, DT_INT64, DT_INT32, DT_COMPLEX64, DT_COMPLEX128, DT_FLOAT16}))
    .ATTR(adjoint_a, Bool, false)
    .ATTR(adjoint_b, Bool, false)
    .OP_END_FACTORY_REG(SparseTensorDenseMatMul)
```

## Brief

Multiplies SparseTensor A (of rank 2) by dense matrix B.

## Inputs

- x1_indices: A 2D tensor of type int32 or int64.
The indices of the matrix "SparseTensor", with size [nnz, 2].
- x1_values: A 1D tensor. The values of the SparseTensor, with size [nnz].
- x1_shape: A 1D tensor of type int64. The shape of the SparseTensor, with size [2].
- x2: A dense matrix tensor of the same type as "x1_values". 2D.

## Outputs

y: A "tensor". Has the same type as "x1_values". 

## Attributes

- adjoint_a: An optional bool. Defaults to "False".Use the adjoint of A in the matrix multiply.
If A is complex, this is transpose(conj(A)). Otherwise it is transpose(A).
- adjoint_b: An optional bool. Defaults to "False".Use the adjoint of B in the matrix multiply.
If B is complex, this is transpose(conj(B)). Otherwise it is transpose(B). 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x1_indices: int32,int64
- input1 x1_values: complex64,complex128,double,float16,float32,int32
- input2 x1_shape: int64
- input3 x2: complex64,complex128,double,float16,float32,int32
- output0 y: complex64,complex128,double,float16,float32,int32

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseTensorDenseMatMul.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
