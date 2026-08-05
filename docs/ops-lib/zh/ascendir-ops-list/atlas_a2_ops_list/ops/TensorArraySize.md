# TensorArraySize

```c
REG_OP(TensorArraySize)
    .INPUT(handle, TensorType({ DT_RESOURCE }))
    .INPUT(flow_in, TensorType({ DT_FLOAT }))
    .OUTPUT(size, TensorType({ DT_INT32 }))
    .OP_END_FACTORY_REG(TensorArraySize)
```

## Brief

Return the number of elements in a TensorArray. 

## Inputs

The input handle must be type resource. Inputs include:
- handle: The handle to a TensorArray.
- flow_in: A float scalar that enforces proper chaining of operations.

## Outputs

size: The number of elements in a TensorArray.. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- input1 flow_in: float32
- output0 size: int32

## Third-party framework compatibility

Compatible with tensorflow TensorArraySize operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
