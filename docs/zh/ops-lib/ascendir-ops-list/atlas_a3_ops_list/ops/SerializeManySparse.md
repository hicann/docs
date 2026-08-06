# SerializeManySparse

```c
REG_OP(SerializeManySparse)
    .INPUT(indices, TensorType({DT_INT64}))
    .INPUT(values, TensorType({DT_BOOL, DT_INT8, DT_UINT8, DT_INT16, \
        DT_UINT16, DT_INT32, DT_INT64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16, \
        DT_COMPLEX64, DT_COMPLEX128, DT_RESOURCE, DT_STRING}))
    .INPUT(shape, TensorType({DT_INT64}))
    .OUTPUT(serialized_sparse, TensorType({DT_STRING, DT_VARIANT}))
    .ATTR(out_type, Type, DT_STRING)
    .OP_END_FACTORY_REG(SerializeManySparse)
```

## Brief

Serializes an "N"-minibatch SparseTensor into an [N, 3] tensor object. 

## Inputs

3 inputs, including:
- indices: A 2D tensor of type int64. The "indices" of the minibatch SparseTensor.
- values: A 1D tensor. The "values" of the minibatch SparseTensor.
- shape: A 1D tensor of type int64. The "shape" of the minibatch SparseTensor.

## Outputs

serialized_sparse: A tensor of type "out_type". 

## Attributes

out_type: An optional type. Defaults to "string". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 indices: int64
- input1 values: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,resource,string,uint8,uint16
- input2 shape: int64
- output0 serialized_sparse: string,variant

## Third-party framework compatibility

Compatible with the TensorFlow operator SerializeManySparse.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
