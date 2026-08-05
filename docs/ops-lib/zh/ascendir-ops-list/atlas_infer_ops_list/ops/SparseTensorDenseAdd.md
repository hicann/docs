# SparseTensorDenseAdd

```c
REG_OP(SparseTensorDenseAdd)
    .INPUT(x1_indices, TensorType({DT_INT32, DT_INT64}))
    .INPUT(x1_values, TensorType({DT_INT64, DT_INT32, DT_UINT16, DT_INT16, DT_UINT8, DT_INT8, \
        DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .INPUT(x1_shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(x2, TensorType({DT_INT64, DT_INT32, DT_UINT16, DT_INT16, DT_UINT8, DT_INT8, \
        DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OUTPUT(y, TensorType({DT_INT64, DT_INT32, DT_UINT16, DT_INT16, DT_UINT8, DT_INT8, \
        DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_COMPLEX64, DT_COMPLEX128}))
    .OP_END_FACTORY_REG(SparseTensorDenseAdd)
```

## Brief

Adds up a SparseTensor and a dense tensor, producing a dense tensor. 

## Inputs

Inputs "x1_*" must be SparseTensors and "x2" must be a dense tensor.
- x1_indices: A matrix tensor of type int32 or int64. 2D. The indices of the SparseTensor.
- x1_values: The values of the SparseTensor. A vector tensor. 1D.
- x1_shape: A vector tensor of type int32 or int64. 1D. The shape of the SparseTensor.
- x2: A matrix tensor. Has the same type and same shape as the x1_values.

## Outputs

y: A matrix tensor. Has the same type and same shape as "x2". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x1_indices: int32,int64
- input1 x1_values: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- input2 x1_shape: int32,int64
- input3 x2: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output0 y: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseTensorDenseAdd.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
