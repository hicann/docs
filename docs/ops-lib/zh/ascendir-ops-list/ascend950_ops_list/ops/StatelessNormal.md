# StatelessNormal

```c
REG_OP(StatelessNormal)
    .INPUT(shape, TensorType({DT_INT64}))
    .INPUT(seed, TensorType({DT_INT64}))
    .INPUT(offset, TensorType({DT_INT64}))
    .INPUT(mean, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16}))
    .INPUT(std, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_BF16, DT_FLOAT}))
    .ATTR(dtype, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(StatelessNormal)
```

## Brief

Outputs deterministic pseudorandom values from a normal distribution,
with GPU-parity (same seed+offset produces same sequence as CUDA). 

## Inputs

- shape: 1-D. The shape of the output tensor. Must be one of the following types: int64.
- seed: 0-D. Seed for the Philox4x32-10 RNG algorithm. Must be one of the following types: int64.
- offset: 0-D. Offset for the Philox4x32-10 RNG algorithm. Must be one of the following types: int64.
- mean: Scalar or tensor. Mean of the normal distribution. Must be one of the following types: float, float16, bfloat16. Only the 0th element is used for calculation if a tensor is input.
- std: Scalar or tensor. Standard deviation of the normal distribution. Must be one of the following types: float, float16, bfloat16. Only the 0th element is used for calculation if a tensor is input.

## Outputs

y: Returns random values with specified shape.
Must be one of the following types: float16, bfloat16, float32. 

## Attributes

dtype: Output data type. Must be one of the following types: float16, bfloat16, float32.
Defaults to float32. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 shape: int64
- input1 seed: int64
- input2 offset: int64
- input3 mean: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with PyTorch torch.normal (stateless, GPU-parity mode).


---

[Back to Operator Specifications (Ascend950)](../README.md)
