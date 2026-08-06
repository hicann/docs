# GroupNormSiluQuant

```c
REG_OP(GroupNormSiluQuant)
    .INPUT(x, TensorType({DT_BF16, DT_FLOAT16}))
    .OPTIONAL_INPUT(gamma, TensorType({DT_BF16, DT_FLOAT16}))
    .OPTIONAL_INPUT(beta, TensorType({DT_BF16, DT_FLOAT16}))
    .INPUT(quantScale, TensorType({DT_FLOAT}))
    .OUTPUT(yOut, TensorType({DT_INT8}))
    .OUTPUT(meanOut, TensorType({DT_BF16, DT_FLOAT16}))
    .OUTPUT(rstdOut, TensorType({DT_BF16, DT_FLOAT16}))
    .REQUIRED_ATTR(num_groups, Int)
    .ATTR(eps, Float, 0.00001f)
    .ATTR(activate_silu, Bool, true)
    .OP_END_FACTORY_REG(GroupNormSiluQuant)
```

## Brief

Computes GroupNorm on x, optionally applies SiLU, then quantizes the result to int8.
  y = round(silu(group_norm(x, num_groups, gamma, beta, eps)) / quantScale), clamped to [-128, 127].

## Inputs

- x: Required tensor of type float16 or bfloat16. Shape is (N, C, *), dim0 = N, dim1 = C.
- gamma: Optional 1-D tensor, same dtype as x, element count = C.
- beta: Optional 1-D tensor, same dtype as x, element count = C.
- quantScale: Required 1-D float32 tensor. Element count must be 1 (per-tensor) or C (per-channel).

## Outputs

- yOut: Quantized output, int8, same shape as x.
- meanOut: Group mean, same dtype as x, shape (N, num_groups).
- rstdOut: Reciprocal of group standard deviation, same dtype as x, shape (N, num_groups).

## Attributes

- num_groups: Required int. C must be divisible by num_groups.
- eps: Optional float. Defaults to 1e-5. Must be greater than 0.
- activate_silu: Optional bool. Whether to apply SiLU. Defaults to true.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16
- input1 gamma: bfloat16,float16
- input2 beta: bfloat16,float16
- input3 quantScale: float32
- output0 yOut: int8
- output1 meanOut: bfloat16,float16
- output2 rstdOut: bfloat16,float16

## Third-party framework compatibility

It is a custom operator. It has no corresponding operator in Caffe, ONNX, TensorFlow, or PyTorch.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
