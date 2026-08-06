# SelectV2

```c
REG_OP(SelectV2)
    .INPUT(condition, TensorType({DT_BOOL}))
    .INPUT(then,TensorType({DT_COMPLEX128,DT_COMPLEX64,DT_DOUBLE,DT_FLOAT,DT_FLOAT16,DT_INT16,DT_INT32,DT_INT64,DT_INT8,DT_UINT16,DT_UINT32,DT_UINT64,DT_UINT8,DT_BOOL,DT_BF16}))
    .INPUT(else,TensorType({DT_COMPLEX128,DT_COMPLEX64,DT_DOUBLE,DT_FLOAT,DT_FLOAT16,DT_INT16,DT_INT32,DT_INT64,DT_INT8,DT_UINT16,DT_UINT32,DT_UINT64,DT_UINT8,DT_BOOL,DT_BF16}))
    .OUTPUT(result,TensorType({DT_COMPLEX128,DT_COMPLEX64,DT_DOUBLE,DT_FLOAT,DT_FLOAT16,DT_INT16,DT_INT32,DT_INT64,DT_INT8,DT_UINT16,DT_UINT32,DT_UINT64,DT_UINT8,DT_BOOL,DT_BF16}))
    .OP_END_FACTORY_REG(SelectV2)
```

## Brief

Select elements from "then" or "else", depending on "condition" .

## Inputs

Three inputs, including:
- condition: A tensor of type bool. If condittion is true, outputs will be set as then. If condittion is false, outputs will be set as else.
- then: A tensor. Must be one of the following types: float16, float32, double, int8, int16, int32, int64,
uint8, uint16, uint32, uint64, complex64, complex128, bool, bfloat16
- else: A tensor of the same type as "then" .

## Outputs

result: A tensor. Has the same type as "then" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 condition: bool
### AI CPU
- input0 condition: bool
- input1 then: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input2 else: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- output0 result: complex64,complex128,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

- The input tensors of condition, then and else must meet the broadcast relationship.
- The shape of result is formed by broadcasting condition, then and else.

## Third-party framework compatibility

Compatible with the TensorFlow operator SelectV2.


---

[Back to Operator Specifications (Ascend950)](../README.md)
