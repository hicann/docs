# TensorArrayScatter

```c
REG_OP(TensorArrayScatter)
    .INPUT(handle, TensorType({ DT_RESOURCE }))
    .INPUT(indices, TensorType({ DT_INT32 }))
    .INPUT(value, TensorType({ DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16,
        DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, DT_DOUBLE,
        DT_STRING, DT_COMPLEX64, DT_COMPLEX128 }))
    .INPUT(flow_in, TensorType({ DT_FLOAT }))
    .OUTPUT(flow_out, TensorType({ DT_FLOAT }))
    .OP_END_FACTORY_REG(TensorArrayScatter)
```

## Brief

Scatter the data from the input value into specific TensorArray
elements. 

## Inputs

The input handle must be type resource. Inputs include:
- handle: The handle to a TensorArray.
- indices: The locations at which to write the tensor elements.
- value: The concatenated tensor to write to the TensorArray.
- flow_in: A float scalar that enforces proper chaining of operations.

## Outputs

flow_out: A float scalar that enforces proper chaining of operations. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- input1 indices: int32
- input2 value: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,string,uint8,uint16
- input3 flow_in: float32
- output0 flow_out: float32

## Third-party framework compatibility

Compatible with tensorflow TensorArrayScatter operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
