# TensorArrayRead

```c
REG_OP(TensorArrayRead)
    .INPUT(handle, TensorType({ DT_RESOURCE }))
    .INPUT(index, TensorType({ DT_INT32 }))
    .INPUT(flow_in, TensorType({ DT_FLOAT }))
    .OUTPUT(y, TensorType({ DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16,
        DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, DT_DOUBLE,
        DT_STRING, DT_COMPLEX64, DT_COMPLEX128}))
    .REQUIRED_ATTR(dtype, Type)
    .OP_END_FACTORY_REG(TensorArrayRead)
```

## Brief

Read an element from the TensorArray into output value. 

## Inputs

The input handle must be type resource. Inputs include:
- handle: A Tensor of type resource. The handle to a TensorArray.
- index: A Tensor of type int32.
- flow_in: A Tensor of type float.

## Outputs

y: A Tensor of type dtype. 

## Attributes

dtype: A DType. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- input1 index: int32
- input2 flow_in: float32
- output0 y: bool,complex64,complex128,double,float16,float32,int8,int16,int32,int64,string,uint8,uint16

## Third-party framework compatibility

Compatible with tensorflow TensorArrayRead operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
