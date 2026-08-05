# CeluV2

```c
REG_OP(CeluV2)
    .INPUT(x, TensorType({DT_FLOAT,DT_FLOAT16, DT_BF16}))
    .OUTPUT(y, TensorType({DT_FLOAT,DT_FLOAT16, DT_BF16}))
    .ATTR(alpha, Float, 1.0)
    .OP_END_FACTORY_REG(CeluV2)
```

## Brief

Continuously Differentiable Exponential Linear Uints:
      Perform the linear uint element-wise on the input tensor X using formula:
      max(0, x) + min(0, alpha * (exp(x/alpha) - 1)).

## Inputs

x: A ND tensor. Support 1D~8D. Must be one of the following types: bfloat16, float16, float32.

## Outputs

y: A tensor. Must be one of the following types: bfloat16, float16, float32 for the normalized result.
Has the same type, shape and format as input x.

## Attributes

alpha: An optional float32. Defines at which negative value the CELU saturates. Defaults to "1.0".

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

- Compatible with ONNX's Celu operator


---

[Back to Operator Specifications (Atlas Inference Series Product)](../README.md)
