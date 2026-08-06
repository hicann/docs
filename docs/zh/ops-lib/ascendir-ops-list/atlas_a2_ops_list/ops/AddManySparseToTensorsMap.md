# AddManySparseToTensorsMap

```c
REG_OP(AddManySparseToTensorsMap)
    .INPUT(indices, TensorType({DT_INT64}))
    .INPUT(values, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, \
        DT_INT32, DT_INT64, DT_BOOL, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, \
        DT_COMPLEX64, DT_COMPLEX128, DT_RESOURCE, DT_STRING}))
    .INPUT(shape, TensorType({DT_INT64}))
    .OUTPUT(handles, TensorType({DT_INT64}))
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .OP_END_FACTORY_REG(AddManySparseToTensorsMap)
```

## Brief

Generates sparse cross from a list of sparse and dense tensors. 

## Inputs

3 inputs, including:
- indices: A 2D tensor of type int64.
The "indices" of the minibatch SparseTensor.
- values: A 1D tensor. The "values" of the minibatch SparseTensor.
- shape: A 1D tensor of type int64. The "shape" of the minibatch SparseTensor.

## Outputs

handles: A tensor of type int64. 

## Attributes

- container: An optional string. Defaults to "".
The container name for the "SparseTensorsMap" created by this op.
- shared_name: An optional string. Defaults to "".
The shared name for the "SparseTensorsMap" created by this op. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 indices: int64
- input1 values: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,resource,string,uint8,uint16
- input2 shape: int64
- output0 handles: int64

## Third-party framework compatibility

Compatible with the TensorFlow operator AddManySparseToTensorsMap.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
