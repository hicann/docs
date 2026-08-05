# SqrtGrad

```c
REG_OP(SqrtGrad)
    .INPUT(y, TensorType(UnaryDataType))
    .INPUT(dy, TensorType(UnaryDataType))
    .OUTPUT(z, TensorType(UnaryDataType))
    .OP_END_FACTORY_REG(SqrtGrad)
```

## Brief

Computes the gradient of the square root of "x" with regard to its
input. grad = dy * 0.5/y, where y = sqrt(x), and "dy" is the corresponding
input gradient. Support broadcasting operations.

## Inputs

Two inputs, including:
- y: A ND Tensor of type of UnaryDataType. Must be one of the following types: float64,
float16, float32, complex128, complex64.
- dy: A ND Tensor. Has the same dtype as "y".

## Outputs

z: A ND Tensor. Has the same dtype as "y". 

## Data Types

Note: The preceding prototypes are applicable to all chips, but the Data Types listed below are applicable only to the current chip.
### AI Core
- input0 y: float16,float32
- input1 dy: float16,float32
- output0 z: float16,float32
### AI CPU

## Attention Constraints

"dy" has the same shape and type as "y".


---

[Back to Operator Specifications (Atlas Training Series Product)](../README.md)
