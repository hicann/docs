# Cdist

```c
REG_OP(Cdist)
    .INPUT(x1, TensorType({DT_FLOAT16, DT_FLOAT}))
    .INPUT(x2, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(p, Float, 2.0)
    .OP_END_FACTORY_REG(Cdist)
```

## Brief

Computes batched the p-norm distance between each pair of
the two collections of row vectors. 

## Inputs

Two inputs, including:
- x1: A tensor with shpae: BxPXM. Must be one of the following types:
    float16, float32. 
- x2: A tensor with shpae: BxRxM. Must be one of the following types:
    float16, float32. 

## Outputs

y: A Tensor with the same type of x1's and with shape BxPxR. 

## Attributes

- p: An optional float >= 0 or inf. Defaults to 2.0.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x1: float16,float32
- input1 x2: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator Cdist. 


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
