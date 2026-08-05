# SparseSliceGrad

```c
REG_OP(SparseSliceGrad)
    .INPUT(backprop_val_grad, TensorType({ DT_INT8, DT_UINT8, DT_INT16,
        DT_UINT16, DT_INT32, DT_INT64, DT_FLOAT, DT_FLOAT16, DT_DOUBLE,
        DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(indices, TensorType({DT_INT64}))
    .INPUT(start, TensorType({DT_INT64}))
    .INPUT(new_indices, TensorType({DT_INT64}))
    .OUTPUT(y_grad, TensorType({ DT_INT8, DT_UINT8, DT_INT16,
        DT_UINT16, DT_INT32, DT_INT64, DT_FLOAT, DT_FLOAT16, DT_DOUBLE,
        DT_COMPLEX64, DT_COMPLEX128 }))
    .OP_END_FACTORY_REG(SparseSliceGrad)
```

## Brief

The gradient operator for the SparseSlice op. 

## Inputs

- backprop_val_grad: A tensor. Must be one of the following types: int8, uint8, int16, uint16,
int32, int64, float16, float, double, complex64, complex128.
- indices: A matrix tensor of type int64. 2D. The indices of the SparseTensor.
- start: A 1D tensor of type int64. The start of the slice.
- new_indices: A matrix tensor of type int64. 2D. The indices of the sliced SparseTensor.

## Outputs

y_grad: A tensor. Must be one of the following types: int8, uint8, int16, uint16, int32,
int64, float16, float, double, complex64, complex128. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 backprop_val_grad: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input1 indices: int64
- input2 start: int64
- input3 new_indices: int64
- output0 y_grad: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseSliceGrad.


---

[Back to Operator Specifications (Ascend950)](../README.md)
