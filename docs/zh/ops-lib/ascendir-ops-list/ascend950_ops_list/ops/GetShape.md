# GetShape

```c
REG_OP(GetShape)
    .DYNAMIC_INPUT(x, TensorType({DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32,
                                  DT_UINT32, DT_INT64, DT_UINT64, DT_BOOL}))
    .OUTPUT(y, TensorType({DT_INT32}))
    .OP_END_FACTORY_REG(GetShape)
```

## Brief

Returns the shape of one or more tensors. 

## Inputs

x: A list of tensors. Must be one of the following types: float32、float16、int8、
int16、uint16、uint8、int32、int64、uint32、uint64、bool、double. 

## Outputs

y: A tensor. The shape of the input tensors. Output type is int32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: int32

## Third-party framework compatibility

Compatible with the TensorFlow operator GetShape.


---

[Back to Operator Specifications (Ascend950)](../README.md)
