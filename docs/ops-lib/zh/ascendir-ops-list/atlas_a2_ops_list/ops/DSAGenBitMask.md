# DSAGenBitMask

```c
REG_OP(DSAGenBitMask)
    .INPUT(count, TensorType({DT_INT64}))
    .INPUT(seed, TensorType({DT_UINT64}))
    .INPUT(dropout, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(out, TensorType({DT_UINT1, DT_UINT8}))
    .ATTR(random_algorithm, String, "Philox")
    .ATTR(output_dtype, String, "uint8")
    .OP_END_FACTORY_REG(DSAGenBitMask)
```

## Brief

Generate DSA random bit mask for dropout. 

## Inputs

- count:The shape of the input tensor. Must be int64.
- seed:If seed is set to be non-zero, the random number
generator is seeded by the given seed. Otherwise, it is seeded by a random seed. Must be int64.
- dropout:0-D. Number of bit 1. Must be one of the following dtypes:float16, float32, bf16. Must in [0,1).

## Outputs

y:If the dtype of y is uint8, output (1-D) random number using uint8 data format. Else if the dtype of y is uint1,
output random number with the shape of count using uint1 data format.
Must be one of the following types:uint1, uint8.
@see DSAGenBitMask()

## Attributes

- random_algorithm:The default value is "Philox".
- output_dtype:The dtype of output. The default value is "uint1".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### Dsa Core
- input0 count: int64
- input1 seed: uint64
- input2 dropout: bfloat16,float16,float32
- output0 out: uint1,uint8


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
