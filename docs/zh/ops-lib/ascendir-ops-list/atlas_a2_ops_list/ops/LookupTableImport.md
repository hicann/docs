# LookupTableImport

```c
REG_OP(LookupTableImport)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .INPUT(keys, TensorType({DT_STRING, DT_INT32, DT_INT64}))
    .INPUT(values, TensorType({DT_BOOL, DT_DOUBLE, \
        DT_FLOAT, DT_INT32, DT_INT64, DT_STRING}))
    .OP_END_FACTORY_REG(LookupTableImport)
```

## Brief

Replaces the contents of the table with the specified keys and values. 

## Inputs

The dtype of input handle must be resource. Inputs include:
- handle: A Tensor of type resource. Handle to the table.
- keys: A Tensor. Any shape. Keys to look up.
- values: A Tensor. Values to associate with keys.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- input1 keys: int32,int64,string
- input2 values: bool,double,float32,int32,int64,string

## Third-party framework compatibility.

Compatible with tensorflow LookupTableImport operator.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
