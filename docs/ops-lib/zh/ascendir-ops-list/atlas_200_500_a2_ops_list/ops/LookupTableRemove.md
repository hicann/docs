# LookupTableRemove

```c
REG_OP(LookupTableRemove)
    .INPUT(table_handle, TensorType({DT_RESOURCE}))
    .INPUT(keys,TensorType({RealNumberType, DT_BOOL, DT_STRING}))
    .OP_END_FACTORY_REG(LookupTableRemove)
```

## Brief

Remove keys in the given table. 

## Inputs

- table_handle: A Tensor of type resource. Handle to the table.
- keys: A Tensor. Any shape. Keys to remove.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 table_handle: resource
- input1 keys: bool,double,float16,float32,int8,int16,int32,int64,string,uint8,uint16,uint32,uint64

## Third-party framework compatibility.

Compatible with tensorflow LookupTableInsert operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
