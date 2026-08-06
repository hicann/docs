# TensorArraySplit

```c
REG_OP(TensorArraySplit)
    .INPUT(handle, TensorType({ DT_RESOURCE }))
    .INPUT(value, TensorType({ DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16,
        DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, DT_DOUBLE,
        DT_STRING, DT_COMPLEX64, DT_COMPLEX128 }))
    .INPUT(lengths, TensorType({ DT_INT64 }))
    .INPUT(flow_in, TensorType({ DT_FLOAT }))
    .OUTPUT(flow_out, TensorType({ DT_FLOAT }))
    .OP_END_FACTORY_REG(TensorArraySplit)
```

## Brief

Split the data from the input value into TensorArray elements. 

## Inputs

The input handle must be type resource. Inputs include:
- handle: The handle to a TensorArray.
- value: The concatenated tensor to write to the TensorArray.
- lengths: The vector of lengths, how to split the rows of value into
the TensorArray.
- flow_in: A float scalar that enforces proper chaining of operations.

## Outputs

flow_out: A float scalar that enforces proper chaining of operations. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- input1 value: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,string,uint8,uint16
- input2 lengths: int64
- input3 flow_in: float32
- output0 flow_out: float32

## Third-party framework compatibility

Compatible with tensorflow TensorArraySplit operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
