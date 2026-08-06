# DeserializeManySparse

```c
REG_OP(DeserializeManySparse)
    .INPUT(serialized_sparse, TensorType({DT_STRING}))
    .OUTPUT(indices, TensorType({DT_INT64}))
    .OUTPUT(values, TensorType({DT_BOOL, DT_INT8, DT_UINT8, DT_INT16, \
        DT_UINT16, DT_INT32, DT_INT64, DT_DOUBLE, DT_FLOAT, DT_FLOAT16, \
        DT_COMPLEX64, DT_COMPLEX128, DT_RESOURCE, DT_STRING}))
    .OUTPUT(shape, TensorType({DT_INT64}))
    .REQUIRED_ATTR(dtype, Type)
    .OP_END_FACTORY_REG(DeserializeManySparse)
```

## Brief

Deserializes and concatenates SparseTensors from a serialized minibatch. 

## Inputs

One inputs, including:
serialized_sparse: A 2D tensor of type string.
The "N" serialized SparseTensor objects. Must have 3 columns. 

## Outputs

- indices: A tensor of type int64.
- values: A tensor of type "dtype".
- shape: A tensor of type int64 .

## Attributes

dtype: The type of the serialized SparseTensor objects. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 serialized_sparse: string
- output0 indices: int64
- output1 values: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,resource,string,uint8,uint16
- output2 shape: int64

## Third-party framework compatibility

Compatible with the TensorFlow operator DeserializeManySparse.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
