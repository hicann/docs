# LookupTableExport

```c
REG_OP(LookupTableExport)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .OUTPUT(keys, TensorType({DT_INT32, DT_INT64, DT_STRING}))
    .OUTPUT(values, TensorType({DT_BOOL, DT_DOUBLE, DT_FLOAT, \
        DT_INT32, DT_INT64, DT_STRING}))
    .REQUIRED_ATTR(Tkeys, Type)
    .REQUIRED_ATTR(Tvalues, Type)
    .OP_END_FACTORY_REG(LookupTableExport)
```

## Brief

Outputs all keys and values in the table. 

## Inputs

The dtype of input handle must be resource. Inputs include:
handle: A Tensor of type resource. Handle to the table. 

## Outputs

- keys: A Tensor of type Tkeys.
- values: A Tensor of type Tvalues.

## Attributes

- Tkeys: A DType of keys.
- Tvalues: A DType of values.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- output0 keys: int32,int64,string
- output1 values: bool,double,float32,int32,int64,string

## Third-party framework compatibility.

Compatible with tensorflow LookupTableExport operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
