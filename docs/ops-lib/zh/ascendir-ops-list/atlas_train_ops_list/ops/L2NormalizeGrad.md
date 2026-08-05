# L2NormalizeGrad

```c
REG_OP(L2NormalizeGrad)
    .INPUT(x, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(y, TensorType({DT_FLOAT, DT_FLOAT16}))
    .INPUT(dy, TensorType({DT_FLOAT, DT_FLOAT16}))
    .OUTPUT(dx, TensorType({DT_FLOAT, DT_FLOAT16}))
    .ATTR(dim, ListInt, {})
    .ATTR(eps, Float, 0.0001f)
    .OP_END_FACTORY_REG(L2NormalizeGrad)
```

## Brief

Performs the backpropagation of L2Normalize for training scenarios .

## Inputs

Three inputs, including:
- x: A ND Tensor(1D-8D) of type float16 or float32, specifying
the eigenvalue of forward inputs.
- y: A ND Tensor(1D-8D) of type float16 or float32, specifying
the normalization result of the forward output. the same shape with x.
- dy: A ND Tensor(1D-8D) of type float16 or float32, specifying
the reverse input gradient. the same shape with x . 

## Outputs

dx: A ND Tensor(1D-8D), Reverse gradient of eigenvalue "x". Has the same shape as "x" . 

## Attributes

- dim: A required attribute of type int, specifying the axis to be
normalized.  Defaults to {}.
- eps: An optional attribute of type float, specifying the lower limit of
normalization. Defaults to "1e-4" . 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: float16,float32
- input1 y: float16,float32
- input2 dy: float16,float32
- output0 dx: float16,float32

## Third-party framework compatibility

Compatible with the L2 scenario of PyTorch operator NormalizeGrad.


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
