# AddSparseToTensorsMap

```c
REG_OP(AddSparseToTensorsMap)
    .INPUT(indices, TensorType({DT_INT64}))
    .INPUT(values, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, \
        DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, DT_DOUBLE, \
        DT_COMPLEX64, DT_COMPLEX128, DT_RESOURCE, DT_STRING}))
    .INPUT(shape, TensorType({DT_INT64}))
    .OUTPUT(handle, TensorType({DT_INT64}))
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .OP_END_FACTORY_REG(AddSparseToTensorsMap)
```

## Brief

Adds a SparseTensor to a SparseTensorsMap. 

## Inputs

The input tensor must be a SparseTensor.
- indices: A matrix tensor of type int64. 2D. The indices of the SparseTensor.
- values: The values of the SparseTensor. A vector tensor. 1D.
- shape: A 1D tensor of type int64. The requested new dense shape.

## Outputs

handle: A tensor of type int64. 

## Attributes

- container: An optional string. Defaults to " ".
- shared_name: An optional string. Defaults to " ".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 indices: int64
- input1 values: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,resource,string,uint8,uint16
- input2 shape: int64
- output0 handle: int64

## Third-party framework compatibility

Compatible with the TensorFlow operator AddSparseToTensorsMap.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
