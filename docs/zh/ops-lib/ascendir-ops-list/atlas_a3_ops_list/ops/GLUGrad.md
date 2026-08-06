# GLUGrad

```c
REG_OP(GLUGrad)
      .INPUT(y_grad, TensorType::FloatingDataType())
      .INPUT(x, TensorType::FloatingDataType())
      .OUTPUT(x_grad, TensorType::FloatingDataType())
      .ATTR(dim, Int, -1)
      .OP_END_FACTORY_REG(GLUGrad)
```

## Brief

Calculates the backward outputs of the function "GLU".

## Inputs

- y_grad: A Tensor. Must be one of the following types: float16, float32.
- x: A Tensor of the same type as `y_grad`, but with a size that is twice as large as `y_grad` along the axis `dim`.

## Outputs

x_grad: A Tensor of the same type as `y_grad` and of the same shape as `x`.

## Attributes

dim: An optional int, specifying the dimension along which the GLU is performed.
It should be in the range [-rank(x), rank(x)). Defaults to -1.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y_grad: float16,float32
- input1 x: float16,float32
- output0 x_grad: float16,float32

## Third-party framework compatibility

Compatible with the Pytorch operator GLUGrad.


---

[Back to Operator Specifications (Atlas A3 Series Product)](../README.md)
