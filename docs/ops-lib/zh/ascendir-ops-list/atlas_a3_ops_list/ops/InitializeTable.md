# InitializeTable

```c
REG_OP(InitializeTable)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .INPUT(keys, TensorType({DT_INT32, DT_INT64, DT_STRING}))
    .INPUT(values, TensorType({DT_INT32, DT_INT64, DT_FLOAT, \
        DT_DOUBLE, DT_BOOL, DT_STRING}))
    .OP_END_FACTORY_REG(InitializeTable)
```

## Brief

Table initializer that takes two tensors for keys and values
respectively. 

## Inputs

The dtype of input handle must be resource. Inputs include:
- handle: A Tensor of type resource. Handle to a table which will be
initialized.
- keys: A Tensor. Keys of type Tkey.
- values: A Tensor. Values of type Tval.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- input1 keys: int32,int64,string
- input2 values: bool,double,float32,int32,int64,string

## Third-party framework compatibility.

Compatible with tensorflow InitializeTable operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
