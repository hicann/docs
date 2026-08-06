# RandomChoiceWithMask

```c
REG_OP(RandomChoiceWithMask)
    .INPUT(x, TensorType({DT_BOOL}))
    .OUTPUT(y, TensorType({DT_INT32}))
    .OUTPUT(mask, TensorType({DT_BOOL}))
    .ATTR(count, Int, 0)
    .ATTR(seed, Int, 0)
    .ATTR(seed2, Int, 0)
    .OP_END_FACTORY_REG(RandomChoiceWithMask)
```

## Brief

Shuffle index of no-zero element . 

## Inputs

include:
x:A tensor <= 5-D . 

## Outputs

- y:2-D tensor, no-zero element index.
- mask:1-D, whether the corresponding index is valid .
@see RandomChoiceWithMask()

## Attributes

- count:the count of output, if 0, out all no-zero elements.
- seed:If either seed or seed2 are set to be non-zero, the random number generator is seeded by the given seed.
Otherwise, it is seeded by a random seed.
- seed2:A second seed to avoid seed collision .


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
