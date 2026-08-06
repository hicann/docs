# StatelessBernoulliV2

```c
REG_OP(StatelessBernoulliV2)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_DOUBLE}))
    .INPUT(seed, TensorType({DT_INT64}))
    .INPUT(offset, TensorType({DT_INT64}))
    .OUTPUT(y, TensorType({DT_INT8, DT_UINT8, DT_INT16, DT_UINT16, DT_INT32, DT_UINT32, DT_INT64, DT_UINT64, DT_BOOL,
                           DT_FLOAT16, DT_FLOAT, DT_DOUBLE, DT_BF16}))
    .ATTR(dtype, Type, DT_UNDEFINED)
    .OP_END_FACTORY_REG(StatelessBernoulliV2)
```

## Brief

Draws binary random numbers (0 or 1) from a Bernoulli distribution.The input tensor
should be a tensor containing probabilities p (a value in the range [0, 1]) to be used for
drawing the binary random number, where an output of 1 is produced with ptobability p and
an output of 0 is produced with probability (1-p). 

## Inputs

include:
- x: All values in input have to be in the range:[0, 1].
- seed: If seed is set to be -1, and offset is set to be 0, the random number
generator is seeded by a random seed. Otherwise, it is seeded by the given seed.
- offset: To avoid seed collision.

## Outputs

y: The returned output tensor only has values 0 or 1, same shape as input tensor. 

## Attributes

- dtype: The data type for the elements of the output tensor. if not specifed,
we will use the data type of the input tensor. 

## Third-party framework compatibility

Compatible with the Onnx operator Bernoulli


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
