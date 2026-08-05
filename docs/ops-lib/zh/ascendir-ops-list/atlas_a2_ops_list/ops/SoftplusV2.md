# SoftplusV2

```c
REG_OP(SoftplusV2)
    .INPUT(x, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .OUTPUT(y, TensorType({ DT_FLOAT, DT_FLOAT16, DT_BF16 }))
    .ATTR(beta, Float, 1.0)
    .ATTR(threshold, Float, 20.0)
    .OP_END_FACTORY_REG(SoftplusV2)
```

## Brief

Calculates the softplus loss function with attributes of beta and threshold.

## Inputs

One inputs, including:
x: A mutable tensor, which supports 1D-8D defaultly. Format support ND. Must be one of the following types:
float16, float32, bfloat16.

## Outputs

y:A mutable tensor of the same type, shape and format as "x".

## Attributes

- beta: An optional float. Defaults to "1.0".
Control the steepness of the beta function.
- threshold: An optional float. Defaults to "20.0".
Define a function to switch the threshold from nonlinear to linear.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator Softplus.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
