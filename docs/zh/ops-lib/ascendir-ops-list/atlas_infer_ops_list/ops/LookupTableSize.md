# LookupTableSize

```c
REG_OP(LookupTableSize)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .OUTPUT(size, TensorType({DT_INT64}))
    .OP_END_FACTORY_REG(LookupTableSize)
```

## Brief

Computes the number of elements in the given table. 

## Inputs

The dtype of input handle must be resource. Inputs include:
handle: A Tensor of type resource. Handle to the table. 

## Outputs

size: A Tensor of type int64. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- output0 size: int64

## Third-party framework compatibility.

Compatible with tensorflow LookupTableSize operator.


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
