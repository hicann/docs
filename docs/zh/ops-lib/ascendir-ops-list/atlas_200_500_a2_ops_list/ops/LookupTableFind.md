# LookupTableFind

```c
REG_OP(LookupTableFind)
    .INPUT(handle, TensorType({DT_RESOURCE}))
    .INPUT(keys, TensorType({DT_INT32, DT_INT64, DT_STRING}))
    .INPUT(default_value, TensorType({DT_DOUBLE, DT_FLOAT, \
        DT_INT32, DT_INT64, DT_STRING, DT_BOOL}))
    .OUTPUT(values, TensorType({DT_DOUBLE, DT_FLOAT, DT_INT32, \
        DT_INT64, DT_STRING, DT_BOOL}))
    .REQUIRED_ATTR(Tout, Type)
    .OP_END_FACTORY_REG(LookupTableFind)
```

## Brief

Looks up keys in a table, outputs the corresponding values. 

## Inputs

The dtype of input handle must be resource. Inputs include:
- handle: A Tensor of type resource. Handle to the table.
- keys: A Tensor. Any shape. Keys to look up.
- default_value: A Tensor.

## Outputs

values: A Tensor. Has the same type as default_value. 

## Attributes

Tout: Specified type of ouput values. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 handle: resource
- input1 keys: int32,int64,string
- input2 default_value: bool,double,float32,int32,int64,string
- output0 values: bool,double,float32,int32,int64,string

## Third-party framework compatibility.

Compatible with tensorflow LookupTableFind operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
