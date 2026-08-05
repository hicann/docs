# SparseSoftmax

```c
REG_OP(SparseSoftmax)
    .INPUT(indices, TensorType({DT_INT64}))
    .INPUT(values, TensorType({DT_FLOAT, DT_DOUBLE}))
    .INPUT(shape, TensorType({DT_INT64}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_DOUBLE}))
    .OP_END_FACTORY_REG(SparseSoftmax)
```

## Brief

Applies softmax to a batched ND SparseTensor. 

## Inputs

The input must be a batched ND SparseTensor.
- indices: A matrix tensor of type int64. 2D. The indices of the SparseTensor.
- values: A vector tensor of type float or double. 1D. The values of the SparseTensor.
- shape: A vector tensor of type int64. 1D. The shape of the SparseTensor.

## Outputs

y: A vector tensor. 1D. Has the same type as "values". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 indices: int64
- input1 values: double,float32
- input2 shape: int64
- output0 y: double,float32

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseSoftmax.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
