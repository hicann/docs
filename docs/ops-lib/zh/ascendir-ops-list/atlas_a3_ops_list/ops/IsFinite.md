# IsFinite

```c
REG_OP(IsFinite)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BOOL, DT_UINT8, DT_INT8, DT_UINT16,
                          DT_INT16, DT_INT32, DT_UINT32, DT_UINT64, DT_INT64}))
    .OUTPUT(y, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(IsFinite)
```

## Brief

Compute element-wise finiteness, return a boolean tensor.

## Inputs

x: An ND tensor. Support 1D ~ 8D. Must be one of the following types:
bfloat16, float16, float32, double, bool, uint8, int8, uint16, int16, int32, uint32, uint64, int64.

## Outputs

y: An ND tensor. Support 1D ~ 8D. Must have the same shape and format as input "x", and dytpe is bool.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bool
### AI CPU
- input0 x: bool,double,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: bool

## Third-party framework compatibility.

Compatible with tensorflow IsFinite operator.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
