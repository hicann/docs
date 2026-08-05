# StatelessUniform

```c
REG_OP(StatelessUniform)
    .INPUT(shape, TensorType({DT_INT64}))
    .INPUT(seed, TensorType({DT_INT64}))
    .INPUT(offset, TensorType({DT_INT64}))
    .INPUT(from, TensorType({DT_DOUBLE}))
    .INPUT(to, TensorType({DT_DOUBLE}))
    .OUTPUT(y, TensorType({DT_FLOAT, DT_BF16, DT_FLOAT16}))
    .ATTR(dtype, Type, DT_FLOAT)
    .OP_END_FACTORY_REG(StatelessUniform)
```

## Brief

Outputs deterministic pseudorandom values from a uniform distribution in [from, to),
       bit-exact with CUDA/PyTorch H20 GPU uniform_() implementation. 

## Inputs

- shape: 1-D tensor. The shape of the output tensor. Must be one of the following types: int64.
- seed: 0-D scalar. Philox algorithm seed. Must be one of the following types: int64.
- offset: 0-D scalar. Philox algorithm offset. Must be one of the following types: int64.
- from: 0-D scalar. Lower bound of the random range (inclusive). Must be one of the following types: double.
- to: 0-D scalar. Upper bound of the random range (exclusive). Must be one of the following types: double.

## Outputs

y: Returns random values with specified shape. Values are in [from, to).
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
- input3 from: double
- input4 to: double
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with PyTorch torch.Tensor.uniform_() operator (bit-exact with CUDA H20).


---

[Back to Operator Specifications (Ascend950)](../README.md)
