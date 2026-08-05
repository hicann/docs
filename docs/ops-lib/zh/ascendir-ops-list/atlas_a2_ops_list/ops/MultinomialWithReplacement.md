# MultinomialWithReplacement

```c
REG_OP(MultinomialWithReplacement)
    .INPUT(x, TensorType({ DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16 }))
    .INPUT(seed, TensorType({ DT_INT64 }))
    .INPUT(offset, TensorType({ DT_INT64 }))
    .OUTPUT(y, TensorType({ DT_INT64 }))
    .REQUIRED_ATTR(numsamples, Int)
    .ATTR(replacement, Bool, false)
    .OP_END_FACTORY_REG(MultinomialWithReplacement)
```

## Brief

Returns a tensor where each row contains numsamples indices sampled from the multinomial distribution. 

## Inputs

x:  A Tensor. Must be one of the following types: float16, float, double.
- seed:If seed is set to be -1, and offset is set to be 0, the random number
generator is seeded by a random seed. Otherwise, it is seeded by the given seed.
- offset:To avoid seed collision .

## Outputs

y: A Tensor, with type int64 . 

## Attributes

- numsamples: An Required int, number of samples to draw.
- replacement: An optional bool, whether to draw with replacement or not. Defaults to false.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: bfloat16,double,float16,float32
- input1 seed: int64
- input2 offset: int64
- output0 y: int64

## Third-party framework compatibility

@ Compatible with the Pytorch operator multinomial.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
