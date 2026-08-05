# HardSwishGradV2

```c
REG_OP(HardSwishGradV2)
    .INPUT(gradOutput, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .INPUT(self, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OUTPUT(out, TensorType({DT_FLOAT16, DT_FLOAT, DT_BF16}))
    .OP_END_FACTORY_REG(HardSwishGradV2)
```

```c
gradSelf_{i} = begin{cases}
0, self_{i} <= -3,
self_{i} / 3 + 0.5, -3 < self_{i} < 3,
1, self_{i} >= 3
end{cases}

out_{i} = gradOutput_{i} times gradSelf_{i}
```

## Brief

Computes the gradient for the hard_swish of "self" .
calculating formula:

## Inputs

Two inputs, including:
- gradOutput: A tensor. Must be one of the following types: float16, float32, bfloat16
- self: A tensor with the same type as "gradOutput" .

## Outputs

out: A tensor with the same type as "gradOutput".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 gradOutput: bfloat16,float16,float32
- input1 self: bfloat16,float16,float32
- output0 out: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the PyTorch operator HardSwishGrad after v2.8.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
