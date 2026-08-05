# Geometric

```c
REG_OP(Geometric)
    .INPUT(x, TensorType({ DT_FLOAT16,DT_FLOAT }))
    .OUTPUT(y, TensorType({ DT_FLOAT16,DT_FLOAT }))
    .REQUIRED_ATTR(p, Float)
    .ATTR(seed, Int, 0)
    .OP_END_FACTORY_REG(Geometric)
```

## Brief

Fills a tensor with elements drawn from the geometric distribution. 

## Inputs

x:  A Tensor. Must be one of the following types: float16, float. 

## Outputs

y: A Tensor list with same type as "x" . 

## Attributes

- p: The probability of experimental success in Bernoulli's experiment.
- seed: An optional int. Defaults to 0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

@ Compatible with the Pytorch operator Geometric.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
