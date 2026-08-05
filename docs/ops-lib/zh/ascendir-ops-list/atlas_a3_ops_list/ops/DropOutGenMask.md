# DropOutGenMask

```c
REG_OP(DropOutGenMask)
    .INPUT(shape, TensorType({ DT_INT32, DT_INT64 }))
    .INPUT(prob, TensorType({ DT_FLOAT16, DT_FLOAT }))
    .OUTPUT(y, TensorType({ DT_UINT8 }))
    .ATTR(seed, Int, 0)
    .ATTR(seed2, Int, 0)
    .OP_END_FACTORY_REG(DropOutGenMask)
```

## Brief

Generate random bit mask for dropout.

## Inputs

include:
- shape:The shape of the output tensor. Must be one of the following types: int32, int64.
- prob:0-D. Number of bit 1 . Must be one of the following types: float16, float32.

## Outputs

y:Output (1-D) random number using uint data format. A Tensor of type uint8. 

## Attributes

- seed: An optional int. If either seed or seed2 are set to be non-zero, the random number
generator is seeded by the given seed. Otherwise, it is seeded by a random seed.
- seed2: An optional int. A second seed to avoid seed collision.

## Attention Constraints

The output is aligned with 128 bits.
@see DropOutGenMask()


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
