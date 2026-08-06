# Embedding

```c
REG_OP(Embedding)
    .INPUT(x, TensorType({DT_COMPLEX64, DT_COMPLEX32, DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT16, DT_INT32, DT_INT64,
                          DT_INT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_UINT8, DT_BOOL, DT_BF16}))
    .INPUT(indices, TensorType::IndexNumberType())
    .OUTPUT(y, TensorType({DT_COMPLEX64, DT_COMPLEX32, DT_DOUBLE, DT_FLOAT, DT_FLOAT16, DT_INT16, DT_INT32, DT_INT64,
                           DT_INT8, DT_UINT16, DT_UINT32, DT_UINT64, DT_UINT8, DT_BOOL, DT_BF16}))
    .OP_END_FACTORY_REG(Embedding)
```

## Brief

According to the indices, return the embedding vectors. 

## Inputs

- x: A required Tensor.Must be one of the following types: complex64, complex32, double, float32,
float16, int16, int32, int64, int8, uint16, uint32, uint64, uint8, bool, bfloat16.
- indices: A required Tensor. A index Tensor. Must be one of the following types: int32, int64.

## Outputs

y: The embedded output tensor. Has the same type and format as input "x".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,bool,complex32,complex64,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64
- input1 indices: int32,int64
- output0 y: bfloat16,bool,complex32,complex64,double,float16,float32,int8,int16,int32,int64,uint8,uint16,uint32,uint64

## Attention Constraints

Based on whether all the 1s in indexed_sizes are consecutive, it is categorized into a continuous axis scenario and
a non-continuous axis scenario.


---

[Back to Operator Specifications (Ascend950)](../README.md)
