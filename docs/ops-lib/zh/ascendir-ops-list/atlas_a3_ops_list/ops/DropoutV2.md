# DropoutV2

```c
REG_OP(DropoutV2)
    .INPUT(x, TensorType({ DT_FLOAT16, DT_FLOAT }))
    .INPUT(seed, TensorType({ DT_FLOAT }))
    .OUTPUT(y, TensorType({ DT_FLOAT16, DT_FLOAT }))
    .OUTPUT(mask, TensorType({ DT_FLOAT }))
    .OUTPUT(seed, TensorType({ DT_FLOAT }))
    .REQUIRED_ATTR(p, Float)
    .OP_END_FACTORY_REG(DropoutV2)
```

## Brief

During training, randomly zeroes some of the elements of the input tensor
with probability

## Inputs

- x: A ND Tensor. Must be one of the following data types: float32, float16
- seed: A ND Tensor. Must be one of the following data types: float32. Seed is
a random seed used to generate deterministic random numbers that control which
neurons are retained in the Dropout operation and which neurons are turned off.

## Outputs

- y: A tensor with the same shape and type as "x".
- mask: A tensor. Must be float32. Indicates which neural network units (neurons)
are "dropped" or retained during training.
- new_seed: A tensor with the same shape and type as "seed".

## Attributes

p: Probability of an element to be zeroed. A required Tensor. Must be float32.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 seed: float32
- output0 y: float16,float32
- output1 mask: float32
- output2 seed: float32


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
