# DSARandomTruncatedNormal

```c
REG_OP(DSARandomTruncatedNormal)
    .INPUT(count, TensorType({DT_INT64}))
    .INPUT(seed, TensorType({DT_UINT64}))
    .INPUT(mean, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(stdev, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(out, TensorType({DT_FLOAT16, DT_FLOAT32, DT_BF16}))
    .ATTR(random_algorithm, String, "Philox")
    .OP_END_FACTORY_REG(DSARandomTruncatedNormal)
```

## Brief

Generate DSA truncatenormal data in random. 

## Inputs

include:
- count: The shape of the input tensor.
- seed: If seed is set to be non-zero, the random number
generator is seeded by the given seed. Otherwise, it is seeded by a random seed
- mean: A Tensor. Must be one of the following types: float16, float32, double
- stdev: A Tensor. Must be one of the following types: float16, float32, double.

## Outputs

y:Output (1-D) random number using float and bf data format . 
@see DSARandomTruncatedNormal()

## Attributes

- random_algorithm:The default value is "Philox".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### Dsa Core
- input0 count: int64
- input1 seed: uint64
- input2 mean: bfloat16,float16,float32
- input3 stdev: bfloat16,float16,float32
- output0 out: bfloat16,float16,float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
