# GLU

```c
REG_OP(GLU)
      .INPUT(x, TensorType::FloatingDataType())
      .OUTPUT(y, TensorType::FloatingDataType())
      .ATTR(dim, Int, -1)
      .OP_END_FACTORY_REG(GLU)
```

## Brief

Activation function called Gated Linear Unit, calculate result by input ND tensor x and integer dim.

## Inputs

x: ND input tensor. Must be one of the following types: float16, float32.

## Outputs

y: A Tensor. Has the same type as "x".

## Attributes

dim: the dimension will be chunked into halves, default to be -1, the dimension itself must be even.

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 x: bfloat16,float16,float32
- output0 y: bfloat16,float16,float32

## Third-party framework compatibility

Compatible with caffe correlation custom operator.


---

[Back to Operator Specifications (Ascend950)](../README.md)
