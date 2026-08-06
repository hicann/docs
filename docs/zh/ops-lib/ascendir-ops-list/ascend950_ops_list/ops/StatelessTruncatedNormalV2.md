# StatelessTruncatedNormalV2

```c
REG_OP(StatelessTruncatedNormalV2)
    .INPUT(shape, TensorType({DT_INT32, DT_INT64}))
    .INPUT(key, TensorType({DT_UINT64}))
    .INPUT(counter, TensorType({DT_UINT64}))
    .INPUT(alg, TensorType({DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT, DT_DOUBLE}))
    .ATTR(dtype, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(StatelessTruncatedNormalV2)
```

## Brief

Outputs random values from a truncated normal distribution (stateless version). 

## Inputs

Inputs include:
shape: A tensor. Must be one of the following types: int32, int64 . 
key: A tensor of type uint64 with shape [1]. The key for the random number generator. 
counter: A tensor of type uint64 with shape [2]. The counter for the random number generator. 
counter: Shape[1] for threefry, Shape[1] for philox. 
alg: A scalar tensor of type int32. The algorithm id (1 = Philox). 
alg: The default setting in this operator is 1. 

## Outputs

- y: A tensor of types: float16, float32, bfloat16, double. A tensor of the specified shape
filled with random truncated normal values. 

## Attributes

- dtype: An optional type. Defaults to DT_FLOAT. The data type of y. It supports 1(float16), 27(bfloat16) and 0(float32).

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 shape: int32,int64
- input1 key: uint64
- input2 counter: uint64
- input3 alg: int32
- output0 y: bfloat16,float16,float32
### AI CPU
- input0 shape: int32,int64
- input1 key: uint64
- input3 alg: int32
- output0 y: bfloat16,double,float16,float32

## Attention Constraints

This is a stateless version. The same key+counter input always produces the same output.
Only Philox algorithm (alg=1) is currently supported.

## Third-party framework compatibility

Compatible with tensorflow StatelessTruncatedNormalV2 operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
