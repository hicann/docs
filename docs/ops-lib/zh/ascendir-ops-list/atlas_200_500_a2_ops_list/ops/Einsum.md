# Einsum

```c
REG_OP(Einsum)
    .DYNAMIC_INPUT(x, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .OUTPUT(y, TensorType({DT_FLOAT16, DT_FLOAT, DT_INT32}))
    .REQUIRED_ATTR(equation, String)
    .REQUIRED_ATTR(N, Int)
    .OP_END_FACTORY_REG(Einsum)
```

## Brief

Concatenates a list of N tensors along the first dimension.

## Inputs

- x: A list of Tensors. Must be one of the following types:  int32,
float16, float32. Tensors to be concatenated. All must have size 1 in
 the first dimension and same shape. It's a dynamic input. 

## Outputs

- y: Sums the product of the elements of the input operands along
dimensions specified
using a notation based on the Einstein summation convention. 

## Attributes

- equation: The subscripts for the Einstein summation.
- N: tensor size of input.

## Attention Constraints

Input N must be Int. 

## Third-party framework compatibility

Compatible with Tensorflow 2.x einsum operator.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
