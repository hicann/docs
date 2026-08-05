# L2Normalize

```c
REG_OP(L2Normalize)
    .INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT}))
    .ATTR(axis, ListInt, {})
    .ATTR(eps, Float, 1e-4f)
    .OP_END_FACTORY_REG(L2Normalize)
```

## Brief

Normalizes elements of a specific dimension of eigenvalues (L2) .

## Inputs

x: A ND Tensor(1D-8D) of type float16 or float32, specifying the eigenvalue . 

## Outputs

y: A ND Tensor(1D-8D) of type float16 or float32, specifying the eigenvalue for normalization. 

## Attributes

- axis: A optional required attribute of type list, specifying the axis for normalization Defaults to {} .
- eps: An optional attribute of type float, specifying the lower limit of normalization. Defaults to "1e-4" .

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- output0 y: float16,float32

## Third-party framework compatibility

Compatible with the L2 scenario of PyTorch operator Normalize.


---

[Back to Operator Specifications (Atlas A2 Series Product)](../README.md)
