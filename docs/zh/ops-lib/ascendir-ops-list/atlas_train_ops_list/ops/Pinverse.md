# Pinverse

```c
REG_OP(Pinverse)
    .INPUT(x, TensorType({ DT_FLOAT, DT_DOUBLE }))
    .OUTPUT(y, TensorType({ DT_FLOAT, DT_DOUBLE }))
    .ATTR(rcond, Float, 1e-15f)
    .OP_END_FACTORY_REG(Pinverse)
```

## Brief

Computes the generalized inverse of any matrix.

## Inputs

- x: input matrix. Must be one of the following types:
    double, float. 

## Outputs

y: A Tensor with the same type and shape of x's transpose. 

## Attributes

- rcond: An optional float >= 0 or inf. Defaults to 1e-15.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI CPU
- input0 x: double,float32
- output0 y: double,float32


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
