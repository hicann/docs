# AssignAddVariableOp

```c
REG_OP(AssignAddVariableOp)
    .INPUT(resource, TensorType({DT_RESOURCE}))
    .INPUT(value, TensorType({DT_FLOAT, DT_FLOAT16, DT_INT8, DT_INT16, \
        DT_UINT16, DT_UINT8, DT_INT32, DT_INT64, DT_BOOL, DT_DOUBLE}))
    .REQUIRED_ATTR(dtype, Type)
    .OP_END_FACTORY_REG(AssignAddVariableOp)
```

## Brief

Adds a value to the current value of a variable. 

## Inputs

- resource:Handle to the resource in which to store the variable.
- value:The value by which the variable will be incremented.

## Attributes

dtype: required, type. 
@see AssignAddVariableOp.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 resource: resource
- input1 value: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
