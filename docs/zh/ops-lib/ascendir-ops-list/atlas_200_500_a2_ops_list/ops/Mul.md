# Mul

```c
REG_OP(Mul)
    .INPUT(x1, "T1")
    .INPUT(x2, "T2")
    .OUTPUT(y, "T3")
    .DATATYPE(T1, TensorType({DT_BOOL, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_UINT8, DT_INT8,
                              DT_UINT16, DT_INT16, DT_INT32, DT_INT64, DT_BF16,
                              DT_COMPLEX64, DT_COMPLEX128, DT_COMPLEX32}))
    .DATATYPE(T2, TensorType({DT_BOOL, DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_UINT8, DT_INT8,
                              DT_UINT16, DT_INT16, DT_INT32, DT_INT64, DT_BF16,
                              DT_COMPLEX64, DT_COMPLEX128, DT_COMPLEX32}))
    .DATATYPE(T3, Promote({"T1", "T2"}))
    .OP_END_FACTORY_REG(Mul)
```

## Brief

Returns x1 * x2 element-wise.
y = x1 * x2. Support broadcasting operations.

## Inputs

- x1: A ND tensor. Must be one of the following types: bool, float16, float32, bfloat16,
float64, uint8, int8, uint16, int16, int32, int64, complex32, complex64, complex128.
- x2: A ND tensor. Must be one of the following types: bool, float16, float32, bfloat16,
float64, uint8, int8, uint16, int16, int32, int64, complex32, complex64, complex128.
The shape of x1 and x2 must meet the requirements of the broadcast relationship.

## Outputs

y: A ND tensor. Must be one of the following types: bool, float16, float32, float64, bfloat16,
uint8, int8, uint16, int16, int32, int64, complex32, complex64, complex128.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: bfloat16,bool,float16,float32,int8,int16,int32,int64,uint8
- input1 x2: bfloat16,bool,float16,float32,int8,int16,int32,int64,uint8
- output0 y: bfloat16,bool,float16,float32,int8,int16,int32,int64,uint8
### AI CPU
- input0 x1: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 x2: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 y: double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

"x1" and "x2" have incompatible shapes or types.

## Third-party framework compatibility

Compatible with the TensorFlow operator Multiply.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
