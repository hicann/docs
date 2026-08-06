# SparseFillEmptyRowsGrad

```c
REG_OP(SparseFillEmptyRowsGrad)
    .INPUT(reverse_index_map, TensorType({DT_INT64}))
    .INPUT(grad_values, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, \
        DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, \
        DT_COMPLEX64, DT_COMPLEX128, DT_RESOURCE, DT_STRING}))
    .OUTPUT(y_value, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, \
        DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, \
        DT_COMPLEX64, DT_COMPLEX128, DT_RESOURCE, DT_STRING}))
    .OUTPUT(y_default_value, TensorType({DT_INT8, DT_UINT8, DT_INT16, \
        DT_UINT16, DT_INT32, DT_INT64, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, \
        DT_COMPLEX64, DT_COMPLEX128, DT_RESOURCE, DT_STRING}))
    .OP_END_FACTORY_REG(SparseFillEmptyRowsGrad)
```

## Brief

The gradient of SparseFillEmptyRows. 

## Inputs

- reverse_index_map: A 1D tensor of type int64. The reverse index map from SparseFillEmptyRows.
- grad_values: A 1D tensor. The gradients from backprop.

## Outputs

- y_value: A tensor. Has the same type as "grad_values".
- y_default_value: A tensor. Has the same type as "grad_values".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 reverse_index_map: int64
- input1 grad_values: complex64,complex128,double,float16,float32,int8,int16,int32,int64,resource,string,uint8,uint16
- output0 y_value: complex64,complex128,double,float16,float32,int8,int16,int32,int64,resource,string,uint8,uint16
- output1 y_default_value: complex64,complex128,double,float16,float32,int8,int16,int32,int64,resource,string,uint8,uint16

## Third-party framework compatibility

Compatible with the TensorFlow operator SparseFillEmptyRowsGrad.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
