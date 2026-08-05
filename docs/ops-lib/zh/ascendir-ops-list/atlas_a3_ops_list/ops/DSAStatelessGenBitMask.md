# DSAStatelessGenBitMask

```c
REG_OP(DSAStatelessGenBitMask)
    .INPUT(count, TensorType({DT_INT64}))
    .INPUT(seed, TensorType({DT_UINT64}))
    .INPUT(dropout, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(offset, TensorType({DT_UINT64}))
    .OUTPUT(out, TensorType({DT_UINT1, DT_UINT8}))
    .ATTR(random_algorithm, String, "Philox")
    .ATTR(output_dtype, String, "uint8")
    .OP_END_FACTORY_REG(DSAStatelessGenBitMask)
```

## Brief

Generate State less DSA dropout data in random. 

## Inputs

include:
- count: The shape of the input tensor.
- seed: If seed is set to be non-zero, the random number
generator is seeded by the given seed. Otherwise, it is seeded by a random seed
- dropout: A Tensor. Must be one of the following types: float16, float32, bfloat16.  Must in [0,1).
- offset: A Tensor. Must be one of the following types: uint64.

## Outputs

y:Output (1-D) random number using float and bf data format . 
@see DSAStatelessGenBitMask()

## Attributes

- random_algorithm:The default value is "Philox".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### Dsa Core
- input0 count: int64
- input1 seed: uint64
- input2 dropout: bfloat16,float16,float32
- input3 offset: int64
- output0 out: uint1,uint8


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
