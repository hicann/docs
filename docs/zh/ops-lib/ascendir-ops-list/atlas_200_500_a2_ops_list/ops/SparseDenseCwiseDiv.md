# SparseDenseCwiseDiv

```c
REG_OP(SparseDenseCwiseDiv)
    .INPUT(x1_indices, TensorType({DT_INT64}))
    .INPUT(x1_values, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, \
                                  DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, \
                                  DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(x1_shape, TensorType({DT_INT64}))
    .INPUT(x2, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, \
                          DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, \
                          DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, \
                           DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, \
                           DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(SparseDenseCwiseDiv)
```

## Brief

Divides a SparseTensor by a dense tensor. 

## Inputs

- x1_indices: A matrix tensor of type int64. 2D. The indices of the SparseTensor.
- x1_values: The values of the SparseTensor. A vector tensor. 1D.
- x1_shape: A 1D tensor of type int64. The requested new dense shape.
- x2: A dense tensor of the same type as "x1_values".

## Outputs

y: A tensor. Has the same type as "x1_values". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x1_indices: int64
- input1 x1_values: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input2 x1_shape: int64
- input3 x2: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseDenseCwiseDiv.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
