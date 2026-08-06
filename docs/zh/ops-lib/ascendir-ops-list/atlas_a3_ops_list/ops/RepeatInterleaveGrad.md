# RepeatInterleaveGrad

```c
REG_OP(RepeatInterleaveGrad)
    .INPUT(y_grad, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .INPUT(repeats, TensorType({DT_INT32, DT_INT64}))
    .OUTPUT(x_grad, TensorType({DT_FLOAT, DT_FLOAT16, DT_BF16}))
    .ATTR(axis, Int, -1)
    .OP_END_FACTORY_REG(RepeatInterleaveGrad)
```

## Brief

Gradient op for RepeatInterleave op.

## Inputs

Two inputs:
- y_grad: A Tensor with any format. Support float, float16, bf16.
- repeats: A Tensor with dim = 1 or a Scalar. Support int32 or int64.

## Outputs

x_grad: A Tensor, which is the same dtype as y_grad. Support float, float16, bf16.

## Attributes

axis: An optional int32, specifying the axis to repeat. Defaults to -1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y_grad: bfloat16,float16,float32
- input1 repeats: int32,int64
- output0 x_grad: bfloat16,float16,float32

## Attention Constraints

- "axis" must be within the rank of the input tensor.
- The elements in "repeats" cannot all be zero.

## Third-party framework compatibility

Compatible with the PyTorch operator the grad of RepeatInterleave.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
