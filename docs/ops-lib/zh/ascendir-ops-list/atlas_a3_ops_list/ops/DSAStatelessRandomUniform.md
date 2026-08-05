# DSAStatelessRandomUniform

```c
REG_OP(DSAStatelessRandomUniform)
    .INPUT(count, TensorType({DT_INT64}))
    .INPUT(seed, TensorType({DT_UINT64}))
    .INPUT(low, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT64, DT_UINT32, DT_UINT64}))
    .INPUT(high, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT64, DT_UINT32, DT_UINT64}))
    .INPUT(counter, TensorType({DT_UINT64}))
    .OUTPUT(out, TensorType({DT_BF16, DT_FLOAT16, DT_FLOAT, DT_INT32, DT_INT64, DT_UINT32, DT_UINT64}))
    .ATTR(random_algorithm, String, "Philox")
    .OP_END_FACTORY_REG(DSAStatelessRandomUniform)
```

## Brief

Generate State less DSA uniform data in random. 

## Inputs

include:
- count: The shape of the input tensor.
- seed: If seed is set to be non-zero, the random number
generator is seeded by the given seed. Otherwise, it is seeded by a random seed
- low: A Tensor, value should be 0.. Must be one of the following types: float16, float32, bfloat16.
- high: A Tensor, value should be 1.. Must be one of the following types: float16, float32, bfloat16.
- Parameters low and high must be configured at the same time, and low < high.
- counter: A Tensor. Must be one of the following types: uint64.

## Outputs

y:Output (1-D) random number using float and bf data format . 
@see DSAStatelessRandomUniform()

## Attributes

- random_algorithm:The default value is "Philox".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### Dsa Core
- input0 count: int64
- input1 seed: uint64
- input2 low: bfloat16,float16,float32,int32,int64,uint32,uint64
- input3 high: bfloat16,float16,float32,int32,int64,uint32,uint64
- input4 counter: uint64
- output0 out: bfloat16,float16,float32,int32,int64,uint32,uint64


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
