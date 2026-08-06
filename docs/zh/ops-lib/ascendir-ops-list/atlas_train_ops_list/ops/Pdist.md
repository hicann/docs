# Pdist

```c
REG_OP(Pdist)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(p, Float, 2.0)
    .OP_END_FACTORY_REG(Pdist)
```

## Brief

Calculate the P-norm distance between vectors  function. 

## Inputs

One inputs, including:
x: A tensor. Must be one of the following types:
    float16, float32. 

## Outputs

y: A Tensor with the same type and shape of x. 

## Attributes

p: An optional float.Defaults to 2. 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core

## Third-party framework compatibility

Compatible with the Pytorch operator Pdist. 


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
