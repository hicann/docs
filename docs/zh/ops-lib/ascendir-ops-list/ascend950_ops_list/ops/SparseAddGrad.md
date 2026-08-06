# SparseAddGrad

```c
REG_OP(SparseAddGrad)
    .INPUT(backprop_val_grad, TensorType({DT_INT8, DT_INT16, DT_INT32,
                  DT_INT64, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(x1_indices, TensorType({DT_INT64}))
    .INPUT(x2_indices, TensorType({DT_INT64}))
    .INPUT(sum_indices, TensorType({DT_INT64}))
    .OUTPUT(x1_val_grad, TensorType({DT_INT8, DT_INT16, DT_INT32,
                  DT_INT64, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(x2_val_grad, TensorType({DT_INT8, DT_INT16, DT_INT32,
                  DT_INT64, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(SparseAddGrad)
```

## Brief

The gradient operator for the SparseAdd op. 

## Inputs

- backprop_val_grad: A 1D tensor with shape [nnz(sum)]. The gradient with respect to the non-empty values of the sum.
- x1_indices: A 2D tensor of type int64. The indices of the SparseTensor A, with size [nnz(A), ndims].
- x2_indices: A 2D tensor of type int64. The indices of the SparseTensor B, with size [nnz(B), ndims].
- sum_indices: A 2D tensor of type int64. The indices of the sum SparseTensor, with size [nnz(sum), ndims].

## Outputs

- x1_val_grad: A tensor. Has the same type as "backprop_val_grad".
- x2_val_grad: A tensor. Has the same type as "backprop_val_grad".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 backprop_val_grad: complex64,complex128,double,float32,int8,int16,int32,int64
- input1 x1_indices: int64
- input2 x2_indices: int64
- input3 sum_indices: int64
- output0 x1_val_grad: complex64,complex128,double,float32,int8,int16,int32,int64
- output1 x2_val_grad: complex64,complex128,double,float32,int8,int16,int32,int64

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseAddGrad.


---

[Back to Operator Specifications (Ascend950)](../README.md)
