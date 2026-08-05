# NonZero

```c
REG_OP(NonZero)
    .INPUT(x, TensorType({DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT8, DT_UINT8,
                          DT_INT16, DT_UINT16, DT_INT32, DT_UINT32, DT_INT64,
                          DT_UINT64, DT_BOOL, DT_BF16}))
    .OUTPUT(y, TensorType({DT_INT64, DT_INT32}))
    .ATTR(transpose, Bool, false)
    .ATTR(dtype, Type, DT_INT64)
    .OP_END_FACTORY_REG(NonZero)
```

## Brief

Returns a tensor containing the indices of all non-zero
elements of input.

## Inputs

x: A Tensor. Must be one of the following types: float16, bfloat16, float32,
   int32, int64, double, int8, uint8, int16, uint16, uint32, uint64, bool.

## Outputs

y: A Tensor. Must be one of the following types: int32, int64. 

## Attributes

- transpose: An optional attribute. Type is bool. Defaults to False.
- dtype: An optional attribute. Specifying the output data type.
    Either "int32" or "int64". Default to "int64". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,float16,float32,int8,uint8
- output0 y: int32,int64
### AI CPU
- input0 x: bool,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: int32,int64

## Third-party framework compatibility

Compatible with the PyTorch operator NonZero.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
