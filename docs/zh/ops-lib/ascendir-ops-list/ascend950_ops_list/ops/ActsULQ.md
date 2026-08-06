# ActsULQ

```c
REG_OP(ActsULQ)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(clamp_min, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(clamp_max, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(clamp_min_mask, TensorType({DT_BOOL, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(clamp_max_mask, TensorType({DT_BOOL, DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(x_clamped_loss, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(fixed_min, Bool, false)
    .ATTR(num_bits, Int, 8)
    .OP_END_FACTORY_REG(ActsULQ)
```

## Brief

ActsULQ fake quantization operator for QAT

## Inputs

- data: A Tensor. Must be one of: float16, float32.
- clamp_min: A Tensor. Same dtype as data.
- clamp_max: A Tensor. Same dtype as data.

## Outputs

- output: A Tensor. Same dtype as data.
- clamp_min_mask: A Tensor. Same dtype as data.
- clamp_max_mask: A Tensor. Same dtype as data.
- x_clamped_loss: A Tensor. Same dtype as data.

## Attributes

- fixed_min: Bool. Default false.
- num_bits: Int. Default 8.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 clamp_min: float16,float32
- input2 clamp_max: float16,float32
- output0 y: float16,float32
- output1 clamp_min_mask: float16,float32
- output2 clamp_max_mask: float16,float32
- output3 x_clamped_loss: float16,float32


---

[Back to Operator Specifications (Ascend950)](../README.md)
