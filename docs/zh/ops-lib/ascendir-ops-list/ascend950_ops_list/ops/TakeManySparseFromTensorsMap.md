# TakeManySparseFromTensorsMap

```c
REG_OP(TakeManySparseFromTensorsMap)
    .INPUT(handles, TensorType({DT_INT64}))
    .OUTPUT(indices, TensorType({DT_INT64}))
    .OUTPUT(values, TensorType({DT_BOOL, DT_INT8, DT_UINT8, DT_INT16, \
        DT_UINT16, DT_INT32, DT_INT64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(shape, TensorType({DT_INT64}))
    .REQUIRED_ATTR(dtype, Type)
    .ATTR(container, String, "")
    .ATTR(shared_name, String, "")
    .OP_END_FACTORY_REG(TakeManySparseFromTensorsMap)
```

## Brief

Reads SparseTensors from a "SparseTensorsMap" and concatenate them. 

## Inputs

handles: A 1D tensor of type int64.
The "N" serialized SparseTensor objects. 

## Outputs

- indices: A tensor of type int64.2-D. The `indices` of the minibatch `SparseTensor`.
- values: A tensor of type "dtype". 1-D. The `values` of the minibatch `SparseTensor`.
- shape: A tensor of type int64 . 1-D. The `shape` of the minibatch `SparseTensor`.

## Attributes

- dtype: A tf.DType. The "dtype" of the SparseTensor objects stored in the "SparseTensorsMap".
- container: An optional string. Defaults to "".
The container name for the "SparseTensorsMap" read by this op.
- shared_name: An optional string. Defaults to "".
The shared name for the "SparseTensorsMap" read by this op. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handles: int64
- output0 indices: int64
- output1 values: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16
- output2 shape: int64

## Third-party framework compatibility

Compatible with the TensorFlow operator TakeManySparseFromTensorsMap.


---

[Back to Operator Specifications (Ascend950)](../README.md)
